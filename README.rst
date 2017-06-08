====================
Extract Social Media
====================

.. image:: https://img.shields.io/pypi/v/extract-social-media.svg
        :target: https://pypi.python.org/pypi/extract-social-media

.. image:: https://img.shields.io/pypi/pyversions/extract-social-media.svg
        :target: https://pypi.python.org/pypi/extract-social-media

.. image:: https://img.shields.io/travis/fluquid/extract-social-media.svg
        :target: https://travis-ci.org/fluquid/extract-social-media

.. image:: https://codecov.io/github/fluquid/extract-social-media/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/fluquid/extract-social-media

.. image:: https://requires.io/github/fluquid/extract-social-media/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/fluquid/extract-social-media/requirements/?branch=master

Extract social media links from websites.

Many websites reference their facebook, twitter, linkedin, youtube accounts
and these can be invaluable to gather 360 degree information about a company.

This library allows to extract links or handles for the most commonly used
international social media networks.

* Free software: MIT license
* Python versions: 2.7, 3.4+

Features
--------

* Extract social media links/handles from html content
* Attempts to extract links/handles also from widgets, scripts, etc.
* Supports most widely used social networks

  * facebook
  * linkedin
  * twitter
  * youtube
  * github
  * google plus
  * pinterest
  * instagram
  * snapchat
  * flipboard
  * flickr
  * weibo
  * periscope
  * telegram
  * soundcloud
  * feedburner
  * vimeo
  * slideshare
  * vkontakte
  * xing

Quickstart
----------

.. code:: python

   import requests
   from html_to_etree import parse_html_bytes
   res = requests.get('https://techcrunch.com/contact/')
   tree = parse_html_bytes(res.content, res.headers.get('content-type'))

   set(find_links_tree(tree))

   {'http://pinterest.com/techcrunch/',
    'http://www.youtube.com/user/techcrunch',
    'http://www.linkedin.com/company/techcrunch',
    'https://www.facebook.com/techcrunch',
    'https://flipboard.com/@techcrunch',
    'http://instagram.com/techcrunch',
    'https://plus.google.com/+TechCrunch',
    'https://instagram.com/techcrunch',
    'https://twitter.com/techcrunch'}

Caveats
-------

* currently finds all social media links on a page

  * need to look into finding most relevant links based on link location,
    link context, company name, etc.

Credits
-------

This package was created with Cookiecutter_ and the `fluquid/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`fluquid/cookiecutter-pypackage`: https://github.com/fluquid/cookiecutter-pypackage
