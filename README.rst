Minchin.ca
==========

This is used to host the website at http://minchin.ca

The site is generated using Pelican, a static site generator for Python.
The source is stored in the `pelican` branch and the output (the site proper)
is stored in the `master` branch.

For the pages hosted at https://genealogy.minchin.ca/ , the code is
hosted at https://github.com/MinchinWeb/genealogy

For the blog (and pages) hosted at https://blog.minchin.ca/ , the code is
hosted at https://github.com/MinchinWeb/blog.minchin.ca/

Several project pages are also "served" from this site, although they typically
aren't well intregrated into the rest of the site. (For this to work, this
repo needs to stay named ``username.github.io`` and hosted by Github.) There
include:

- documentation for `colourettu <http://minchin.ca/colourettu/>`_` , a Python
  library for working with colours and colour palettes (`page source
  <https://github.com/MinchinWeb/colourettu/tree/gh-pages>`_, generated with
  Sphinx);
- `Introduction to Pelican <http://minchin.ca/introduction-to-pelican/>`_` --
  these are the presentation slides for a talk I did introducting Pelican to a
  local Python group in 2016. I have since reworked it into a `blog post
  <https://blog.minchin.ca/2017/05/introduction-to-pelican.html>`_ (that
  assumes I'm not standing there to give further commentary); you probably want
  the blog post! (`page source
  <https://github.com/MinchinWeb/introduction-to-pelican/tree/gh-pages>`_,
  generated with Pelican).
- documentation for OpenTTD's `MetaLibrary
  <http://minchin.ca/openttd-metalibrary/>`_, which is a collection of
  functions I wrote for writing AIs for OpenTTD. (`page source
  <https://github.com/minchinweb/openttd-metalibrary/tree/gh-pages>`, generated
  with doxygen)
- landing/download page for the `Progressive Rail Set
  <http://minchin.ca/openttd-progressive-rail/>`_` for OpenTTD. (`page source
  <https://github.com/MinchinWeb/openttd-progressive-rail/tree/gh-pages>`_,
  generated with Jekyll?)
- `vivint <https://minchin.ca/vivint/>`_, some notes from my time working there
  (dating back to 2016). (`source
  <https://github.com/MinchinWeb/vivint/tree/gh-pages>`_, generated with
  Sphinx)
- a landing page for `wm-todo <http://minchin.ca/wm_todo/>`_` a fork of
  ``todo.txt-python``. This was deprecated by me in 2016. (`source
  <https://github.com/MinchinWeb/wm_todo/tree/gh-pages>`_; written in raw
  HTML?)


Note to Self: To Manage Dependencies
------------------------------------

To update requirements::

    pip-compile --update

To update the (local) virtual environment::

    pip -m piptools sync

(Note that ``pip-sync`` can't update itself on Windows.)
