#!/usr/bin/env python

import sys

f = open("PhilosophersFull.csv")
phils = f.read().splitlines()
# phils = ["Aristotle", "Plato", "Kant"]
phils = phils[1:]
phils = [p.split()[-1].upper() for p in phils]

inp = open("test3.txt")
inp = inp.read().splitlines()

# inp = sys.stdin

def to_decade(year):
    start = int(year) - int(year)%10
    # end = start + 10
    return str(start)+'s'


for line in inp:
    # print(line)
    line = line.strip()
    # line = str(line, 'utf-16')
    columns = line.split('\t')
    if len(columns) == 67:
        try:
            citation = columns[29]
            year = columns[44]
            cites = citation.upper().split(';')
            out = ["%s\t%s\t1" % (to_decade(year), p) for c in cites for p in phils if p in c]
            for l in out:
                print(l)

        except ValueError:
            pass
