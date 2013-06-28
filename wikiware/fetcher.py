import sys
import requests

import defaults

class WikiwareFetch(object):
    """ Fetch content from Wikipedia """

    def __init__(self):
        """ Mediawiki API query """

        self.user_agent = {
            'User-agent': 'python-request-{}'.format(sys.version.split()[0]),
        }

        self.headers = self.user_agent

    def fetch_api(self, title, format="txt"):
        """ dump Wikipedia article """

        self.url = defaults.WIKIWARE_API_URL
        self.params = {
            'titles': title,
            'format': format,
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'redirects': '',
        }

        r = requests.get(self.url, params=self.params, headers=self.headers)
        return r.text

    def fetch_en(self, title, printable=True):
        """ dump Wikipedia article in HTML """

        self.url = defaults.WIKIWARE_EN_URL
        self.params = {
            'title': title,
            'printable': 'yes' if printable else 'no',
        }
        r = requests.get(self.url, params=self.params, headers=self.headers)
        return r.text







