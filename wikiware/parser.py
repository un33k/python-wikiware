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

    def cleanup(self, text):
        txt = text.replace("'''", '')
        txt = remove_html_comment_pattern.sub('', txt)
        txt = remove_parentheses_pattern.sub('', txt)
        txt = remove_right_angled_brackets_pattern.sub('', txt)
        txt = remove_double_angled_brackets_pattern.sub('', txt)
        txt = remove_short_ref_pattern.sub('', txt)
        txt = remove_long_ref_pattern.sub('', txt)
        txt = remove_curly_brackets_pattern.sub('', txt)
        txt = self.serialize(txt)
        return txt

    def summary_raw(self, text):
        txt = str_find_between_regex(text, start="'''",  end="==")
        return txt

    def summary(self, text):
        txt = self.summary_raw(text)
        txt = self.unescape(txt)
        txt = self.serialize(txt)
        return self.cleanup(txt)

    def infobox_raw(self, text):
        infobox = str_find_between_regex(txt, start='{{Infobox',  end="'''", case=False)
        return infobox

    def parse(self):
        """ parser content """

        print self.summary(self.content)







