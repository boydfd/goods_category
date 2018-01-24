from categorize import get_omitted_baike_links
from crawler import crawl
from goods_cut import cut_goods
from goods_preprocessor import dict_preprocessor
from jd_similarity import save_goods_similarities
from utilities import get_words, parse_html

if __name__ == '__main__':
    dict_preprocessor()
    cut_goods(user_dict='./output/filtered_dict_without_english.csv',
              source_goods_path='./sources/goods.csv', output_path="./output/needed_words.csv")

    get_omitted_baike_links(category_path='./sources/category.txt',
                            output_missed_path='./output/missed_standard_words.txt',
                            output_link_path='./output/standard_words_link.txt')

    crawl('./output/standard_words_link.txt', './htmls')

    words = get_words('./output/standard_words_link.txt')
    for word in words:
        parse_html(word, './htmls')

    save_goods_similarities()


