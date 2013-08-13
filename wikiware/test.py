
import defaults
defaults.DEBUG = True
from geo import *

if __name__ == '__main__':
    titles = [
        'The Democratic Republic of Congo',
        'The United States',
        'Hong Kong',
        'The United Kingdom',
        'Antarctica',
        'Germany',
        'Ghana',
        'Iran',
        'Jamaica',
        'Canada',
        'Botswana',
        'Netherlands',
        'Jersey',
        'Georgia_%28country%29',
        'United State',
        'Nalbandyan,_Armenia',
        'Netherland',
    ]
    print "\n\n============"
    for title in titles:
        summary = get_wiki_summary(title)
        print "\n\n============"
        print summary
        print "============\n\n"
