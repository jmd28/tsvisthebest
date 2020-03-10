#!/usr/bin/env python

# from operator import itemgetter
import sys

# keep a map of the sum of upvotes of each reddit
countmap = {}


for line in sys.stdin:
    if line.strip():
        decade, name, count = line.split('\t')
        # print ("%s, %s, %s" % (decade, name, count))
        try:
            count = int(count)
            countmap[(decade, name)] = int(countmap.get((decade, name), 0)) + count
        except ValueError:
            # ignore lines where the count is not a number
            pass

for key in sorted(countmap.keys()) :
    print(key, countmap[key])
