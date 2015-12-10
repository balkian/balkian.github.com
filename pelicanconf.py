#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from functools import partial
from collections import Counter

AUTHOR = u'J. Fernando S\xe1nchez'
SITENAME = u'balkian.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "balkiantheme"

PLUGIN_PATHS = ["plugins/",]
PLUGINS = ["neighbors",]

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

STATIC_PATHS = [
    'extra/CNAME',
    'extra/favicon',
    'fonts'
    ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon': {'path': 'favicon'},
}

IGNORE_FILES = ['.*']

MENUITEMS=[('CV','http://jfernando.es')]

DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU = True

CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

CATEGORIES_SAVE_AS = 'categories.html'
DEFAULT_CATEGORY = 'misc'


def date_to_string(date):
    return date.strftime('%Y-%m-%d')

def sort_by_article_count(x):
    return sorted(x, key=lambda tags: len(tags[1]), reverse=True)

def normalize_count(x):
    articles, tag = x
    counter = Counter()
    for i in articles:
        counter.update(i.tags)        
    maximum = counter.most_common(1)[0][1]
    return 100*counter[tag]/maximum
    
JINJA_FILTERS = {
    'sort_by_article_count': sort_by_article_count,
    'date_to_string': date_to_string,
    'normalize_count': normalize_count
}
