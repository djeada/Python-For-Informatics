'''
Exercise 4
Add code to the above program to figure out who has the most messages in the
file.
After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section ??) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

file = open('mbox-short.txt')
lines = [line.strip('\n') for line in file if line.startswith('From ')]
dictionary = {}

for line in lines:
    words = line.split()
    dictionary[words[1]] = dictionary.get(words[1], 0) + 1


maximum = 0
winner_address = None

for address in dictionary:
    if dictionary[address] > maximum:
        maximum = dictionary[address]
        winner_address = address

print(winner_address, maximum)
