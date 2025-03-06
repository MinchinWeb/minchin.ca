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


Note to Self: To Manage Dependencies
------------------------------------

To update requirements::

    pip-compile --update

To update the (local) virtual environment::

    pip -m piptools sync

(Note that ``pip-sync`` can't update itself on Windows.)
