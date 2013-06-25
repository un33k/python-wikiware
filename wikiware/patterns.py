import re

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
    # Remove html comment <!-- comments -->
    "\<!--"         # Match <!--
    ".*?"           # Lazy Match any char
    "--\>"          # Match -->
)

remove_curly_brackets_pattern = re.compile(
    # Remove {{ something }} patterns
    "\{\{"          # Match {{
    ".*?"           # Lazy Match any char
    "[^\}\}]"       # Match anything but }
    "\}\}"          # Match }}
)

remove_double_angled_brackets_pattern = re.compile(
    # Remove [[ or ]]
    "\[\["          # Match [[
    "|"             # OR
    "\]\]"          # ]]
)

