'''
Exercise 1  
Write a function that takes a string as an argument and displays the letters
backward, one per line.
'''

def backwards(word):
    x = len(word) - 1
    while x >= 0:
        print(word[x])
        x -= 1

backwards('hello')
