# !/usr/bin/env python
import sys
import re

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # removing all special characters
    line = re.sub('[^A-Za-z]+', ' ', line)
    # convert line to lower case
    line = line.lower()
    # split the line into words
    words = line.split()

    # key: (word, next word) value: 1
    for i in range(len(words)):
      # write the results to STDOUT (standard output);
      # output from mapper will be fed as input to reducer
      if i == len(words) - 1:
        break
      else:
        print('%s\t%s' % ((words[i], words[i+1]), 1))