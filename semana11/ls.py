#! /usr/bin/env python3

# Modulos sugeridos  os, stat, pwd, grp, datetime, sys

import datetime, os, stat, pwd, grp, sys

from collections import namedtuple
file = namedtuple('file', 'name date')
arch = file('test.txt', datetime.time)
print(arch.name)
help(grp)