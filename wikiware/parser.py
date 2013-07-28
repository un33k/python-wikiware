# -*- coding: utf-8 -*-

import re
import HTMLParser
from bs4 import BeautifulSoup

from patterns import *

import defaults

class WikiwareAPIParse(object):
    """ Parse Wikipedia contents from API Calls (html)"""

    def __init__(self, content):
        self.set_content(content)

    def set_content(self, content):
        self.html = HTMLParser.HTMLParser().unescape(content)
        self.soup = BeautifulSoup(self.html)

    def _purge_redundant_nodes(self, soup):
        goners = soup.findAll(id=coordinates_pattern)
        goners += soup.findAll(id=cite_reference_pattern)
        goners += soup.findAll(attrs={'class': error_pattern})
        goners += soup.findAll('table')
        for node in goners:
            node.extract()
        return soup

    def _remove_extra_parentheses(self, text):
        text = parentheses_pattern.sub('', parentheses_pattern.sub('', text))
        return text

    def _clean_punctuations(self, text):
        text = single_dash_pattern.sub('-', text)
        text = translation_pattern.sub('', text)
        text = long_dash_pattern.sub(' ', text)
        text = comma_pattern.sub(', ', text)
        text = dot_pattern.sub('. ', text)

        text = single_space_pattern.sub(' ', text)
        text = text.strip().strip('\n').strip('\t')
        return text

    def _cleanup(self, text):
        text = self._remove_extra_parentheses(text)
        text = self._clean_punctuations(text)
        return text

    def _validate_query(self, text):
        if defaults.WIKIWARE_QUERY_NOT_FOUND_TEXT in text:
            return ''
        else:
            return text

    def get_summary(self, force=False):
        if hasattr(self, 'summary') and self.summary and not force:
            return self.summary
        self.summary = ''
        soup = self._purge_redundant_nodes(self.soup)
        paragraphs = paragraph_pattern.findall(str(soup.body))
        for p in paragraphs:
            self.summary += BeautifulSoup(p).get_text()
        self.summary = self._cleanup(self.summary)
        self.summary = self._validate_query(self.summary)
        return self.summary




