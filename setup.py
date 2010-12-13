#!/usr/bin/env python
import sys
import string

def howto_install_setuptools():
    print """Error: You need setuptools Python package!

It's very easy to install it, just type (as root on Linux):
   wget http://peak.telecommunity.com/dist/ez_setup.py
   python ez_setup.py
"""

try:
    from setuptools import setup
    params = {
        'install_requires': [ 'pysnmp' ],
        'zip_safe': True
        }
except ImportError:
    for arg in sys.argv:
        if string.find(arg, 'egg') != -1:
            howto_install_setuptools()
            sys.exit(1)
    from distutils.core import setup
    if sys.version_info > (2, 2):
        params = {
            'requires': [ 'pysnmp' ]
            }
    else:
        params = {}

params.update( {
    'name': 'pysnmp-mibs',
    'version': '0.0.10a',
    'description': 'A collection of pre-compiled PySNMP MIBs',
    'author': 'Ilya Etingof',
    'author_email': 'ilya@glas.net',
    'url': 'http://sourceforge.net/projects/pysnmp/',
    'license': 'BSD',
    'packages': [ 'pysnmp_mibs' ],
    'scripts': [ 'tools/rebuild-pysnmp-mibs' ]
    } )
               
apply(setup, (), params)
