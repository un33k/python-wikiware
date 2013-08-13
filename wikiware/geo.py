# -*- coding: utf-8 -*-

import re

from fetcher import WikiwareFetch
from parser import WikiwareAPIParseSummary
from patterns import *
import defaults

def get_wiki_summary(title):
    """ Get the summary for a geography section of a wiki page """
    summary = None
    f = WikiwareFetch()
    html = f.fetch_api_parse(title=title, section="0")
    if html:
        p = WikiwareAPIParseSummary(content=html)
        if p.is_category(defaults.WIKIWARE_CATEGORY_TYPE_GEOGRAPHY):
            p.set_attr(attr={'id': pattern_coordinates})
            summary = p.get_summary()
    return summary



