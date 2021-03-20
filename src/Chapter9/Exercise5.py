"""
Exercise 5
This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e. the whole
e-mail address). At the end of the program print out the contents of your
dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

file_name = open("mbox-short.txt")
lines = [
    line.strip("\n")
    for line in file_name
    if line.startswith("From") and not line.startswith("From:")
]
dictionary = {}

for line in lines:
    line = line.split()
    dictionary[line[1].split("@")[1]] = dictionary.get(line[1].split("@")[1], 0) + 1

print(dictionary)
