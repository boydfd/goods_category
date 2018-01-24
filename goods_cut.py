import pandas as pd
import re
import numpy as np
import operator
import jieba as jieba
import matplotlib.pyplot as plt

letter2good = {
    'M': '邮件',
    'V': '贵重物品',
    'S': '急件',
    'P': '普货',
    'L': '活体动物',
    'X': '海鲜',
    'G': '果蔬',
    'H': '鲜花',
    'D': '鲜冻品',
    'O': '其他',
    'A': '所有',
}


def cut_good_name(word):
    word = word.upper()
    words = list(jieba.cut(word))
    if words[0] in letter2good:
        words[0] = letter2good[words[0]]
    if len(words) > 1 and words[0] == words[1]:
        words.pop(0)
    return words


def normalize(inventory):
    result_inventory = {}
    print('inventory', inventory)
    for item in inventory.items():
        if not item[0]:
            continue
        item_name = item[0]
        item_names = cut_good_name(item_name)

        for name in item_names:
            if name not in result_inventory:
                result_inventory[name] = 0
            result_inventory[name] += item[1]
    return result_inventory


def cut_goods(user_dict='./output/filtered_dict_without_english.csv',
              source_goods_path='./sources/goods.csv', output_path="./output/needed_words.csv"):
    jieba.load_userdict(user_dict)
    print('loaded')
    df = pd.read_csv(source_goods_path)

    splited = df[df.columns[0]].dropna().map(lambda row: re.split('[ \\\\/,;；，、|()（）.]',
                                                                  row)).dropna()

    inventory = {}

    def insert_items(items):
        for item in items:
            inventory[item] = 1 if item not in inventory else inventory[item] + 1

    splited.apply(insert_items)

    inventory = normalize(inventory)

    sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)

    pattern = re.compile('^[a-zA-Z0-9]{2,}$')
    filtered_inventory = list(filter(lambda item: item[1] > 2 and (pattern.match(item[0]) or 0 <
                                                                   len(item[0])
                                                                   <= 4),
                                     sorted_inventory))
    inventory_count = np.asarray([value for _, value in filtered_inventory]).sum()
    filtered_inventory.insert(0, ('all', inventory_count))
    pd.DataFrame(np.asarray(filtered_inventory)).to_csv(output_path, index=False,
                                                        header=False)


if __name__ == '__main__':
    # jieba.load_userdict('./sources/filtered_dict.txt')
    jieba.load_userdict('./output/filtered_dict_without_english.csv')
    print('loaded')
    df = pd.read_csv('./sources/goods.csv')

    splited = df['cnvcGoodsName'].dropna().map(lambda row: re.split('[ \\\\/,;；，、|()（）.]',
                                                                    row)).dropna()

    inventory = {}


    def insert_items(items):
        for item in items:
            inventory[item] = 1 if item not in inventory else inventory[item] + 1


    splited.apply(insert_items)

    inventory = normalize(inventory)

    sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)

    pattern = re.compile('^[a-zA-Z0-9]{2,}$')
    filtered_inventory = list(filter(lambda item: item[1] > 2 and (pattern.match(item[0]) or 0 <
                                                                   len(item[0])
                                                                   <= 4),
                                     sorted_inventory))
    inventory_count = np.asarray([value for _, value in filtered_inventory]).sum()
    filtered_inventory.insert(0, ('all', inventory_count))
    pd.DataFrame(np.asarray(filtered_inventory)).to_csv("./output/needed_words.csv", index=False,
                                                        header=False)
    # np.asarray([value for _, value in list(filter(lambda item: item[1] > 10, sorted_inventory))]).sum()
    pass
