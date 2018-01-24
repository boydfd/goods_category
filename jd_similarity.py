import operator
import pickle
import os.path
from urllib.request import urlopen
import pandas as pd

import jieba
import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities
from urllib3.util import timeout

from categorize import parse_categories_dict, parse_categories, create_inverse_index
from jd_parser import get_rectified_word
from utilities import get_standard_words, get_content_from_html


class Similarity:
    def __init__(self, words):
        jieba.load_userdict('./sources/filtered_dict.txt')
        stop_words = './items/stop_words.txt'
        stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
        self.stopwords = [w.strip() for w in stopwords]
        self.stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']

        self.init_category(words)
        with open('./sources/category.txt') as file:
            words = parse_categories_dict(parse_categories(file.read()))
            self.inverse_index = create_inverse_index(words)

    def tokenization_with_path(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
            return self.tokenization(text)
            # words = pseg.cut(text)
            # for word, flag in words:
            #     if flag not in self.stop_flag and word not in self.stopwords:
            #         result.append(word)
            # return result

    def tokenization(self, text):
        result = []
        words = pseg.cut(text)
        for word, flag in words:
            if flag not in self.stop_flag and word not in self.stopwords:
                result.append(word)
        return result

    def init_category(self, words):
        self.filenames = ['./jd_items/%s' % word for word in words]
        self.names = words

        corpus = []
        for each in self.filenames:
            corpus.append(self.tokenization_with_path(each))

        dictionary = corpora.Dictionary(corpus)
        self.dictionary = dictionary

        doc_vectors = [dictionary.doc2bow(text) for text in corpus]

        tfidf = models.TfidfModel(doc_vectors)
        tfidf_vectors = tfidf[doc_vectors]

        lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=len(corpus))
        self.lsi = lsi
        self.lsi_vector = lsi[tfidf_vectors]

    def calculate_similarity_lsi_sorted(self, sims):
        sims = list(enumerate(sims))
        return ['name:%s sub:%s sim:%s' % (
            self.inverse_index[self.names[item[0]]],
            self.names[item[0]],
            item[1]
        ) for item in sorted(sims, key=operator.itemgetter(1), reverse=True)[:5]]

    def calculate_similarity_lsi(self, query):
        query = self.tokenization(query)
        query_bow = self.dictionary.doc2bow(query)
        # print(query_bow)
        query_lsi = self.lsi[query_bow]
        # print(query_lsi)
        index = similarities.MatrixSimilarity(self.lsi_vector)
        sims = index[query_lsi]
        return sims


def get_baike_from_word(simi, word):
    rectified_word = get_rectified_word(word)
    link = list(rectified_word.values())[0]
    print('start', word)
    decode = urlopen(link, timeout=5).read().decode('utf-8')
    print(len(decode))
    print('end', word)
    simis = simi.calculate_similarity_lsi(
        get_content_from_html(decode)
    )
    return simi.calculate_similarity_lsi_sorted(simis)


def get_baike_from_words(simi, words, output_path, error_path):
    with open(output_path, 'w') as output, open(error_path, 'w') as error:
        for index, word in enumerate(words):
            try:
                from_word = get_baike_from_word(simi, word)
                output.write('%s %s\n' % (word, str(from_word)))
            except:
                error.write(str(word) + '\n')

            if index % 10 == 0:
                output.flush()
                error.flush()


similarity = None


def get_similarity():
    global similarity
    if similarity:
        return similarity
    path = './model/standard_similarity.pickle'
    if not os.path.isfile(path):
        similarity = Similarity(get_standard_words())
        pickle_out = open(path, "wb")
        pickle.dump(similarity, pickle_out)
        pickle_out.close()
    else:
        similarity = pickle.load(open(path, "rb"))
    return similarity


def get_all_goods():
    df = pd.read_csv('./output/needed_words.csv')
    words = df['all'].tolist()

    get_baike_from_words(get_similarity(), words, './output/similarities/jd_result1.txt',
                         './output/similarities/jd_error.txt')


if __name__ == '__main__':
    get_all_goods()
# similarity.calculate_similarity_lsi('./items/手机壳_.txt')
# similarity.calculate_similarity_lsi('./items/上衣.txt')
# similarity.calculate_similarity_lsi('./items/石榴.txt')
# similarity.calculate_similarity_lsi('./items/糖果.txt')
# similarity.calculate_similarity_lsi('./items/酱牛肉.txt')
# similarity.calculate_similarity_lsi('./items/鞋.txt')
