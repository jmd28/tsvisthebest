# tsvisthebest
wow

### usage:
remove null bytes from file (required on first run): <br>
`tr < final.txt -d '\000' > myfile.txt`<br>
run map reduce job:<br>
`python2 map.py | python2 reduce.py | python2 writer.py`<br>

**writes csvs to:**
- ../out/1980-1989.csv
- ../out/1990-1999.csv
- ../out/2000-2009.csv
- ../out/2010-2019.csv
(these must exist before running)
