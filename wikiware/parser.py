# -*- coding: utf-8 -*-

import re
import HTMLParser
import bleach

from pydry.string import str_serialize_clean
from pydry.string import str_find_between_regex, str_find_between_tags

import defaults
from patterns import *
from utils import clean_wiki_markup

class WikiwareParseBase(object):
    """ Parse Wikipedia base"""

    def serialize(self, text):
        txt = str_serialize_clean(text)
        return txt

    def unescape(self, text):
        txt = HTMLParser.HTMLParser().unescape(text)
        return txt

    def clean(self, text):
        txt = text.replace("'''", '')
        txt = long_dash_pattern.sub(' ', txt)
        txt = comma_pattern.sub(', ', txt)
        txt = dot_pattern.sub('. ', txt)
        txt = double_single_qoute_pattern.sub('"', txt)
        txt = self.serialize(txt)
        txt = self.clean_html(txt)
        return txt

    def clean_html(self, text):
        txt = re.sub(r'(?i)&nbsp;', ' ', text)
        txt = re.sub(r'(?i)<br[ \\]*?>', '\n', txt)
        txt = re.sub(r'(?m)<!--.*?--\s*>', '', txt)
        txt = re.sub(r'(?i)<ref[^>]*>[^>]*<\/ ?ref>', '', txt)
        txt = re.sub(r'(?m)<.*?>', '', txt)
        txt = re.sub(r'(?i)&amp;', '&', txt)
        return txt
        
class WikiwareAPIParse(WikiwareParseBase):
    """ Parse Wikipedia contents from API Calls"""

    def __init__(self, content, format='txt'):
        self.content = content
        self.format = format

    def clean_parentheses(self, text):
        txt = parentheses_pattern.sub('', text)
        txt = parentheses_pattern.sub('', txt)
        return txt

    def clean_ref_tags(self, text):
        txt = ref_pattern.sub('', text)
        return txt

    def clean_doubled_angled_brackets(self, text):
        txt = right_angled_brackets_pattern.sub('', text)
        txt = double_angled_brackets_pattern.sub('', txt)
        return txt

    def clean_curly_brackets(self, text):
        txt = double_curly_brackets_content_pattern.sub('', text)
        txt = double_curly_brackets_pattern.sub('', txt)
        return txt

    def clean_language_brackets(self, text):
        txt = language_translation_pattern.sub('\\1', text)
        return txt

    def clean_reference_number(self, text):
        txt = reference_number_pattern.sub('', text)
        return txt

    def clean_dates(self, text):
        txt = date_template_pattern.sub(' ', text)
        return txt

    def clean_converts(self, text):
        txt = convert_pattern.sub("\\1 \\2", text)
        return txt

    def clean(self, text):
        txt = super(WikiwareAPIParse, self).clean(text)
        return txt

    def get_summary_block(self, text):
        txt = html_comment_pattern.sub('', text)
        start, end = 'summary_start', 'summary_end'
        txt = summary_start_pattern.sub(start, txt)
        txt = summary_end_pattern.sub(end, txt)
        txt = str_find_between_regex(txt, start=start,  end=end, case=False)
        return txt

    def get_summary(self, text):
        """ order is important """

        txt = self.get_summary_block(text)
        txt = self.unescape(txt)
        txt = self.serialize(txt)
        txt = self.clean_converts(txt)
        txt = self.clean_dates(txt)
        txt = self.clean_language_brackets(txt)
        txt = self.clean_parentheses(txt)
        txt = self.clean_ref_tags(txt)
        txt = self.clean_reference_number(txt)
        txt = self.clean_doubled_angled_brackets(txt)
        txt = self.clean_curly_brackets(txt)
        txt = self.clean(txt)
        return txt

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
        txt = clean_wiki_markup(txt)
        return txt

class WikiwareEnParse(WikiwareParseBase):
    """ Parse Wikipedia contents from EN site Calls """

    def __init__(self, content, printable='yes'):
        self.content = content
        self.printable = format

    def clean_tags(self, text):
        txt = bleach.clean(text, tags=[], strip=True)
        return txt

    def clean_cite_tags(self, text):
        txt = cite_note_pattern.sub('', text)
        return txt

    def clean(self, text):
        txt = super(WikiwareEnParse, self).clean(text)
        return txt

    def get_summary_block(self, text):
        txt = str_find_between_tags(text, start='="infobox',  end='="toc', case=False)
        txt = self.unescape(txt)
        txt = self.serialize(txt)
        txt = str_find_between_tags(text, start='<p><b>',  end='<table', case=False)
        return txt

    def get_summary(self, text):
        txt = self.get_summary_block(text)
        txt = self.clean_cite_tags(txt)
        txt = self.clean_tags(txt)
        return txt

    def parse(self):
        """ parser content """

        # print self.get_infobox(self.content)
        print self.get_summary(self.content)





