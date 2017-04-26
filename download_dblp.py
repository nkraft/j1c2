from paths import mkdir_p
import requests
from itertools import chain
import os
import time


def page_url_gen(base_url, base_page, start_year, end_year, year_to_page_id = lambda x : x):
    for year in range(start_year, end_year + 1):
        yield '{0}/{1}{2}.html'.format(base_url.rstrip('/'), base_page, year_to_page_id(year))


def download_page(page_url, session, output_dir):
    page_file = os.path.join(output_dir, page_url.rsplit('/', 1)[-1])
    request = session.get(page_url)
    with open(page_file, 'wb') as page:
        page.write(request.content)
    time.sleep(2)


def main(args):
    output_dir = 'dblp'
    mkdir_p(output_dir)

    session = requests.Session()
    session.proxies = { 'http' : 'http://proxy.us.abb.com:8080' }

    software_page_urls = page_url_gen('http://dblp.uni-trier.de/db/journals/software/', 'software', 2007, 2016, lambda x: x - 1983)
    fse_page_urls = page_url_gen('http://dblp.uni-trier.de/db/conf/sigsoft', 'fse', 2007, 2016)

    for page_url in chain(software_page_urls, fse_page_urls):
        download_page(page_url, session, output_dir)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))

