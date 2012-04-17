#!/usr/bin/env python
import sys

def howto_install_setuptools():
    print("""Error: You need setuptools Python package!

It's very easy to install it, just type (as root on Linux):
   wget http://peak.telecommunity.com/dist/ez_setup.py
   python ez_setup.py
""")

try:
    from setuptools import setup
    params = {
        'install_requires': [ 'pysnmp>=4.2.2' ],
        'zip_safe': True
        }
except ImportError:
    for arg in sys.argv:
        if arg.find('egg') != -1:
            howto_install_setuptools()
            sys.exit(1)
    from distutils.core import setup
    params = {}
    if sys.version_info[:2] > (2, 4):
        params['requires'] = [ 'pysnmp(>=4.2.2)' ]

params.update( {
    'name': 'pysnmp-mibs',
    'version': '0.1.3',
    'description': 'A collection of IETF & IANA MIBs pre-compiled for PySNMP',
    'author': 'Ilya Etingof',
    'author_email': 'ilya@glas.net',
    'url': 'http://sourceforge.net/projects/pysnmp/',
    'classifiers': [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Intended Audience :: Telecommunications Industry',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Topic :: Communications',
      'Topic :: System :: Monitoring',
      'Topic :: System :: Networking :: Monitoring',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'License :: OSI Approved :: BSD License'
    ],    
    'license': 'BSD',
    'packages': [ 'pysnmp_mibs' ],
    'scripts': [ 'tools/rebuild-pysnmp-mibs' ]
    } )
               
setup(**params)
