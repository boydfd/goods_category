from _socket import timeout
import os.path
from urllib.request import urlretrieve, urlopen


def crawl(input_path, output_dir):
    max_try_times = 10
    with open(input_path, 'r') as file:
        words = [row.split(' ') for row in file.read().split('\n') if row.split(' ')[0] is
                 not '']
        for (word, link) in words:
            path = output_dir + '/%s' % word
            if not os.path.isfile(path):
                with open(path, 'w') as file:
                    for i in range(max_try_times):
                        try:
                            page = urlopen(link, timeout=5).read().decode('utf-8')
                            file.write(page)
                            break
                        except timeout:
                            if i + 1 == max_try_times:
                                raise timeout
            # urlretrieve(link, path)

if __name__ == '__main__':
    crawl('./output/standard_words_link.txt', './htmls')
