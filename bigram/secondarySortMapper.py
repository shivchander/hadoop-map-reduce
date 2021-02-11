# !/usr/bin/env python
import sys
import re

'''Secondary Sort'''

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line key and value
    key = line.split('\t')[0]
    value = line.split('\t')[1]
    print('%s\t%s' % ((key, value), 1))
