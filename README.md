
Pre-compiled PySNMP MIBs
------------------------
[![Build status](https://travis-ci.org/etingof/pysnmp-mibs.svg?branch=master)](https://secure.travis-ci.org/etingof/pysnmp-mibs)
[![Python Versions](https://img.shields.io/pypi/pyversions/pysnmp-mibs.svg)](https://pypi.python.org/pypi/pysnmp-mibs/)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/etingof/pysnmp-mibs/master/LICENSE.txt)

This is a collection of IETF & IANA MIBs pre-compiled and packaged to
simplify their use with older versions of [PySNMP library](http://pysnmp.sf.net).

WARNING: since version 4.3, PySNMP performs MIB parsing automatically by calling
[pysmi](http://pysmi.sf.net) library. You may still need `pysnmp-mibs` package if
you are running older version of PySNMP.

MIB modules shipped in pysnmp-mibs package were taken from
[http://mibs.snmplabs.com/asn1/](http://mibs.snmplabs.com/asn1/) and compiled
into pysnmp format with pysmi's
[mibdump.py](https://github.com/etingof/pysmi/blob/master/scripts/mibdump.py)
tool.

Installation
------------

Download pysnmp-mibs from [PyPI](https://pypi.python.org/pypi/pysnmp-mibs) or just run:

```bash
$ pip install pysnmp-mibs
```

Getting help
------------

If something does not work as expected, try browsing PySNMP
[mailing list archives](http://sourceforge.net/mail/?group_id=14735) or post
your question [to Stack Overflow](http://stackoverflow.com/questions/ask).

Feedback and collaboration
--------------------------

I'm interested in bug reports, fixes, suggestions and improvements. Your
pull requests are very welcome!

Copyright (c) 2005-2017, [Ilya Etingof](mailto:etingof@gmail.com). All rights reserved.
