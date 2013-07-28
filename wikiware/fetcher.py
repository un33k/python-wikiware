import sys
import requests
import logging
import urllib
import defaults

if defaults.DEBUG:
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

    def fetch_api_query_method(self, title):
        """ dump Wikipedia article via query title """

        self.url = defaults.WIKIWARE_API_URL
        self.params = {
            'titles': urllib.unquote_plus(title),
            'format': 'json',
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'redirects': '1',
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

    def fetch_api_parse(self, title, section=None, redirect=1):
        """ dump Wikipedia article via parse page """

        self.url = defaults.WIKIWARE_API_URL
        self.params = {
            'page': urllib.unquote_plus(title),
            'format': 'json',
            'action': 'parse',
            'prop': 'text',
            'redirects': redirect,
        }
        if not section is None:
            self.params.update({"section": section,})

        r = requests.get(self.url, params=self.params, headers=self.headers)
        if r.status_code != requests.codes.ok:
            logger.error('Fetch Failed: Title={0}, Status={1}'.format(title, r.status_code))
            return ''

        text = r.json()
        try:
            text = text['parse']['text']['*']
        except:
            logger.error('No text returned: Title={0}, Status={1}'.format(title, r.status_code))
            return ''
        return text

    def fetch_en_printable_method(self, title, printable=True):
        """ dump Wikipedia article in HTML """

        self.url = defaults.WIKIWARE_EN_URL
        self.params = {
            'title': urllib.unquote_plus(title),
            'printable': 'yes' if printable else 'no',
        }
        r = requests.get(self.url, params=self.params, headers=self.headers)
        return r.text







