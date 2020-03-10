# tsvisthebest
wow

### usage:
remove null bytes from file (required on first run): <br>
`tr < final.txt -d '\000' > myfile.txt`<br>
run map reduce job:<br>
`python2 map.py | python2 reduce.py | python2 writer.py >> output.txt`<br>

