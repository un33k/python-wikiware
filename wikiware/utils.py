import re
import HTMLParser

from patterns import *

# def clean_wiki_markup(text):
#     """ Remove wiki markup from the text. (http://pastebin.com/idw8vQQK) """
# 
#     txt = re.sub(r'(?i)\{\{IPA(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), text)
#     txt = re.sub(r'(?i)\{\{Lang(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), txt)
#     txt = re.sub(r'\{\{[^\{\}]+\}\}', '', txt)
#     txt = re.sub(r'(?m)\{\{[^\{\}]+\}\}', '', txt)
#     txt = re.sub(r'(?m)\{\|[^\{\}]*?\|\}', '', txt)
#     txt = re.sub(r'(?i)\[\[Category:[^\[\]]*?\]\]', '', txt)
#     txt = re.sub(r'(?i)\[\[Image:[^\[\]]*?\]\]', '', txt)
#     txt = re.sub(r'(?i)\[\[File:[^\[\]]*?\]\]', '', txt)
#     txt = re.sub(r'\[\[[^\[\]]*?\|([^\[\]]*?)\]\]', lambda m: m.group(1), txt)
#     txt = re.sub(r'\[\[([^\[\]]+?)\]\]', lambda m: m.group(1), txt)
#     txt = re.sub(r'\[\[([^\[\]]+?)\]\]', '', txt)
#     txt = re.sub(r'(?i)File:[^\[\]]*?', '', txt)
#     txt = re.sub(r'\[[^\[\]]*? ([^\[\]]*?)\]', lambda m: m.group(1), txt)
#     txt = re.sub(r"''+", '', txt)
#     txt = re.sub(r'(?m)^\*$', '', txt)
#  
#     return txt

def prepare_markup_wiki(text):
    text = HTMLParser.HTMLParser().unescape(text)
    text = html_comment_pattern.sub('', text)
    return text

def clean_markup_wiki(text):
    text = prepare_markup_wiki(text)
    text = language_translation_pattern.sub('\\1', text)
    text = convert_pattern.sub("\\1 \\2", text)
    text = date_template_pattern.sub('', text)
    text = reference_number_pattern.sub('', text)
    text = ref_pattern.sub('', text)
    text = ipa_pattern.sub('', text)
    text = parentheses_pattern.sub('', text)

    return text

def clean(self, text):
    txt = text.replace("'''", '')
    txt = long_dash_pattern.sub(' ', txt)
    txt = comma_pattern.sub(', ', txt)
    txt = dot_pattern.sub('. ', txt)
    txt = double_single_qoute_pattern.sub('"', txt)
    return txt

def clean_html(self, text):
    txt = re.sub(r'(?i)&nbsp;', ' ', text)
    txt = re.sub(r'(?i)<br[ \\]*?>', '\n', txt)
    txt = re.sub(r'(?m)<!--.*?--\s*>', '', txt)
    txt = re.sub(r'(?i)<ref[^>]*>[^>]*<\/ ?ref>', '', txt)
    txt = re.sub(r'(?m)<.*?>', '', txt)
    txt = re.sub(r'(?i)&amp;', '&', txt)
    return txt




