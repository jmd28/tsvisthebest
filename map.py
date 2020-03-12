#!/usr/bin/env python

import sys
import re

f = open("PhilosophersFullToo.csv")
phils = f.read().splitlines()

# remove header
phils = phils[1:]

inp = open("../data/cleanedfinal.txt")
inp = inp.read().splitlines()

# inp = sys.stdin


# currently only works if author cited with full name or initials 
# (not surname only where other names are present)
def in_citation(philosopher, citation):
    
    names = [n.upper() for n in philosopher.split()] #splits entire name into subnames
    surname = names[-1] #gets the last element in the list which is the surname
    if not surname in citation: return False
    #makes a set of the first n-1 subnames and gets their first character
    # - (where n is the length of the entire name) 
    initials = {name[0] for name in names[:-1]}

    fields = citation.split(',')   # delimited by comma
    for f in fields:
        s = re.sub("[^\w\-\']", ' ', f).split()  #removed symbols and replace with spaces. Then split on whitespace.
        for entry in s:
            if surname == entry.upper():
                if not initials:
                    # print(initials, surname)
                    # print(citation)
                    return True
                if len(s) == 1:
                    return True
                else:
                    # if not index 0, look left
                    if s.index(surname) != 0 and s[s.index(surname) - 1][0] in initials:
                        # print(initials, surname)
                        # print(citation)
                        return True
                    # if not index last, look right
                    if s.index(surname) != (len(s)-1) and s[s.index(surname) + 1][0] in initials:
                        # print(initials, surname)
                        # print(citation)
                        return True

    return False

def to_decade(year):
    start = int(year) - int(year)%10
    end = start + 9
    return str(start)+'-'+ str(end)

for line in inp:
    line = line.strip()
    columns = line.split('\t')
    if len(columns) == 67:
        try:
            citations = columns[29]
            year = columns[44]
            cites = citations.upper().split(';')
            out = ["%s\t%s\t1" % (to_decade(year), p) for c in cites for p in phils if in_citation(p, c)]
            for l in out:
                print(l)

        except ValueError:
            pass


