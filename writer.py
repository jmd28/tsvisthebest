import sys
import re


def printSorted(d, file):
    for (v, k) in sorted( ((int(v),k) for k,v in d.iteritems()), reverse=True)[:10]:
        print ("  %s: %s" % (k, v))
        file.write("%s, %s\n" % (k.strip()[1:-1], v))


out = {}
for line in sys.stdin:
    # print(line)
    d, n, c = line.replace("(", "").replace(")", "").split(',')
    if d not in out.keys():
        out[d] = {}
    out[d][n] = c

for d in sorted(out.keys()):
    print(d)
    file = open("../out/%s.csv" % d[1:-1], 'w')
    file.write("Philosopher, Count\n")
    printSorted(out[d], file)
    file.close()