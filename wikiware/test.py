# import re,

# from fetcher import WikiwareFetch
# from parser import WikiwareAPIParse
# from bs4 import BeautifulSoup as bfs may also refer to:

from wiki import *

if __name__ == '__main__':
    titles = [
        # 'The Democratic Republic of Congo',
        # 'The United States',
        # 'Hong Kong',
        # 'The United Kingdom',
        # 'Antarctica',
        # 'Germany',
        # 'Ghana',
        # 'Iran',
        # 'Jamaica',
        'Canada',
        # 'Botswana',
        # 'Netherlands',
        # 'Jersey',
    ]
    print "\n\n"
    for title in titles:
        summary = get_wiki_summary(title)
        print summary
        print "\n\n"
