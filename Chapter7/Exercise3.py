'''
Exercise 3  
Sometimes when programmers get bored or want to have a bit of fun, they add
a harmless Easter Egg to their program
(en.wikipedia.org/wiki/Easter_egg_(media)). Modify the program that prompts
the user for the file name so that it prints a funny message when the user
types in the exact file name 'na na boo boo'. The program should behave
normally for all other files which exist and don't exist. Here is a sample
execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs - this is just
an exercise.
'''

import sys
import os.path

file_name = input('Enter a file name: ')

if file_name == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    sys.exit(0)

elif not os.path.isfile(file_name):
    print('File cannot be opened: {}'.format(file_name))
    sys.exit(0)

lines = [line.strip('\n')  for line in open(file_name, 'r')]

subject_count = 0
for line in lines:
    if line.startswith('Subject'):
          subject_count += 1
print(subject_count)
