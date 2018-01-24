import unittest

from jd_parser import ListItem, parse_jd, JdItems, get_rectified_word

unittest.TestCase.maxDiff = None


class TestJdParser(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.maxDiff = None

    def test_compareItemInListItem_withListItem_shouldReturnEqual(self):
        self.assertEqual('房产', ListItem(['房产', '汽车', '汽车用品']))

    def test_parseJdItem_containMultipleNames_shouldSplitToNamesField(self):
        item = {
            '房产\n/ 汽车\n/ 汽车用品': {}
        }
        self.assertEqual({
            ListItem(['房产', '汽车', '汽车用品']): {},
        }, parse_jd(item))

    def test_transformJdItem_ToList_shouldContainBothKeyAndValue(self):
        item = {
            '房产\n/ 汽车\n/ 汽车用品': {
                'item1': [
                    'item2',
                    'item3/item4',
                ],
            },
        }
        self.assertEquals(
            sorted(['房产', '汽车', '汽车用品', 'item1', 'item2', 'item3', 'item4']),
            sorted(JdItems(item).to_list())
        )

    def test_transformJdItem_ToSimpleList_shouldContainBothKeyAndFirstLevelValue(self):
        item = {
            '房产\n/ 汽车\n/ 汽车用品': {
                'item1': [
                    'item2',
                    'item3/item4',
                ],
            },
        }
        self.maxDiff = None
        self.assertEquals(
            sorted(['房产', '汽车', '汽车用品', 'item1']),
            sorted(JdItems(item).to_simple_list())
        )

    def test_getRectifiedWord_fromNoun_shouldGetWordFromBaikeDirectly(self):
        word = '家电'
        self.assertEqual(
            {'家用电器': 'https://baike.baidu.com/item/%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8/3161846'},
            get_rectified_word(word)
        )

    def test_getRectifiedWord_fromWordWithNonNounWord_shouldUseNounToGetWordFromBaike(self):
        word = '潮流男包'
        self.assertEqual(
            {
                '潮流(词语释义)': 'https://baike.baidu.com/item/%E6%BD%AE%E6%B5%81/36237',
                '男包': 'https://baike.baidu.com/item/%E7%94%B7%E5%8C%85/7119206',
            },
            get_rectified_word(word)
        )
