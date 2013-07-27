from fetcher import WikiwareFetch
from parser import WikiwareAPIParse

if __name__ == '__main__':
    # title = 'The Democratic Republic of Congo'
    # title = 'The United States'
    # title = 'Hong Kong'
    # title = 'The United Kingdom'
    title = 'Antarctica'
    format = 'json'
    fetcher = WikiwareFetch()
    content = fetcher.fetch_api(title=title, format=format)
    parser = WikiwareAPIParse(content=content, format=format)
    text = parser.parse()

    print "\n\n"
    print text
    print "\n\n"
