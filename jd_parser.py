import _pickle as cPickle
import random
from _socket import timeout
from urllib.request import quote, urlopen, urlretrieve

import time
from bs4 import BeautifulSoup
import jieba.posseg as pseg

from utilities import get_filtered_dictionary, retry_for_timeout


class ListItem:
    def __init__(self, items):
        self.items = frozenset(items)

    def __eq__(self, other):
        if type(other) is ListItem:
            return self.items == other.items
        return other in self.items

    def __hash__(self) -> int:
        return self.items.__hash__()

    def __str__(self):
        return self.items.__str__()


def parse_first_level(key, value):
    return {
        ListItem(key.split('\n/ ')): value,
    }


def parse_jd(items):
    print({ListItem(key.split('\n/ ')): value for key, value in items.items()})
    return {ListItem(key.split('\n/ ')): value for key, value in items.items()}


class JdItems:
    def __init__(self, items):
        self.items = parse_jd(items)

    def to_list(self):
        result = []
        for key, value in self.items.items():
            result += key.items
            for key2, value2 in value.items():
                result.append(key2)
                result += [it for item in value2 for it in item.split('/')]
        return result

    def to_simple_list(self):
        result = []
        for key, value in self.items.items():
            result += key.items
            for key2, value2 in value.items():
                result.append(key2)
        return result


def get_word_link_from_baike(word):
    def get_soup():
        page = urlopen('https://baike.baidu.com/search/none?word=%s' % quote(word),
                       timeout=5).read()
        return BeautifulSoup(page, "html.parser")

    soup = retry_for_timeout(get_soup)
    try:
        found_result = soup.find(class_='result-title')
        return (found_result.text[:-5], found_result['href'])
    except AttributeError:
        return 'Unknown', ''


def get_rectified_word(word, max_try_times=5):
    def get_nouns(words):
        return [word for word, flag in words if
                flag in ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns",
                         "nsf", "nt", "nz", "nl", "ng"]]

    nouns = get_nouns(pseg.cut(word))
    result = {}
    if len(nouns) is 0:
        nouns.append(word)
    for noun in nouns:
        for i in range(max_try_times):
            try:
                word = get_word_link_from_baike(noun)
                break
            except timeout:
                if i + 1 == max_try_times:
                    raise timeout
        result[word[0]] = word[1]
    return result
    # return {item for noun in nouns for item in get_word_from_baike(noun)} \
    #     if len(nouns) is not 0 else  get_word_from_baike(word)


def get_words_omitted_in_baike(words, output_name):
    output_path = './output/missed_%s_words.txt' % output_name
    output_file = open(output_path, 'w')
    dictionary = get_filtered_dictionary()
    exist_words = []
    omitted_words = []
    rectified_words = []
    omitted_links = []
    exist_links = []
    for word in words:
        exist = word in dictionary
        if exist:
            exist_links.append(
                'https://baike.baidu.com/item/%s' % quote(word))
            exist_words.append(word)
        else:
            omitted_words.append(word)
            rectified_word = get_rectified_word(word)
            rectified_words.append(rectified_word)
            omitted_links.append(list(rectified_word.values())[0])
            # if word not in dictionary:
            #     print(word)
            # word_out = '%s %s\n' % (word, exist)
            # jd_words.write(word_out)
    omitted_words = [word.replace('/', '-') for word in omitted_words]
    links = exist_links + omitted_links
    combined_list = exist_words + omitted_words
    output_file.write('exist: %d, omitted: %d\n' % (len(exist_words), len(omitted_words)))
    for word in exist_words:
        word_out = '%s %s\n' % (word, True)
        output_file.write(word_out)
    for index, word in enumerate(omitted_words):
        word_with_link = rectified_words[index]
        if list(word_with_link.values())[0] is '':
            continue
        word_out = '%s %s %s\n' % (word, False, word_with_link)
        output_file.write(word_out)
    print(links)
    with open('./output/%s_words_link.txt' % output_name, 'w') as f:
        for index, word in enumerate(combined_list):
            path = './htmls/%s' % word

            link = links[index]
            if link is '':
                continue
            if link.startswith('/'):
                link = 'https://baike.baidu.com' + link

            f.write('%s %s\n' % (word, link))
            # urlretrieve(link, path)
    print('len of jd_words', len(words))


if __name__ == '__main__':
    g_dict = cPickle.load(open("./sources/jd.p", "rb"))
    # del g_dict['图书\n/ 音像\n/ 电子书']
    # del g_dict['房产\n/ 汽车\n/ 汽车用品']
    del g_dict['机票\n/ 酒店\n/ 旅游\n/ 生活']
    del g_dict['理财\n/ 众筹\n/ 白条\n/ 保险']

    out_path = './output/missed_jd_words'
    g_list = JdItems(g_dict).to_simple_list()
    get_words_omitted_in_baike(g_list, 'jd')

pass
