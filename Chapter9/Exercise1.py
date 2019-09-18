'''
Exercise 1  
Write a program that reads the words in words.txt and stores them as keys in
a dictionary. It doesn't matter what the values are. Then you can use the in
operator as a fast way to check whether a string is in the dictionary.
'''


file = open('mbox-short.txt')
lines = [word.strip('\n') for word in file]
dictionary = {}
for line in lines:
    words = line.split()
    for word in words:
        dictionary [word] = 'xD'


def is_in_book(word, dictionary):
    if word in dictionary:
        return True
    else:
        return False

print(is_in_book('lol',dictionary))
print(is_in_book('From',dictionary))
print(is_in_book('mora',dictionary))



