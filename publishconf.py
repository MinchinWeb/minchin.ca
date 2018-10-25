#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = '//minchin.ca'
RELATIVE_URLS = False
LOAD_CONTENT_CACHE = False
# OUTPUT_PATH = '../minchinweb.github.io-master/'  # default is 'output/'

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-384291-3'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'minchin.ca'

PLUGINS = PLUGINS + [
                     # 'assets',
                     'minify',  # pelican-minify
                     'extended_sitemap',  # pelican-extended-sitemap
                     'minchin.pelican.plugins.optimize_images',  # need executables for Linux to do this on Travis-CI
                     'minchin.pelican.plugins.cname',
                     'minchin.pelican.plugins.nojekyll',
                     ]
