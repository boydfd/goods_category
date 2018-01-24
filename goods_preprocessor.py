import pandas as pd


def goods_preprocessor():
    df = pd.read_csv('./sources/goods.csv')
    df = df.drop_duplicates().dropna()
    df['name'] = df['cnvcGoodsName']
    df.to_csv('./output/goods_without_duplicity.csv', index=False, columns=['name'])


def dict_preprocessor(source_dict_path='./sources/filtered_dict.txt',
                      output_path='./output/filtered_dict_without_english.csv'):
    with open(source_dict_path, 'r') as r:
        df = pd.DataFrame(r.read().split('\n'))
    df = df.drop_duplicates().dropna()
    df1 = df[~df[0].str.match('^[^\u4e00-\u9fa5]+$')].dropna().drop_duplicates()
    df1.to_csv(output_path, index=False, header=False)
