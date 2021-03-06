'''
Exercise 1  
Write a simple program to simulate the operation of the the grep command on
Unix. Ask the user to enter a regular expression and count the number of
lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
'''

import re

regular_expression = input("Enter a regular expression: ")
file = open('mbox-short.txt')
lines = [line.strip('\n') for line in file]

count = 0
for line in lines:
    if re.search(re.compile(regular_expression), line):
        count += 1

print('mbox.txt had {} lines that matched {}'.format(count, regular_expression ))

