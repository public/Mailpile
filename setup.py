#!/usr/bin/python
from datetime import date
from setuptools import setup, find_packages
from mailpile.app import APPVER
import os

try:
  # This borks sdist.
  os.remove('.SELF')
except:
  pass

setup(
    name="mailpile",
    version=APPVER.replace('github',
                           'dev'+date.today().isoformat().replace('-', '')),
    license="AGPLv3+",
    author="Bjarni R. Einarsson",
    author_email="bre@klaki.net",
    url="http://www.mailpile.is/",
    description="""Mailpile is a personal tool for searching and indexing e-mail.""",
    long_description="""\
Mailpile is a tool for building and maintaining a tagging search
engine for a personal collection of e-mail.  It can be used as a
simple web-mail client.
""",
   packages=find_packages(),
   entry_points = {
     'console_scripts': [
       'mailpile = mailpile.__main__:main'
     ]
   },
)
