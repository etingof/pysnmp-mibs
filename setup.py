#!/usr/bin/env python

from distutils.core import setup

setup(name="pysnmp-mibs",
      version="0.1.1",
      description="A collection of SNMP MIBs for PySNMP toolkit",
      author="Ilya Etingof",
      author_email="ilya@glas.net ",
      url="http://sourceforge.net/projects/pysnmp/",
      data_files=[('/usr/local/bin',
                   ['tools/libsmi2pysnmp', 'tools/pysnmpmibdir'])],
      license="BSD")
