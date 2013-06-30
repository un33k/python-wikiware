from fetcher import WikiwareFetch
from parser import WikiwareAPIParse, WikiwareEnParse

if __name__ == '__main__':
    title = 'Hamadan'
    format = 'txt'
    fetcher = WikiwareFetch()
    content = fetcher.fetch_api(title=title, format=format)
    parser = WikiwareAPIParse(content=content, format=format)
    text = parser.parse()

    print "\n\n"
    print text
    print "\n\n"

    # fetch_en = WikiwareFetch()
    # content = fetcher.fetch_en(title=title)
    # parser = WikiwareEnParse(content=content)
    # parser.parse()

