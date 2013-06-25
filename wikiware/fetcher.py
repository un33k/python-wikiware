import sys
import requests

import defaults

class WikiwareFetch(object):
    """ Fetch content from Wikipedia """

    def __init__(self, title, fmt="txt"):
        """ Mediawiki API query """

        self.url = defaults.WIKIWARE_API_URL
        self.params = {
            'titles': title,
            'format': fmt,
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'redirects': '',
        }
        self.user_agent = {
            'User-agent': 'python-request-{}'.format(sys.version.split()[0]),
        }

        self.headers = self.user_agent

    def fetch(self):
        """ dump Wikipedia article """

        r = requests.get(self.url, params=self.params, headers=self.headers)
        return r.text








