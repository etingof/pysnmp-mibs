#!/usr/bin/env python

from distutils.core import setup

setup(name="pysnmp-mibs",
      version="0.0.5a",
      description="A collection of pre-compiled SNMP MIBs for PySNMP",
      author="Ilya Etingof",
      author_email="ilya@glas.net ",
      url="http://sourceforge.net/projects/pysnmp/",
      packages = [ 'pysnmp_mibs', 'pysnmp_mibs.v4' ],
      scripts = [ 'tools/rebuild-pysnmp-mibs' ],
      license="BSD")
