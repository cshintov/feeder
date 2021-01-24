""" Get content """
import requests
from html2text import html2text as h2x

def get_content(url):
    res = requests.get(url)
    return res.content.decode(res.encoding)

def to_text(url):
    content = get_content(url)
    return h2x(content)

def terminal(url):
    print(to_text(url))


if __name__ == '__main__':
    print('Content: Main')
