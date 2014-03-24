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
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# static paths will be copied under the same name
STATIC_PATHS = ['images', '_extras']

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    '_extras\minchin.ico': {'path': 'favicon.ico'},
    }

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Custom settings
#FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')	#default?
MARKUP = (( 'rst',
			'md',
			'markdown',
			'mkd',
			'mdown',
			'html',
			'htm'))	 
PATH = '../_content'
OUTPUT_PATH = '../'

# Theme Related
TYPOGRIFY = True
THEME = 'themes/pelican-minchin-ca'
DISPLAY_CATEGORIES_ON_MENU = False
SITELOGO = 'images/MinchindotCA-200.png'
SITELOGO_SIZE = 200
HIDE_SITENAME = True
PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = 'favicon.ico'
HIDE_SIDEBAR = True
BOOTSTRAP_THEME = 'cerulean'
# like fonts of simplex, shamrock


