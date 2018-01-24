import unittest

from categorize import parse_categories, parse_categories_dict, get_standard_first_category, \
    create_inverse_index


class CategoryParserTest(unittest.TestCase):
    def test_parseCategory_withChineseNumberStarted_shouldBeCategorizedToOneSection(self):
        categories = '''一、第一个类别
1类1，1类
2、1类3、1类4
二、第二个类别
2类1、
2类2，
2类3'''
        self.assertEquals({
            '一、第一个类别': '1类1，1类、2、1类3、1类4、',
            '二、第二个类别': '2类1、、2类2，、2类3、'
        }, parse_categories(categories))

    def test_parseCategory_withDictionaryType_shouldRemoveCategoryNumberAndCutSubCategories(self):
        categories = {
            '一、第一个类别': '1类1，1类2、、1类3、1类4',
            '二、第二个类别': '2类1、2类2，2类3、',
        }

        self.assertEquals({
            '第一个类别': ['1类1', '1类2', '1类3', '1类4'],
            '第二个类别': ['2类1', '2类2', '2类3'],
        }, parse_categories_dict(categories))

    def test_createInverseIndex_withDictionary_shouldReturnCorrectIndex(self):
        categories = {
            '第一个类别': ['1类1', '1类2', '1类3', '1类4'],
            '第二个类别': ['2类1', '2类2', '2类3'],
        }

        self.assertEquals({
            '第一个类别': '第一个类别',
            '1类1': '第一个类别',
            '1类2': '第一个类别',
            '1类3': '第一个类别',
            '1类4': '第一个类别',
            '第二个类别': '第二个类别',
            '2类1': '第二个类别',
            '2类2': '第二个类别',
            '2类3': '第二个类别',
        }, create_inverse_index(categories))

    def test_getFirstCategory_fromSecondCategory_shouldReturnCorrectCategory(self):
        category = '蟹类'
        self.assertEquals('海鲜', get_standard_first_category(category))

        category = '空气净化器'
        self.assertEquals('家电', get_standard_first_category(category))

        category = '手机'
        self.assertEquals('手机', get_standard_first_category(category))
