#!/usr/bin/env python

from distutils.core import setup

setup(name="pysnmp-mibs",
      version="0.0.1a",
      description="A collection of pre-compiled SNMP MIBs for PySNMP",
      author="Ilya Etingof",
      author_email="ilya@glas.net ",
      url="http://sourceforge.net/projects/pysnmp/",
      packages = [ 'pysnmp_mibs' ],
      license="BSD")
