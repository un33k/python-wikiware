from fetcher import WikiwareFetch
from parser import WikiwareParse

if __name__ == '__main__':
    title = 'France'
    format = 'txt'
    fetcher = WikiwareFetch(title=title, fmt=format)
    content = fetcher.fetch()
    parser = WikiwareParse(content=content, format=format)
    parser.parse()


