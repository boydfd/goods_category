from bs4 import BeautifulSoup
import re
import jieba

from jd_parser import get_words_omitted_in_baike
from utilities import flatten


def read_category_from_html():
    pattern = re.compile('[\u4e00-\u9fa5、]+')
    re.match(pattern, '')
    url = 'https://wenku.baidu.com/view/781bb826aaea998fcc220ece.html'

    chinese = ['一', '二', '三', '四', '五', '七', '八', '九', '十', ]
    useless_name = ['项目', '货物名称', '货物分类', 1, 2, 3, 4, 5, 6, 7, 8, 9, '\n', ' ', '']
    path = './sources/category-previous.html'
    with open(path) as file:
        soup = BeautifulSoup(file.read())
        soup.find_all(class_='reader-word-layer')
        '\n'.join(
            [x.text for x in soup.find_all(class_='reader-word-layer') if
             re.match(pattern, x.text) and
             x.text not
             in
             useless_name][:64])


def parse_categories(text):
    # with open('./sources/category.txt') as f:
    #     for line in f:
    rows = text.split('\n')
    chinese_number = ['一', '二', '三', '四', '五', '七', '八', '九', '十', ]
    mark = None
    result = {}
    for row in rows:
        if row[0] in chinese_number:
            mark = row
            result[mark] = ''
        else:
            result[mark] += row + '、'
    return result


def parse_categories_dict(categories):
    def is_not_empty(item):
        return item is not ''

    return {key[key.index('、') + 1:]: list(filter(is_not_empty, re.split('[、， ]+', value)))
            for (key, value) in categories.items()}


def create_inverse_index(dictionary):
    return {value: key for key, values in dictionary.items() for value in [key] + values}
    # return dictionary


def get_standard_first_category(category):
    with open('./sources/category.txt') as file:
        words = parse_categories_dict(parse_categories(file.read()))
        inverse_words = create_inverse_index(words)
        return inverse_words[category]


class CategoryInverseIndex:
    def __init__(self):
        with open('./sources/category.txt') as file:
            words = parse_categories_dict(parse_categories(file.read()))
            self.inverse_words = create_inverse_index(words)

    def get_standard_first_category(self, category):
        return self.inverse_words[category]


if __name__ == '__main__':
    with open('./sources/category.txt') as file:
        words = parse_categories_dict(parse_categories(file.read()))
        words = flatten(words.values())
        get_words_omitted_in_baike(words, 'standard')

pass
