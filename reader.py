""" RSS feed reader """
import sys
import click
import feedparser as fp
from content import terminal

def parse(feed):
    """ Parse the rss feed """
    rss = fp.parse(feed)
    return (rss, rss.feed.title, rss.feed.subtitle)

def entries(feed):
    """ Generator that yields title, summary and link of the entry """
    for entry in feed.entries:
        details = []
        for item in ['title', 'summary', 'link']:
            details.append(entry.get(item, ''))
        yield details

def read_feed(url, viewer=click.launch):
    """ Read each article one by one """
    feed, title, desc = parse(url)

    for title, description, link in entries(feed):
        wanto_read = input(f'Want to read {title}? [y/n]: ')
        if wanto_read in ['y', 'Y']:
            print('\n' + '-' * 50)
            print(f'\nEnjoy {title}...')
            print('\n' + '-' * 50)
            viewer(link)
            click.pause(info='Press any key to continue ...')
        elif wanto_read == 'q':
            return
            print('You must be tired! Enjoy your break! And come back soon for more!')
            sys.exit(0)
    else:
        print(f'{title = } \n{description = } \n{link = }\n')

@click.command()
@click.option('--url', help='Feed url')
@click.option('--feeds', help='File containing rss feed urls.')
@click.option('--reader', default='terminal', help='Set the reader. web/terminal')
def main(url, feeds, reader):
    """ Parse single or multiple rss feeds """
    urls = []

    if url:
        urls = [url]
    elif feeds:
        urls = [url for url in open(feeds)]
    else:
        print(main.get_help(click.Context(main)))

    reader = click.launch if reader == 'web' else terminal

    for url in urls:
        print('\n' + '-' * 50)
        print(f'\nBrowsing {url}')
        read_feed(url, reader)

if __name__ == '__main__':
    main()
    # TODO: implement Terminal reader
