import re

# match "( and (anything) here )" inclusive
parentheses_pattern = re.compile("\(([^()])+\)")

# match "[[ anything |" inclusive
right_angled_brackets_pattern = re.compile("\[\[[^\]]*?\|")

# match "<ref anything />" or "<ref> anything </ref>" inclusive
ref_pattern = re.compile("<\s*ref[^>]*?\/>|<\s*ref[^>*]*>.*?</ref>")

# match html comments "<!-- anything -->" inclusive
html_comment_pattern = re.compile("\<!--.*?--\>") 

# match "{{ anything }}" inclusive
double_curly_brackets_content_pattern = re.compile("\{\{.*?[^\}\}]\}\}")

# match "{{"
double_curly_brackets_right_pattern = re.compile("\{\{|\}\}")

# match "}}
double_curly_brackets_left_pattern = re.compile("\}\}")

# match "{{" or "}}"
double_curly_brackets_pattern = re.compile("\{\{|\}\}")

# match any "[[" or "]]"
double_angled_brackets_pattern = re.compile("\[\[|\]\]")

# match space before comma " ," or "       ,"
comma_pattern = re.compile(" {1,}\,")

# match space before dot " ." or "       ."
dot_pattern = re.compile(" {1,}\.")

# match the start of the infobox
infobox_start_pattern = re.compile("\{\{\s*infobox", re.I)

# match the end of infobox
infobox_end_pattern = re.compile("\}\}\s*'''")

# match start of summary
summary_start_pattern = infobox_end_pattern

# match end of summary
summary_end_pattern = re.compile("==\s*(.*?)\s*==")

# match language translation
language_translation_pattern = re.compile("\{\{\s*lang\s*\|\s*.+?\s*\|\s*(.+?)\s*\}\}")

# match refn "{{refn| anything }}"
reference_number_pattern = re.compile("\{\{\s*refn.*?\}\}")

# match double single qoute " '' "
double_single_qoute_pattern = re.compile("\'\'")

# match convert template
convert_pattern = re.compile("\{\{\s*convert\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|.*?\}\}", re.I)



