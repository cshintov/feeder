""" RSS feed reader """
import feedparser as fp

def read(feed):
    rss = fp.parse(feed)
    return (rss, rss.feed.title, rss.feed.subtitle)

def entries(feed):
    """ Generator that yields title, summary and link of the entry """
    for entry in feed.entries:
        details = []
        for item in ['title', 'summary', 'link']:
            details.append(entry.get(item, ''))
        yield details

if __name__ == '__main__':
    devto = 'https://dev.to/feed/'
    devto_old = './data/devto.main.feed'
    pgessays = './data/pgessays.rss'

    feed, title, desc = read(devto_old)
    print(f'Count = {len(feed.entries)}')
    for title, description, link in entries(feed):
        print(f'{title = } \n{description = } \n{link = }\n')
