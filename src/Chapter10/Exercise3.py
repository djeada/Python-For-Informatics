'''
Exercise 3
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at
wikipedia.org/wiki/Letter_frequencies.
'''


file = open('mbox-short.txt')
lines = [line.strip("\n") for line in file]
dictionary = {}

for line in lines:
    words = line.split()
    for word in words:
        for x in word:
            if x.isalpha():
                dictionary[x.lower()] = dictionary.get(x.lower(), 0) + 1


list_of_tuples = [(dictionary[key], key) for key in dictionary]


for item in sorted(list_of_tuples, reverse=True):
    print(item[1], item[0])


