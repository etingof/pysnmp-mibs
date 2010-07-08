#!/usr/bin/env python
import sys

def howto_install_setuptools():
    print """Error: You need setuptools Python package!

It's very easy to install it, just type (as root on Linux):
   wget http://peak.telecommunity.com/dist/ez_setup.py
   python ez_setup.py
"""

try:
    from setuptools import setup
except ImportError:
    for arg in sys.argv:
        if "egg" in arg:
            howto_install_setuptools()
            sys.exit(1)
    from distutils.core import setup

setup(name = 'pysnmp-mibs',
      version = '0.0.9a',
      description = 'A collection of pre-compiled PySNMP MIBs',
      author = 'Ilya Etingof',
      author_email = 'ilya@glas.net',
      url = 'http://sourceforge.net/projects/pysnmp/',
      license = 'BSD',
      requires = [ 'pysnmp' ],
      packages = [ 'pysnmp_mibs' ],
      scripts = [ 'tools/rebuild-pysnmp-mibs' ])
