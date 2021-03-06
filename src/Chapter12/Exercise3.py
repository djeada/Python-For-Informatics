'''
Exercise 3
Useurllibto replicate the previous exercise of (1) retrieving thedocument from
a URL, (2) displaying up to 3000 characters, and (3) counting theoverall
number of characters in the document. Don’t worry about the headers forthis
exercise, simply show the first 3000 characters of the document contents.
'''

import urllib.request
import urllib.parse
import urllib.error
import os

url = input('Enter url: ')

try:
    fhand = urllib.request.urlopen(url)
except:
    print('Please enter a valid URL')
    os.sys.exit(1)

characters = 0
for line in fhand:
    words = line.decode()
    characters += len(words)
    if characters < 3000:
        print(line.decode().strip())
print(characters)
