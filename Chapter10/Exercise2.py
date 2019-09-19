'''
Exercise 2  
This program counts the distribution of the hour of the day for each of the
messages. You can pull the hour from the "From" line by finding the time
string and then splitting that string into parts using the colon character.
Once you have accumulated the counts for each hour, print out the counts,
one per line, sorted by hour as shown below.
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

file = open('mbox-short.txt')
lines = [line.strip("\n") for line in file if line.startswith("From ")]
dictionary = {}

for line in lines:
    dictionary[line.split()[5].split(":")[0]] = dictionary.get(line.split()[5].split(":")[0], 0) + 1

list_of_tuples = [(dictionary[key], key) for key in dictionary]

for item in list_of_tuples:
    print(item[0], item[1])
