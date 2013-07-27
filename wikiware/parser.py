# -*- coding: utf-8 -*-

import re
import HTMLParser
import bleach

from pydry.string import str_serialize_clean, str_single_space, str_single_next_line
from pydry.string import str_find_between_regex, str_find_between_tags

import defaults
from patterns import *
from utils import clean_markup_wiki

class WikiwareParseBase(object):
    """ Parse Wikipedia base"""

    def clean_doubled_angled_brackets(self, text):
        txt = right_angled_brackets_pattern.sub('', text)
        txt = double_angled_brackets_pattern.sub('', txt)
        return txt

    def clean_curly_brackets(self, text):
        txt = double_curly_brackets_content_pattern.sub('', text)
        txt = double_curly_brackets_pattern.sub('', txt)
        return txt

    def clean(self, text):
        text = text.replace("'''", '')
        text = long_dash_pattern.sub(' ', text)
        text = comma_pattern.sub(', ', text)
        text = dot_pattern.sub('. ', text)
        text = double_single_qoute_pattern.sub('"', text)
        text = str_single_space(text)
        text = str_single_next_line(text)
        return text.strip()

class WikiwareAPIParse(WikiwareParseBase):
    """ Parse Wikipedia contents from API Calls"""

    def __init__(self, content, format='txt'):
        self.content = content
        self.format = format

    def get_summary_block(self, text):
        start, end = 'summary_starts_here ', 'summary_ends_here '
        text = summary_start_pattern.sub(start, text)
        if start not in text:
            text = summary_start_pattern_with_the.sub(start+" The ", text)
        text = summary_end_pattern.sub(end, text)
        text = str_find_between_regex(text, start=start,  end=end, case=False)
        if not text:
            text = summary_start_pattern_with_the.sub(start, text)
            text = str_find_between_regex(text, start=start,  end=end, case=False)
        return text

    def get_summary(self, text):
        """ order is important """

        text = clean_markup_wiki(text)
        text = self.get_summary_block(text)
        text = self.clean_doubled_angled_brackets(text)
        text = self.clean_curly_brackets(text)
        text = self.clean(text)
        return text

    def get_infobox(self, text):
        start, end = 'infobox_start', 'infobox_end'
        txt = infobox_start_pattern.sub(start, text)
        txt = infobox_end_pattern.sub(end, txt)
        txt = str_find_between_regex(txt, start=start,  end=end, case=False)
        return txt

    def parse(self):
        """ parser content """

        # print self.get_infobox(self.content)
        txt = self.get_summary(self.content)
        return txt



