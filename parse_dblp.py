from paths import mkdir_p, replace_ext
from bs4 import BeautifulSoup
from collections import Counter
from glob import iglob
import os


def extract_authors(page_file):
    soup = BeautifulSoup(open(page_file, 'r'), 'lxml')
    author_tags = soup.select('span[itemprop="author"] > a')
    return {author_tag['href'].rsplit('/', 1)[-1] for author_tag in author_tags}


def main(args):
    dblp_dir = 'dblp'

    output_dir = 'authors'
    mkdir_p(output_dir)

    for page_file in iglob(os.path.join(dblp_dir, '*.html')):
        authors_file = os.path.join(output_dir, replace_ext(os.path.basename(page_file), '.txt'))
        with open(authors_file, 'w', encoding='utf-8') as authors:
            for author in extract_authors(page_file):
                print(author, file=authors)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

