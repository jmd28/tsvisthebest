# tsvisthebest

A map reduce style project to process a TSV-formatted file - obtained excruciatingly by manually dowloading 185000 records in batches of 500 from the Web of Science resource banks.

This was a commission from a geography lecturer interested to learn the frequencies with which geographical papers cite the works of certain philosophers, on a per decade basis.

### usage:
remove null bytes from file (required on first run): <br>
`tr < final.txt -d '\000' > myfile.txt`<br>
run map reduce job:<br>
`python2 map.py | python2 reduce.py | python2 writer.py`<br>

**writes csvs to:**
- ../out/1980-1989.csv
- ../out/1990-1999.csv
- ../out/2000-2009.csv
- ../out/2010-2019.csv <br>
(these must exist before running)
