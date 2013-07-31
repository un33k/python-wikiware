# -*- coding: utf-8 -*-

import re
import HTMLParser
from bs4 import BeautifulSoup

from patterns import *
from utils import *

import defaults

class WikiwareAPIParseBase(object):
    """ Parse Wikipedia API Parse Base """

    def __init__(self, known_phrase=defaults.WIKIWARE_QUERY_NOT_FOUND_PHRASE):
        self.phrases = known_phrase

    def _set_content(self, content):
        """ Set the content to be parsed """

        self.html = HTMLParser.HTMLParser().unescape(content)
        self.soup = BeautifulSoup(self.html)

    def set_not_found_phrases(self, phrase_list):
        """ Set a list of phrase that indicate a not found page """

        self.phrases = phrase_list

    def _clean_punctuations(self, text):
        """ Clean up punctuations """

        text = pattern_single_dash.sub('-', text)
        text = pattern_translation.sub('', text)
        text = pattern_long_dash.sub(' ', text)
        text = pattern_comma.sub(', ', text)
        text = pattern_dot.sub('. ', text)
        text = pattern_semicolon.sub('; ', text)

        text = pattern_single_space.sub(' ', text)
        return text

    def _remove_duplicates(self, text):
        """ Remove duplicate characters """

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
        """ Remove extra leftover characters """

        text = pattern_parentheses.sub('', pattern_parentheses.sub('', text))
        replace = ['(', ')', '{', '}', '[', ']',]
        for r in replace:
            text = text.replace(r, ' ')
        return text
    
    def _cleanup(self, text):
        """ Clean up text """
        text = self._remove_extras(text)
        text = self._clean_punctuations(text)
        text = self._strip_extras(text)
        text = self._remove_duplicates(text)
        return text

    def _validate_query(self, text):
        """ Validate if query was found by ensuring the absence of known phrases """

        for phrase in self.phrases:
            if phrase in text:
                return None
        else:
            return text


class WikiwareAPIParseSummary(WikiwareAPIParseBase):
    """ Parse Wikipedia contents for the Summary section """

    def _is_summary_tag(self, tag):
        """ Summary tag is a <p> some text </p> pattern """

        return tag.name == 'p' and not tag.has_attr('class') and not tag.has_attr('id')

    def _purge_non_summary_nodes(self, soup):
        """ Remove any non-summary html node from the dom tree """

        goners = soup.find_all(id=pattern_coordinates)
        goners += soup.find_all(id=pattern_cite_reference)
        goners += soup.find_all(attrs={'class': pattern_error})
        goners += soup.find_all('table')
        for node in goners:
            node.extract()
        return soup

    def _get_summary_paragraphs(self, soup):
        """ Returns the text for all the summary pharagraphs """

        summary_paragraphs = []
        soup = self._purge_non_summary_nodes(soup)
        paragraphs = soup.find_all(self._is_summary_tag)
        for p in paragraphs:
            summary_paragraphs.append(self._cleanup(p.get_text()))
        return summary_paragraphs

    def get_summary(self, content):
        """ Returns the summary for the given wikipedia content """

        self._set_content(content)
        paragraphs = self._get_summary_paragraphs(self.soup)
        summary = self._validate_query("\n".join(paragraphs))
        return summary




