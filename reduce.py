#!/usr/bin/env python

# from operator import itemgetter
import sys

# keep a map of the sum of upvotes of each reddit
countmap = {}


for line in sys.stdin:
    if line.strip():
        decade, name, count = line.split('\t')
        try:
            count = int(count)
            if decade != "2020-2029":
                countmap[(decade, name)] = int(countmap.get((decade, name), 0)) + count
        except ValueError:
            # ignore lines where the count is not a number
            pass

for key in countmap.keys() :
    print(key, countmap[key])
