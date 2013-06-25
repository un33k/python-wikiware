from fetcher import WikiwareFetch
from parser import WikiwareParse

if __name__ == '__main__':
    title = 'Ottawa'
    format = 'txt'
    fetcher = WikiwareFetch(title=title, fmt=format)
    content = fetcher.fetch()
    parser = WikiwareParse()
    parser.parse(content, fmt=format)


