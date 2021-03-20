"""
Exercise 2  
Write a program to look for lines of the form
New Revision: 39772
And extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.
Enter file:mbox.txt
38549.7949721
Enter file:mbox-short.txt
39756.9259259
"""

import re

file = open("mbox-short.txt")
lines = [line.strip("\n") for line in file]

total = 0
count = 0
for line in lines:
    if re.findall("New Revision: 397*", line):
        count += 1
        total += float(line[14:19])

print(total / count)
