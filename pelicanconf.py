#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wm. Minchin'
SITENAME = u'Minchin.ca'
SITEURL = ''

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custome settings
FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')	#default?
MARKUP = (( 'rst',
			'md',
			'markdown',
			'mkd',
			'mdown',
			'html',
			'htm'))	 
PATH = 'content'
RELATIVE_URLS = True	# for testing
TYPOGRIFY = True
THEME = 'S:\Documents\GitHub\pelican-themes\pelican-bootstrap3'
