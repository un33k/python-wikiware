# -*- coding: utf-8 -*-

import re

# match "( and (anything) here )" inclusive
parentheses_pattern = re.compile("(?mis)\([^()]*\)")

# match "[[ anything |" inclusive
right_angled_brackets_pattern = re.compile("(?mis)\[\[[^\]]*?\|")

# match "<ref anything />" or "<ref> anything </ref>" inclusive
ref_pattern = re.compile("(?mis)<\s*ref[^>]*?\/>|<\s*ref[^>*]*>.*?</ref>")

# match html comments "<!-- anything -->" inclusive or <!--- anything --->
html_comment_pattern = re.compile("(?mis)\<!-{1,}[^\<]*-{1,}\>") 

# match "{{ anything }}" inclusive
double_curly_brackets_content_pattern = re.compile("(?mis)\{\{.*?[^\}\}]\}\}")

# match "{{"
double_curly_brackets_right_pattern = re.compile("(?mis)\{\{|\}\}")

# match "}}
double_curly_brackets_left_pattern = re.compile("(?mis)\}\}")

# match "{{" or "}}"
double_curly_brackets_pattern = re.compile("(?mis)\{\{|\}\}")

# match any "[[" or "]]"
double_angled_brackets_pattern = re.compile("(?mis)\[\[|\]\]")

# match space before comma " ," or "       ,"
comma_pattern = re.compile("(?mis) {1,}\,")

# match space before dot " ." or "       ."
dot_pattern = re.compile("(?mis) {1,}\.")

# match space before ; " ;" or "       ;"
semicolon_pattern = re.compile("(?mis) {1,}\;")

# match the start of the infobox
infobox_start_pattern = re.compile("(?mis)\{\{\s*infobox", re.I)

# match the end of infobox
infobox_end_pattern = re.compile("(?mis)\}\}\s*'''")

# match start of summary
summary_start_pattern = infobox_end_pattern
summary_start_pattern_with_the = re.compile("(?mis)\}\}[\\n]+The\s*\'\'\'")

# match end of summary
summary_end_pattern = re.compile("(?mis)==\s*(.*?)\s*==")

# match language translation
language_translation_pattern = re.compile("(?mis)\{\{\s*lang\s*\|\s*.+?\s*\|\s*(.+?)\s*\}\}")

# match (IPA) International Phonetic Alphabet
ipa_pattern = re.compile("(?mis)\{\{IPA.*?\}\}")

# match refn "{{refn| anything }}"
reference_number_pattern = re.compile("(?mis)\{\{\s*refn.*?\}\}")

# match double single qoute " '' "
double_single_qoute_pattern = re.compile("(?mis)\'\'")

# match convert template
convert_pattern = re.compile("(?mis)\{\{\s*convert\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|.*?\}\}", re.I)

# match cite notes <sup> anything </sup>
cite_note_pattern = re.compile("(?mis)\<\s*sup.*?>.*?</\s*sup\s*\>")

# match long dash " – "
long_dash_pattern = re.compile("(?mis)\–")

# match date template
date_template_pattern = re.compile("(?mis)\{\{[^\{\{]*\|(\d{4})\|(\d{2})\|(\d{2})\s*\}\}")

# match the power of two
power_of_two_pattern = re.compile("(?mis)<\s*sup\s*>\s*(2)\s*<\s*/\s*sup\s*>")

# match paragraphs
paragraph_pattern = re.compile("(?mis)<\s*p\s*>(.*?)<\s*/\s*p\s*>")

# match cite_refs
cite_reference_pattern = re.compile("(?mis)cite_ref.*")

# match coordinates
coordinates_pattern = re.compile("(?mis)coordinates")

# match infobox
infobox_pattern = re.compile("(?mis)infobox")

# match errors
error_pattern = re.compile("(?mis)error")

# match one or more space
single_space_pattern = re.compile('(?mis)\s+|\t+')

# match one or more dash
single_dash_pattern = re.compile('(?mis)-+')

# match one or more ;
single_semicolon_pattern = re.compile('(?mis);+')

# match translation; i/ˈkænədə/
translation_pattern = re.compile("(?mis)i/.*?/|/.*?/")




