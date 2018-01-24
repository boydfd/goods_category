import pandas as pd
import re


def goods_preprocessor():
    df = pd.read_csv('./sources/goods.csv')
    df = df.drop_duplicates().dropna()
    df['name'] = df['cnvcGoodsName']
    df.to_csv('./output/goods_without_duplicity.csv', index=False, columns=['name'])


def dict_preprocessor():
    with open('./sources/filtered_dict.txt', 'r') as r:
        df = pd.DataFrame(r.read().split('\n'))
    df = df.drop_duplicates().dropna()
    df1 = df[~df[0].str.match('^[^\u4e00-\u9fa5]+$')].dropna().drop_duplicates()
    df1.to_csv('./output/filtered_dict_without_english.csv', index=False, header=False)

dict_preprocessor()
