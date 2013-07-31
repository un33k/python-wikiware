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

    def _purge_undesired_nodes(self, soup):
        """ Remove any undesired html node from the nodes """

        undesired = soup.find_all(id=pattern_cite_reference)
        undesired += soup.find_all(attrs={'class': pattern_error})
        for node in undesired:
            node.extract()
        return soup

    def _is(self, node, kind):
        """ Returns True if node is a right `kind` """

        return getattr(node, 'name', '').lower() == kind.lower()

    def _class_contains(self, node, text):
        """ Returns True if node has class that contains text """

        classes = node.get('class', [])
        for c in classes:
            if text.lower() in c.lower():
                return True
        return False

    def _is_table_of_content(self, node):
        """ Returns True if node is the table of content <div class='toc'>...</div> """

        return self._is(node, 'div') and self._class_contains(node, 'toc')

    def _is_infobox_table(self, node):
        """ Returns True if node is the infobox """

        return self._is(node, 'table') and self._class_contains(node, 'infobox')


class WikiwareAPIParseSummary(WikiwareAPIParseBase):
    """ Parse Wikipedia contents for the Summary section """

    def _is_summary_tag(self, node):
        """ Summary tag is a <p> some text </p> pattern """

        return self._is(node, 'p') and not (node.has_attr('class') or node.has_attr('id'))

    def _get_summary_paragraphs(self, soup):
        """ Return summary paragraphs of an article """

        summary_paragraphs = []
        nextNode = soup.find('table', attrs={'class': pattern_infobox})
        while nextNode:
            nextNode = nextNode.findNextSibling()
            if not nextNode or self._is_table_of_content(nextNode):
                break
            elif self._is_summary_tag(nextNode):
                nextNode = self._purge_undesired_nodes(nextNode)
                p_cleaned = self._cleanup(nextNode.get_text())
                if p_cleaned and len(p_cleaned) >= defaults.WIKIWARE_PARAGRAPH_MIN_CHARACTERS:
                    summary_paragraphs.append(p_cleaned)
        return summary_paragraphs

    def get_summary(self, content):
        """ Returns the summary for the given wikipedia content """

        summary = None
        self._set_content(content)
        paragraphs = self._get_summary_paragraphs(self.soup)
        if paragraphs:
            summary = self._validate_query("\n".join(paragraphs))
        return summary




