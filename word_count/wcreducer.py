# !/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# read the entire line from STDIN from mapper
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # splitting the data using tab delimter
    word, count = line.split('\t', 1)
    # cast count from string to int
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # check if the frequency of word is between 5 and 10
            if 5 <= current_count <= 10:
                # write result to STDOUT
                print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# output the last word
if current_word == word:
    # check if the frequency of word is between 5 and 10
    if 5 <= current_count <= 10:
        # write result to STDOUT
        print('%s\t%s' % (current_word, current_count))