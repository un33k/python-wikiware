import sys
import requests
import logging

import defaults

logging.basicConfig(filename='wikiware.log',level=logging.DEBUG)

logger = logging.getLogger('wikiware-fetcher')

class WikiwareFetch(object):
    """ Fetch content from Wikipedia """

    def __init__(self):
        """ Mediawiki API query """

        self.user_agent = {
            'User-agent': 'python-request-{}'.format(sys.version.split()[0]),
        }

        self.headers = self.user_agent

    def fetch_api(self, title, format="json"):
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
        if r.status_code != requests.codes.ok:
            logger.error('Fetch Failed: Title={0}, Status={1}'.format(title, r.status_code))
            return ''

        text = r.json()
        try:
            pages = text['query']['pages']
        except:
            logger.error('No pages returned: Title={0}, Status={1}'.format(title, r.status_code))
            return ''
        revision = ''
        for page in pages:
            try:
                revision = pages[page]['revisions'][0]['*']
            except:
                pass
            break

        if not revision:
            logger.error('No revisions found: Title={0}, Status={1}'.format(title, r.status_code))
        return revision

    def fetch_en(self, title, printable=True):
        """ dump Wikipedia article in HTML """

        self.url = defaults.WIKIWARE_EN_URL
        self.params = {
            'title': title,
            'printable': 'yes' if printable else 'no',
        }
        r = requests.get(self.url, params=self.params, headers=self.headers)
        return r.text







