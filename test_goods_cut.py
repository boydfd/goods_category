import unittest

from goods_cut import normalize, cut_good_name


class TestGoodsCut(unittest.TestCase):
    def test_normalizeGoodName_StartWithOneCategoryEnglishLetter_shouldRemoveLetter(
            self):
        inventory = {'p普货': 1}
        self.assertEqual({'普货': 1}, normalize(inventory))

    def test_normalizeGoodName_StartWithOneEnglishLetterIsNotCategory_shouldConvertLetterToUpperCase(
            self):
        inventory = {
            'u盘': 1,
            'U盘': 1,
            'p普货': 2,
        }
        self.assertEqual({'U盘': 2, '普货': 2}, normalize(inventory))

    def test_normalizeGoodName_onlyOneEnglishLetter_shouldConvertLetterToGoodName(self):
        inventory = {
            'p': 2,
            'p普货': 2,
            '普货': 2,
        }
        self.assertEqual({'普货': 6}, normalize(inventory))

    def test_normalizeGoodName_containMultipleWords_shouldCutToMultipleWords(self):
        inventory = {
            'p麻花麻酱衣服': 2,
            'pbc': 1,
        }
        self.assertEqual({'PBC': 1, '麻花': 2, '麻酱': 2, '衣服': 2, '普货': 2}, normalize(inventory))

    def test_cutGoodName_onlyOneEnglishLetter_shouldConvertLetterToGoodName(self):
        word = 'p'
        self.assertEqual(['普货'], cut_good_name(word))

    def test_cutGoodName_containMultipleWords_shouldCutToMultipleWords(self):
        word = 'p普货麻花麻酱衣服'
        self.assertEqual(['普货', '麻花', '麻酱', '衣服'], cut_good_name(word))
