import re
import requests as rqst

from pydry.string import str_serialize_clean
from pydry.string import str_find_between_regex

import defaults

remove_parentheses_pattern = re.compile(
    # Remove anything between parentheses including parentheses, even nested parentheses
    "\("            # Match a ( char
    ".*?"           # Match any char one or more times, lazy = as few as possible
    "[^\(]"         # Match anything other than a ( char
    "."             # Match any char
    "\)"            # Match a ) char
)

remove_right_angled_brackets_pattern = re.compile(
    # Remove double angled brackets and | and anything in between. Before: [[ United States | USA ]] After: USA ]]
    "\[\["          # Match [[
    "[^\]]"         # Match anything other than a ( char
    "*?"            # Match any char one or more times, lazy = as few as possible
    "\|"            # Match a | char
)

remove_short_ref_pattern = re.compile(
    # Remove shorthand <ref / >. Before: <ref name=City /> After: 
    "<\s*ref"       # Match <ref or < ref
    "[^>]"          # Match anything but >
    "*?"            # Match Previous char one or more times
    "\/>"           # Match />
)

remove_long_ref_pattern = re.compile(
    # Remove long <ref></ref>. Before: <ref>some text</ref> After: 
    "<\s*ref"       # Match <ref or < ref
    "[^>*]"         # Match anything but >
    "*>"            # Match any char followed by >
    ".*?"           # Match Previous char one or more times
    "</ref>"        # Match />
)

remove_html_comment_pattern = re.compile(
    # Remote html comment <!-- comments -->
    "\<!--"         # Match <!--
    ".*?"           # Lazy Match any char
    "--\>"          # Match -->
)

remove_curly_brackets_pattern = re.compile(
    # Remote {{ something }}
    "\{\{"          # Match {{
    ".*?"           # Lazy Match any char
    "[^\}\}]"       # Match anything but }
    "\}\}"          # Match }}
)

class WikiwareParse(object):
    """ Parse Wikipedia contents """

    def parse(self, content, fmt='txt'):
        """ parser content """

        txt = str_serialize_clean(content)
        infobox = str_find_between_regex(txt, start='{{Infobox',  end="'''", case=False)

        summary = str_find_between_regex(txt, start="'''",  end="==")
        summary = summary.replace("'''", '')
        summary = remove_html_comment_pattern.sub('', summary)
        summary = remove_parentheses_pattern.sub('', summary)
        summary = remove_right_angled_brackets_pattern.sub('', summary)
        summary = summary.replace(']]', '').replace('[[', '')
        summary = remove_short_ref_pattern.sub('', summary)
        summary = remove_long_ref_pattern.sub('', summary)
        summary = remove_curly_brackets_pattern.sub('', summary)
        print summary







