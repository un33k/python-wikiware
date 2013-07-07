from fetcher import WikiwareFetch
from parser import WikiwareAPIParse

if __name__ == '__main__':
    title = 'France'
    format = 'json'
    fetcher = WikiwareFetch()
    content = fetcher.fetch_api(title=title, format=format)
    parser = WikiwareAPIParse(content=content, format=format)
    text = parser.parse()

    print "\n\n"
    print text
    print "\n\n"
