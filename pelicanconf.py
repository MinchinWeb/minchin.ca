#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wm. Minchin'
SITENAME = u'Minchin.ca'
SITEURL = 'http://minchin.ca'

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
				'..\extras',
				'css',
				'design',
				'..\.gitattributes',
				'..\.gitignore',
				'..\README.txt',]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
	'..\.gitattributes': 			{'path': '.gitattributes'},
	'..\.gitignore': 				{'path': '.gitignore'},
	'..\README.txt': 				{'path': 'README.txt'},
	'..\extras\CNAME': 				{'path': 'CNAME'},
    '..\extras\minchin.ico': 		{'path': 'favicon.ico'},
	'..\extras\MTS_1v1.xlsm': 		{'path': 'MTS_1v1.xlsm'},
	'..\extras\TRB_Minchin.ca.XSL': {'path': 'TRB_Minchin.ca.XSL'},
    }



# Custom settings
#FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')	#default?
MARKUP = (( 'rst',
			'md',
			'markdown',
			'mkd',
			'mdown',
			'html',
			'htm'       ))
PATH = 'content'
OUTPUT_PATH = '../minchinweb.github.io-master/'

# Add Blog to sidebar
MENUITEMS = ( 	('Blog', 	'http://blog.minchin.ca/', 'fa fa-pencil'), )
DISPLAY_PAGES_ON_MENU = True

# disable Tags
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Theme Related
TYPOGRIFY = True
THEME = 'themes/pelican-minchin-ca'
SITELOGO = 'images/MinchindotCA-200.png'
SITELOGO_SIZE = '100%'
PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = 'favicon.ico'
BOOTSTRAP_THEME = 'minchin-ca'
USE_OPEN_GRAPH = True
CUSTOM_CSS = 'css/minchin-ca.css'
DOCUTIL_CSS = False

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-384291-3'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'minchin.ca'

# Plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['assets', 'minify', 'sitemap', 'optimize_images']

ASSET_CSS = False	
ASSET_JS = False

SITEMAP = {
	"format": "xml",
}

# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` & `pelican_comment_system` might be useful...
# `optimize_images` works, but I don't have many images yet
#		- requires `jpegtran.exe` <http://jpegclub.org/jpegtran/> and
#			`optinpng.exe` <http://sourceforge.net/projects/optipng/>


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
