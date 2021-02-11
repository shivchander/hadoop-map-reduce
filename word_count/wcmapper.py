# !/usr/bin/env python
import sys
import re

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # removing all special characters
    line = re.sub(r"\W+|_", " ", line)
    # convert line to lower case
    line = line.lower()
    # split the line into words
    words = line.split()

    # key: word value: 1
    for word in words:
        # removing all the numbers
        if word.isalpha():
          # write the results to STDOUT (standard output);
          # output from mapper will be fed as input to reducer
          print('%s\t%s' % (word, 1))