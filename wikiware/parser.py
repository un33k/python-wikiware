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
        txt = curly_brackets_pattern.sub('', text)
        return txt

    def clean_html_comments(self, text):
        txt = html_comment_pattern.sub('', text)
        return txt

    def cleanup(self, text):
        txt = text.replace("'''", '')
        txt = comma_pattern.sub(', ', txt)
        txt = dot_pattern.sub('. ', txt)
        txt = self.clean_html_comments(txt)
        txt = self.serialize(txt)
        return txt

    def summary_raw(self, text):
        txt = str_find_between_regex(text, start="'''",  end="==")
        return txt

    def summary(self, text):
        """ order is important """

        txt = self.summary_raw(text)
        txt = self.unescape(txt)
        txt = self.serialize(txt)
        txt = self.clean_parentheses(txt)
        txt = self.clean_ref_tags(txt)
        txt = self.clean_doubled_angled_brackets(txt)
        txt = self.clean_curly_brackets(txt)
        txt = self.clean_curly_brackets(txt)
        txt = self.cleanup(txt)
        return txt

    def infobox_raw(self, text):
        infobox = str_find_between_regex(txt, start='{{Infobox',  end="'''", case=False)
        return infobox

    def parse(self):
        """ parser content """

        print self.summary(self.content)







