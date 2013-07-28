# -*- coding: utf-8 -*-

import re
import HTMLParser
from bs4 import BeautifulSoup

from patterns import *
from utils import *

import defaults

class WikiwareAPIParse(object):
    """ Parse Wikipedia contents from API Calls (html)"""

    def __init__(self, content):
        self.set_content(content)

    def set_content(self, content):
        self.html = HTMLParser.HTMLParser().unescape(content)
        self.soup = BeautifulSoup(self.html)

    def _clean_punctuations(self, text):
        text = pattern_single_dash.sub('-', text)
        text = pattern_translation.sub('', text)
        text = pattern_long_dash.sub(' ', text)
        text = pattern_comma.sub(', ', text)
        text = pattern_dot.sub('. ', text)
        text = pattern_semicolon.sub('; ', text)

        text = pattern_single_space.sub(' ', text)
        return text

    def _remove_duplicates(self, text):
        dups = ['\t', '\n', '\r', ' ', '-', ':', ';', '_', '-', ',',]
        for d in dups:
            text = re.sub('(?mis)%s{1,}' % d, d, text)
        return text

    def _strip_extras(self, text):
        strip = ['\t', '\n', '\r\n', '\r', ' ',]
        for s in strip:
            text = text.strip(s)
        return text

    def _remove_extras(self, text):
        text = pattern_parentheses.sub('', pattern_parentheses.sub('', text))
        replace = ['(', ')', '{', '}', '[', ']',]
        for r in replace:
            text = text.replace(r, ' ')
        return text
    
    def _cleanup(self, text):
        text = self._remove_extras(text)
        text = self._clean_punctuations(text)
        text = self._strip_extras(text)
        text = self._remove_duplicates(text)
        return text

    def _is_summary_tag(self, tag):
        return tag.name == 'p' and not tag.has_attr('class') and not tag.has_attr('id')

    def _validate_query(self, text):
        if defaults.WIKIWARE_QUERY_NOT_FOUND_TEXT in text:
            return ''
        else:
            return text

    def _purge_non_summary_nodes(self, soup):
        goners = soup.find_all(id=pattern_coordinates)
        goners += soup.find_all(id=pattern_cite_reference)
        goners += soup.find_all(attrs={'class': pattern_error})
        goners += soup.find_all('table')
        for node in goners:
            node.extract()
        return soup

    def get_summary_paragraphs(self, soup):
        summary_paragraphs = []
        soup = self._purge_non_summary_nodes(soup)
        paragraphs = soup.find_all(self._is_summary_tag)
        for p in paragraphs:
            summary_paragraphs.append(self._cleanup(p.get_text()))
        return summary_paragraphs

    def get_summary(self, force=False):
        if hasattr(self, 'summary') and self.summary and not force:
            return self.summary
        self.summary = ''
        paragraphs = self.get_summary_paragraphs(self.soup)
        self.summary = "\n".join(paragraphs)
        self.summary = self._validate_query(self.summary)
        return self.summary




