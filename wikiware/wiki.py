from fetcher import WikiwareFetch
from parser import WikiwareAPIParse, WikiwareEnParse

if __name__ == '__main__':
    title = 'France'
    format = 'txt'
    fetcher = WikiwareFetch()
    content = fetcher.fetch_api(title=title, format=format)
    parser = WikiwareAPIParse(content=content, format=format)
    parser.parse()

    print "\n\n"

    # fetch_en = WikiwareFetch()
    # content = fetcher.fetch_en(title=title)
    # parser = WikiwareEnParse(content=content)
    # parser.parse()

