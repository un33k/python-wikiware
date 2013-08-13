# -*- coding: utf-8 -*-

import re
import HTMLParser
from bs4 import BeautifulSoup

from patterns import *
from utils import *

import defaults

class WikiwareAPIParseBase(object):
    """ Parse Wikipedia API Parse Base """

    def __init__(self, content=None):
        self.phrases = defaults.WIKIWARE_QUERY_NOT_FOUND_PHRASE
        if content is not None:
            self.set_content(content)

        self.attrs = [{'class': pattern_error}, {'id': pattern_cite_reference}]

    def set_content(self, content):
        """ Set the content to be parsed """

        self.html = HTMLParser.HTMLParser().unescape(content)
        self.soup = BeautifulSoup(self.html)

    def set_attr(self, attr):
        """ Set the attr of to be removed tags """

        self.attrs.append(attr)

    def set_not_found_phrases(self, phrase_list):
        """ Set a list of phrase that indicate a not found page """

        self.phrases = phrase_list

    def clean_punctuations(self, text):
        """ Clean up punctuations """

        text = pattern_single_dash.sub('-', text)
        text = pattern_translation.sub('', text)
        text = pattern_long_dash.sub(' ', text)
        text = pattern_comma.sub(', ', text)
        text = pattern_dot.sub('. ', text)
        text = pattern_semicolon.sub('; ', text)

        text = pattern_single_space.sub(' ', text)
        return text

    def remove_duplicates(self, text):
        """ Remove duplicate characters """

        dups = ['\t', '\n', '\r', ' ', '-', ':', ';', '_', '-', ',',]
        for d in dups:
            text = re.sub('(?mis)%s{1,}' % d, d, text)
        return text

    def strip_extras(self, text):

        strip = ['\t', '\n', '\r\n', '\r', ' ',]
        for s in strip:
            text = text.strip(s)
        return text

    def remove_extras(self, text):
        """ Remove extra leftover characters """

        text = pattern_parentheses.sub('', pattern_parentheses.sub('', text))
        replace = ['(', ')', '{', '}', '[', ']',]
        for r in replace:
            text = text.replace(r, ' ')
        return text

    def cleanup(self, text):
        """ Clean up text """

        text = self.remove_extras(text)
        text = self.clean_punctuations(text)
        text = self.strip_extras(text)
        text = self.remove_duplicates(text)
        return text

    def validate_query(self, text):
        """ Validate if query was found by ensuring the absence of known phrases """

        for phrase in self.phrases:
            if phrase in text:
                return None
        else:
            return text

    def purge_undesired_nodes(self, soup, attrs):
        """ Remove any undesired html node from the nodes """

        undesired = soup.find_all(attrs=attrs)
        for node in undesired:
            node.extract()
        return soup

    def is_it(self, node, kind):
        """ Returns True if node is a right `kind` """

        return getattr(node, 'name', '').lower() == kind.lower()

    def class_contains(self, node, text):
        """ Returns True if node has class that contains text """

        classes = node.get('class', [])
        for c in classes:
            if text.lower() in c.lower():
                return True
        return False

    def is_table_of_content(self, node):
        """ Returns True if node is the table of content <div class='toc'>...</div> """

        return self.is_it(node, 'div') and self.class_contains(node, 'toc')

    def is_infobox_table(self, node):
        """ Returns True if node is the infobox """

        return self.is_it(node, 'table') and self.class_contains(node, 'infobox')

    def is_category(self, category):
        infobox = self.soup.find('table', attrs={'class': pattern_infobox})
        if infobox is not None and self.class_contains(infobox, category):
            return True
        return False

    class Meta:
        abstract = True

class WikiwareAPIParseSummary(WikiwareAPIParseBase):
    """ Parse Wikipedia contents for the Summary section """

    def is_summary_tag(self, node):
        """ Summary tag is a <p> some text </p> pattern """

        return self.is_it(node, 'p') and not (node.has_attr('class') or node.has_attr('id'))

    def get_summary_paragraphs(self, soup):
        """ Return summary paragraphs of an article """

        summary_paragraphs = []
        nextNode = soup.find('table', attrs={'class': pattern_infobox})
        while nextNode:
            nextNode = nextNode.findNextSibling()
            if not nextNode or self.is_table_of_content(nextNode):
                break
            elif self.is_summary_tag(nextNode):
                for attr in self.attrs:
                    nextNode = self.purge_undesired_nodes(nextNode, attr)
                p_cleaned = self.cleanup(nextNode.get_text())
                if p_cleaned and len(p_cleaned) >= defaults.WIKIWARE_PARAGRAPH_MIN_CHARACTERS:
                    summary_paragraphs.append(p_cleaned)
        return summary_paragraphs

    def get_summary(self):
        """ Returns the summary for the given wikipedia content """

        summary = None
        paragraphs = self.get_summary_paragraphs(self.soup)
        if paragraphs:
            summary = self.validate_query("\n".join(paragraphs))
        return summary




