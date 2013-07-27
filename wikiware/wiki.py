# -*- coding: utf-8 -*-

import re

from fetcher import WikiwareFetch
from parser import WikiwareAPIParse

def get_wiki_summary(title):
    fetcher = WikiwareFetch()
    html = fetcher.fetch_api_parse(title=title, section="0")
    parser = WikiwareAPIParse(content=html)
    summary = parser.get_summary()
    return summary



