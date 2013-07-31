import sys
import requests
import logging
import urllib
import defaults

log_level = logging.DEBUG if defaults.DEBUG else logging.ERROR
logging.basicConfig(filename='wikiware.log',level=log_level)
logger = logging.getLogger('wikiware-fetcher')

class WikiwareFetch(object):
    """ Fetch content from Wikipedia """

    def __init__(self, timeout=defaults.WIKIWARE_QUERY_CONNECTION_TIMEOUT_SECONDS):
        """ Mediawiki API query """

        self.user_agent = {
            'User-agent': 'python-request-{}'.format(sys.version.split()[0]),
        }

        self.headers = self.user_agent
        self.timeout = timeout

    def fetch_api_query_method(self, title):
        """ dump Wikipedia article via query title """

        content = None
        self.url = defaults.WIKIWARE_API_URL
        self.params = {
            'titles': urllib.unquote_plus(title),
            'format': 'json',
            'action': 'query',
            'prop': 'revisions',
            'rvprop': 'content',
            'redirects': '1',
        }

        r = self.make_get_request(self.url, params=self.params, headers=self.headers, timeout=self.timeout)
        if r and r.status_code != requests.codes.ok:
            logger.error('Fetch Failed: Title={0}, Status={1}'.format(title, r.status_code))
            return content

        text = r.json()
        try:
            pages = text['query']['pages']
        except:
            logger.error('No pages returned: Title={0}, Status={1}'.format(title, r.status_code))
            return content

        for page in pages:
            try:
                content = pages[page]['revisions'][0]['*']
            except:
                pass
            break

        if content is None:
            logger.error('No revisions found: Title={0}, Status={1}'.format(title, r.status_code))
        return content

    def fetch_api_parse(self, title, section=None, redirect=1):
        """ dump Wikipedia article via parse page """

        content = None
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

        r = self.make_get_request(self.url, params=self.params, headers=self.headers, timeout=self.timeout)
        if r and r.status_code != requests.codes.ok:
            logger.error('Fetch Failed: Title={0}, Status={1}'.format(title, r.status_code))
            return content

        text = r.json()
        try:
            content = text['parse']['text']['*']
        except:
            logger.error('No text returned: Title={0}, Status={1}'.format(title, r.status_code))
            return content
        return content

    def fetch_en_printable_method(self, title, printable=True):
        """ dump Wikipedia article in HTML """

        self.url = defaults.WIKIWARE_EN_URL
        self.params = {
            'title': urllib.unquote_plus(title),
            'printable': 'yes' if printable else 'no',
        }
        r = make_get_request(self.url, params=self.params, headers=self.headers, timeout=self.timeout)
        if r and r.text:
            return r.text
        return None


    def make_get_request(self, url, params, headers, timeout):
        """ Make the actual request """

        try:
            r = requests.get(self.url, params=self.params, headers=self.headers, timeout=timeout)
        except requests.exceptions.Timeout, e:
            logger.warning('Request Timeout: {}'.format(e))
            return None
        except requests.exceptions.ConnectionError, e:
            logger.error('Connection Error: {}'.format(e))
            raise
        return r







