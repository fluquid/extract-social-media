"""Main part to extract social media links from websites."""
from __future__ import unicode_literals
import re

import six

__author__ = 'Johannes Ahlmann'
__email__ = 'johannes@fluquid.com'
__version__ = '0.4.0'


# FIXME: a lot wrong with the below
# - too permissive
# - likely too slow
PREFIX = r'https?://(?:www\.)?'
SITES = [
    '(?:[a-z]{2}-[a-z]{2}\.)?facebook.com/',
    '(?:[a-z]{2}\.)?linkedin.com/(?:company/|in/|pub/)',
    'fb.co',
    'feeds.feedburner.com',
    'flickr.com',
    'flipboard.com/',
    'github.com/',
    'google.com/+',
    'instagram.com/',
    'periscope.tv/',
    'pinterest.com/',
    'plus\.google.com/',
    'slideshare.net',
    'snapchat.com/',
    'soundcloud.com',
    'telegram.me/',
    'twitter.com/',
    'vimeo.com',
    'vkontakte.ru',
    'weibo.com/',
    'youtube.com/',
]
BETWEEN = ['user/', 'add/', 'pages/', '#!/', 'photos/', 'u/0/']
ACCOUNT = r'[\w\+_@\.\-/%]+'
PATTERN = (r'%s(?:%s)(?:%s)?%s' % (
    PREFIX, '|'.join(SITES), '|'.join(BETWEEN), ACCOUNT))
SOCIAL_REX = re.compile(PATTERN, flags=re.I)
BLACKLIST_RE = re.compile(
    """
    sharer.php|
    /photos/.*\d{6,}|
    google.com/(?:ads/|
                  analytics$|
                  chrome$|
                  intl/|
                  maps/|
                  policies/|
                  search$
               )|
    instagram.com/p/|
    /share\?|
    /status/|
    /hashtag/|
    home\?status=|
    twitter.com/intent/|
    twitter.com/share|
    search\?|
    /search/|
    pinterest.com/pin/create/|
    vimeo.com/\d+$|
    /watch\?""",
    flags=re.VERBOSE)


def get_from_url(url):  # pragma: no cover
    """Get list of social media links/handles given an URL."""
    import requests
    from html_to_etree import parse_html_bytes
    res = requests.get(url)
    tree = parse_html_bytes(res.content, res.headers.get('content-type'))

    return list(find_links_tree(tree))


def matches_string(string):
    """Check if a given string matches known social media URL patterns."""
    return SOCIAL_REX.match(string) and not BLACKLIST_RE.search(string)


def find_links_tree(tree):
    """Find social media links/handles given a lxml etree.

    TODO:
    - `<fb:like href="http://www.facebook.com/elDiarioEs"`
    - `<g:plusone href="http://widgetsplus.com/"></g:plusone>`
    - <a class="reference external" href="https://twitter.com/intent/follow?screen_name=NASA">
    """
    for link in tree.xpath('//*[@href or @data-href]'):
        href = link.get('href') or link.get('data-href')
        if (href and
                isinstance(href, (six.string_types, six.text_type)) and
                matches_string(href)):
            yield href

    for script in tree.xpath('//script[not(@src)]/text()'):
        for match in SOCIAL_REX.findall(script):
            if not BLACKLIST_RE.search(match):
                yield match

    for script in tree.xpath('//meta[contains(@name, "twitter:")]'):
        name = script.get('name')
        if name in ('twitter:site', 'twitter:creator'):
            # FIXME: track fact that source is twitter
            yield script.get('content')
