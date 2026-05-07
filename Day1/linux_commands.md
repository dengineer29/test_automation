ps

* process status
* shows running processes
* find PID

Example:
ps aux
ps aux | grep python

---

top

* real-time process monitor
* CPU usage
* memory usage

Example:
top

Keys:
P = sort by CPU
M = sort by memory
q = quit

---

kill

* terminate process
* uses PID

Example:
kill 1234
kill -9 1234

---

grep

* search/filter text
* find logs/errors

Example:
grep ERROR logs.txt
python3 app.py | grep ERROR

---

|

* pipe
* passes output of one command to another

Example:
ps aux | grep python
cat logs.txt | grep FAIL

---

>

* output redirection
* saves output to file

Example:
python3 test.py > logs.txt

---

tail -f

* live log monitoring
* watches file updates in real time

Example:
tail -f logs.txt

---

Common workflow

Run script:
python3 test.py

Find process:
ps aux | grep python

Kill process:
kill PID

Save logs:
python3 test.py > logs.txt

Check errors:
grep ERROR logs.txt

Watch logs live:
tail -f logs.txt
