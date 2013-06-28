import re

def clean_wiki_markup(text):
    """ Remove wiki markup from the text. (http://pastebin.com/idw8vQQK) """

    txt = re.sub(r'(?i)\{\{IPA(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), text)
    txt = re.sub(r'(?i)\{\{Lang(\-[^\|\{\}]+)*?\|([^\|\{\}]+)(\|[^\{\}]+)*?\}\}', lambda m: m.group(2), txt)
    txt = re.sub(r'\{\{[^\{\}]+\}\}', '', txt)
    txt = re.sub(r'(?m)\{\{[^\{\}]+\}\}', '', txt)
    txt = re.sub(r'(?m)\{\|[^\{\}]*?\|\}', '', txt)
    txt = re.sub(r'(?i)\[\[Category:[^\[\]]*?\]\]', '', txt)
    txt = re.sub(r'(?i)\[\[Image:[^\[\]]*?\]\]', '', txt)
    txt = re.sub(r'(?i)\[\[File:[^\[\]]*?\]\]', '', txt)
    txt = re.sub(r'\[\[[^\[\]]*?\|([^\[\]]*?)\]\]', lambda m: m.group(1), txt)
    txt = re.sub(r'\[\[([^\[\]]+?)\]\]', lambda m: m.group(1), txt)
    txt = re.sub(r'\[\[([^\[\]]+?)\]\]', '', txt)
    txt = re.sub(r'(?i)File:[^\[\]]*?', '', txt)
    txt = re.sub(r'\[[^\[\]]*? ([^\[\]]*?)\]', lambda m: m.group(1), txt)
    txt = re.sub(r"''+", '', txt)
    txt = re.sub(r'(?m)^\*$', '', txt)
 
    return txt