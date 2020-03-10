import sys


def printSorted(d):
    for (v, k) in sorted( ((int(v),k) for k,v in d.iteritems()), reverse=True)[:10]:
        print ("  %s: %s" % (k, v))


out = {}
for line in sys.stdin:
    if line.strip():
        l = line.replace("(", "").replace(")", "").replace(" ", "").replace("\n", "").split(',')
        d, n, c = l
        if d not in out.keys():
            out[d] = {}
        out[d][n] = c

for d in out.keys():
    print(d)
    printSorted(out[d])