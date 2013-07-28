# -*- coding: utf-8 -*-

import re

# match "( and (anything) here )" inclusive
pattern_parentheses = re.compile("(?mis)\([^()]*\)")

# match "[[ anything |" inclusive
pattern_right_angled_brackets = re.compile("(?mis)\[\[[^\]]*?\|")

# match html comments "<!-- anything -->" inclusive or <!--- anything --->
pattern_html_comment = re.compile("(?mis)\<!-{1,}[^\<]*-{1,}\>") 

# match "{{ anything }}" inclusive
pattern_double_curly_brackets_content = re.compile("(?mis)\{\{.*?[^\}\}]\}\}")

# match "{{"
pattern_double_curly_brackets_right = re.compile("(?mis)\{\{|\}\}")

# match "}}
pattern_double_curly_brackets_left = re.compile("(?mis)\}\}")

# match "{{" or "}}"
pattern_double_curly_brackets = re.compile("(?mis)\{\{|\}\}")

# match any "[[" or "]]"
pattern_double_angled_brackets = re.compile("(?mis)\[\[|\]\]")

# match space before comma " ," or "       ,"
pattern_comma = re.compile("(?mis) {1,}\,")

# match space before dot " ." or "       ."
pattern_dot = re.compile("(?mis) {1,}\.")

# match space before ; " ;" or "       ;"
pattern_semicolon = re.compile("(?mis) {1,}\;")

# match double single qoute " '' "
pattern_double_single_qoute = re.compile("(?mis)\'\'")

# match cite notes <sup> anything </sup>
pattern_cite_note = re.compile("(?mis)\<\s*sup.*?>.*?</\s*sup\s*\>")

# match long dash " – "
pattern_long_dash = re.compile("(?mis)\–")

# match the power of two
pattern_power_of_two = re.compile("(?mis)<\s*sup\s*>\s*(2)\s*<\s*/\s*sup\s*>")

# match paragraphs
pattern_paragraph = re.compile("(?mis)<\s*p\s*>(.*?)<\s*/\s*p\s*>")

# match cite_refs
pattern_cite_reference = re.compile("(?mis)cite_ref.*")

# match coordinates
pattern_coordinates = re.compile("(?mis)coordinates")

# match infobox
pattern_infobox = re.compile("(?mis)infobox")

# match errors
pattern_error = re.compile("(?mis)error")

# match one or more space
pattern_single_space = re.compile('(?mis)\s+|\t+')

# match one or more dash
pattern_single_dash = re.compile('(?mis)-+')

# match one or more ;
pattern_single_semicolon = re.compile('(?mis);+')

# match translation; i/ˈkænədə/
pattern_translation = re.compile("(?mis)i/.*?/|/.*?/")




