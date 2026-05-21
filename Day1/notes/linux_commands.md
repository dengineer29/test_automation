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


GUIDE — THE 3 TOOLS
These tools process text files line by line. In automation testing, you'll use them to extract job IDs, usernames, or error codes from printer log files without writing Python scripts.
Tool	What it does	Best for
cut	Extracts specific columns or characters from each line	Fixed-format logs with delimiters like spaces or commas
awk	Processes each line as fields — most powerful of the three	Extracting specific fields, doing math, filtering by condition
sed	Find and replace text in a stream	Cleaning up log output, replacing values, deleting lines
# Sample printer log (logs.txt):
# 2026-05-07 09:12 skadi park.pdf 5pages IM307+ printed
# 2026-05-07 09:15 arona photo.jpg 2pages MP3055 cancelled
# 2026-05-07 09:20 skadi doc.txt 1pages IM307+ printed

# cut: extract column 3 (username) — delimiter is space
cut -d' ' -f3 logs.txt

# awk: print field 3 (username) and field 7 (status)
awk '{print $3, $7}' logs.txt

# awk: show only cancelled jobs
awk '$7 == "cancelled"' logs.txt

# sed: replace "printed" with "DONE" in output
sed 's/printed/DONE/g' logs.txt


GUIDE — THE 5 COMMANDS
As an automation tester at Xerox, printers live on a network. Before you can test a printer you need to confirm it's reachable, what port it's listening on, and whether your machine can talk to it. These 5 commands are how you check that from the terminal.

Command             What it does	                                        When to use it
    
ping host	        Checks if a machine is reachable                        First check — is the printer even online?
                    on the network at all	
    
curl url	        Makes an HTTP request and shows                     	Check if the printer's web interface or IPP port responds
                    the response — works with IPP too
    
ss -tlnp	        Shows all open ports and which                          Confirm CUPS is listening on port 631
                    process is listening on each	
    
netstat -tlnp	    Same as ss but older — still found on many servers	    Legacy systems where ss isn't available
    
traceroute host	    Shows every network hop between you and the target	    Diagnose where a connection is failing