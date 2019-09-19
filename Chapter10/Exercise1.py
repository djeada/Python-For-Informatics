'''
Exercise 1  
Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line. Count the number of messages from
each person using a dictionary.
After all the data has been read print the person with the most commits by
creating a list of (count, email) tuples from the dictionary and then sorting
the list in reverse order and print out the person who has the most commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

file = open('mbox-short.txt')
lines = [line.strip("\n") for line in file if line.startswith("From ")]
dictionary = {}

for line in lines:
    dictionary[line.split()[1]] = dictionary.get(line.split()[1], 0) + 1

list_of_tuples = [(dictionary[key], key) for key in dictionary]

print(sorted(list_of_tuples, reverse=True)[0][1],sorted(list_of_tuples, reverse=True)[0][0])

