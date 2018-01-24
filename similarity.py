import operator

import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities

from html_ import get_words

stop_words = './items/stop_words.txt'
stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
stopwords = [w.strip() for w in stopwords]

whole_article = '_'

stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']


def tokenization(filename):
    result = []
    with open(filename, 'r') as f:
        text = f.read()
        words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result


# words = get_words()
# filenames = ['./jd_items/%s' % word for word in words]

filenames = [
    './items/手机%s.txt' % whole_article,
    './items/休闲食品%s.txt' % whole_article,
    './items/服装%s.txt' % whole_article,
    './items/水果%s.txt' % whole_article,
    './items/熟食%s.txt' % whole_article,
    './items/坚果%s.txt' % whole_article,
]

corpus = []
for each in filenames:
    corpus.append(tokenization(each))

print('corpus length' + str(len(corpus)))

dictionary = corpora.Dictionary(corpus)
print(dictionary)

doc_vectors = [dictionary.doc2bow(text) for text in corpus]
print('doc vector length' + str(len(doc_vectors)))
print(doc_vectors)

tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]

print(len(tfidf_vectors))
print(len(tfidf_vectors[0]))


def calculate_similarity(query):
    query = tokenization(query)
    query_bow = dictionary.doc2bow(query)
    print(len(query_bow))
    print(query_bow)

    index = similarities.MatrixSimilarity(tfidf_vectors)

    sims = index[query_bow]
    print(list(enumerate(sims)))


calculate_similarity('./items/手机壳_.txt')
calculate_similarity('./items/酱牛肉_.txt')
calculate_similarity('./items/坚果.txt')
calculate_similarity('./items/屏幕_.txt')
calculate_similarity('./items/上衣_.txt')
calculate_similarity('./items/鞋.txt')
calculate_similarity('./items/石榴.txt')

lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=len(corpus))
lsi.print_topics(3)

lsi_vector = lsi[tfidf_vectors]
for vec in lsi_vector:
    print(vec)


def calculate_similarity_lsi(query):
    query = tokenization(query)
    query_bow = dictionary.doc2bow(query)
    # print(query_bow)
    query_lsi = lsi[query_bow]
    # print(query_lsi)
    index = similarities.MatrixSimilarity(lsi_vector)
    sims = index[query_lsi]
    sims = list(enumerate(sims))
    # print(sims)
    print(['name:%s sim:%s' % (filenames[item[0]], item[1]) for item in
           sorted(sims,
                  key=operator.itemgetter(
                      1),
                  reverse=True)])

print('-' * 100)

calculate_similarity_lsi('./items/手机壳_.txt')
calculate_similarity_lsi('./items/酱牛肉_.txt')
calculate_similarity_lsi('./items/坚果.txt')
calculate_similarity_lsi('./items/屏幕_.txt')
calculate_similarity_lsi('./items/上衣_.txt')
calculate_similarity_lsi('./items/鞋.txt')
calculate_similarity_lsi('./items/石榴.txt')
calculate_similarity_lsi('./items/糖果.txt')


