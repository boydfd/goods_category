import _pickle as cPickle
import pandas as pd
import numpy as np
from gensim.models.wrappers import FastText
from gensim.models.keyedvectors import KeyedVectors
from scipy import spatial

from word_vector import words

g_dict = cPickle.load(open("./sources/jd.p", "rb"))
del g_dict['图书\n/ 音像\n/ 电子书']
del g_dict['房产\n/ 汽车\n/ 汽车用品']
del g_dict['机票\n/ 酒店\n/ 旅游\n/ 生活']
del g_dict['理财\n/ 众筹\n/ 白条\n/ 保险']
category = [second_key for _,first in g_dict.items() for second_key,second in first.items()]


category_vec = {key: np.asarray(words[key], dtype=np.float32) for key in category if key in words}
# model = KeyedVectors.load_word2vec_format('./sources/wiki.zh.vec', binary=False)
df = pd.read_csv('./output/needed_words.csv')
def get_category(item):
    print("-"*100)
    print(item)
    if item not in words:
        return

    item_vec = np.asarray(words[item], dtype=np.float32)
    for name, cat in category_vec.items():
        print(name, 1-spatial.distance.cosine(item_vec, cat))
    print("-"*100)

# def get_category(item):
#     print("-"*100)
#     print(item)
#     if item not in words:
#         return
#     for cat in category:
#         if cat not in words:
#             continue
#         print(cat, model.similarity(cat, item))
#     print("-"*100)
df['all'].map(get_category)


pass
