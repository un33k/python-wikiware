# -*- coding: utf-8 -*-

import re

from fetcher import WikiwareFetch
from parser import WikiwareAPIParseSummary

def get_wiki_summary(title):
    summary = None
    fetcher = WikiwareFetch()
    html = fetcher.fetch_api_parse(title=title, section="0")
    if html:
        parser = WikiwareAPIParseSummary()
        summary = parser.get_summary(html)
    return summary



