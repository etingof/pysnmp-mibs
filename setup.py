#!/usr/bin/env python

from distutils.core import setup

setup(name="pysnmp-mibs",
      version="0.0.1",
      description="A collection of SNMP MIBs for PySNMP toolkit",
      author="Ilya Etingof",
      author_email="ilya@glas.net ",
      url="http://sourceforge.net/projects/pysnmp/",
      packages = [ 'pysnmp_mibs',
                   'pysnmp_mibs.libsmi' ],
      license="BSD")
