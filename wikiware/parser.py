import re
import HTMLParser

from pydry.string import str_serialize_clean
from pydry.string import str_find_between_regex

import defaults
from patterns import *

class WikiwareParse(object):
    """ Parse Wikipedia contents """

    def __init__(self, content, format='txt'):
        self.content = content
        self.format = format

    def serialize(self, text):
        txt = str_serialize_clean(text)
        return txt

    def unescape(self, text):
        txt = HTMLParser.HTMLParser().unescape(text)
        return txt

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
        txt = double_curly_brackets_pattern.sub('', text)
        return txt

    def clean_html_comments(self, text):
        txt = html_comment_pattern.sub('', text)
        return txt

    def clean_language_brackets(self, text):
        txt = language_translation_pattern.sub('', text)
        return txt

    def clean(self, text):
        txt = text.replace("'''", '')
        txt = comma_pattern.sub(', ', txt)
        txt = dot_pattern.sub('. ', txt)
        txt = self.clean_html_comments(txt)
        txt = self.serialize(txt)
        return txt

    def get_summary_block(self, text):
        start, end = 'summary_start', 'summary_end'
        txt = summary_start_pattern.sub(start, text)
        txt = summary_end_pattern.sub(end, txt)
        txt = str_find_between_regex(txt, start=start,  end=end, case=False)
        return txt

    def get_summary(self, text):
        """ order is important """

        txt = self.get_summary_block(text)
        txt = self.unescape(txt)
        txt = self.serialize(txt)
        txt = self.clean_parentheses(txt)
        txt = self.clean_ref_tags(txt)
        txt = self.clean_doubled_angled_brackets(txt)
        txt = self.clean_language_brackets(txt)
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
        print self.get_summary(self.content)







