import operator
import numpy as np
import re
from urllib.request import urlopen

import jieba
import pandas as pd
from gensim import similarities

from goods_cut import cut_good_name
from jd_parser import get_word_link_from_baike
from jd_similarity import get_similarity, Similarity
from utilities import get_content_from_html, retry_for_timeout, get_saved_similarities


def cut_good_name():
    df = pd.read_csv('./output/goods_without_duplicity.csv')

    jieba.load_userdict('./output/filtered_dict_without_english.csv')

    def cut_with_comma(word):
        return ','.join([item for item in cut_good_name(word) if item != '' and item != ' '])

    pattern = re.compile('[ \\\\/,;；，、|()（）.]')
    df['name'] = df['name'].map(lambda row: re.sub(pattern, ' ',
                                                   row)).dropna().map(cut_with_comma)

    df.to_csv('./output/goods_cut.csv', index=False)


def get_baike(word):
    def get():
        _, link = get_word_link_from_baike(word)
        return urlopen(link, timeout=5).read().decode('utf-8')

    decode = retry_for_timeout(get)
    return get_content_from_html(decode)


def get_all_similarities(baikes, similarity):
    all_similarities = []
    for baike in baikes:
        all_similarities.append(similarity.calculate_similarity_lsi(baike))
    return all_similarities


def process_similarity(calc_similarity, output_path):
    similarity = get_similarity()
    saved_similarities_dict = get_saved_similarities()

    df = pd.read_csv('./output/goods_cut.csv')
    with open(output_path, 'w') as f:
        for index, names in enumerate(df['name'].values):
            names = names.split(',')
            saved_similarities = []
            baikes = []
            rest_names = []
            for name in names:
                if name not in saved_similarities_dict:
                    rest_names.append(name)
                    print(name, '不存在')
                else:
                    saved_similarities.append(saved_similarities_dict[name])
            for name in rest_names:
                try:
                    baikes.append(get_baike(name))
                except:
                    pass
            all_similarities = get_all_similarities(baikes, similarity)
            for i, sim in enumerate(all_similarities):
                saved_similarities_dict[rest_names[i]] = sim
            all_similarities = all_similarities + saved_similarities
            sims = list(enumerate(calc_similarity(all_similarities)))
            sims = ['name:%s sub:%s sim:%s' % (
                similarity.inverse_index[similarity.names[item[0]]],
                similarity.names[item[0]],
                item[1]
            ) for item in sorted(sims, key=operator.itemgetter(1), reverse=True)[:5]]
            f.write('%s %s\n' % (names, str(sims)))
            if index % 10 == 0:
                f.flush()


def average_similarity(all_similarities):
    if len(all_similarities) == 0:
        return all_similarities
    all_similarities = np.asarray(all_similarities)
    return np.mean(all_similarities, axis=0)


if __name__ == '__main__':
    process_similarity(average_similarity, './output/similarities/standard_result_tmp.txt')
