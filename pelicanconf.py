#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import seafoam

# Caching
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

AUTHOR = u'Wm. Minchin'
SITENAME = u'Minchin.ca'
# SITEURL = 'http://minchin.ca'
SITEURL = ''
SITE_ROOT_URL = SITEURL

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = u'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

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
STATIC_PATHS = ['images',
                '../extras',
                'css',
                'projects/design',
                '../.gitattributes',
                '../.gitignore',
                '../README.txt', ]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    '../.gitattributes':                     {'path': '.gitattributes'},
    '../.gitignore':                         {'path': '.gitignore'},
    '../README.txt':                         {'path': 'README.txt'},
    '../extras/minchin.ico':                 {'path': 'favicon.ico'},
    '../extras/MTS_1v1.xlsm':                {'path': 'MTS_1v1.xlsm'},
    '../extras/TRB_Minchin.ca.XSL':          {'path': 'TRB_Minchin.ca.XSL'},
    '../extras/TRB_Minchin.ca.2013.XSL':     {'path': 'TRB_Minchin.ca.2013.XSL'},
    '../extras/googlecbc66a9bfde8606b.html': {'path': 'googlecbc66a9bfde8606b.html'},
    }

# Custom settings
#FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')  #default?
MARKUP = (('rst',
           'md',
           'markdown',
           'mkd',
           'mdown',))  # don't include htm and html files
READERS = {'html': None,
           'htm': None}
PATH = 'content'
# OUTPUT_PATH = '../minchinweb.github.io-temp/'  # default is 'output/'

# Add Blog to sidebar
MENUITEMS = (('Blog',    'http://blog.minchin.ca/', 'fa fa-pencil'), )
DISPLAY_PAGES_ON_MENU = True

# disable Tags, etc
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_URL = ''
CATEGORIES_SAVE_AS = ''
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_URL = ''
ARCHIVES_SAVE_AS = ''
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Theme Related
TYPOGRIFY = True
# THEME = 'themes/pelican-minchin-ca'
THEME = seafoam.get_path()
BOOTSTRAP_THEME = 'seafoam'
SITELOGO = 'images/MinchindotCA-200.png'
SITELOGO_SIZE = '100%'
# PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = 'favicon.ico'
USE_OPEN_GRAPH = True
#CUSTOM_CSS = 'css/minchin-ca.css'  # folded into Bootstrap theme
DOCUTIL_CSS = False
INDEX_COPY_DATE = '2007-{}'.format(str(date.today().year)[-2:])

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = [
           'minchin.pelican.jinja_filters',  # required by seafoam theme
           ]

ASSET_CSS = False
ASSET_JS = False

SITEMAP = {
    "format": "xml",
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.def_list': {},
    },
    'output_format': 'html5',
}

# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` might be useful...


# # Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False
