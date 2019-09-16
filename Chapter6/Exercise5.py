'''
Exercise 5
Take the following Python code that stores a string:`

string = 'X-DSPAM-Confidence:  0.8475'

Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
'''
string = 'X-DSPAM-Confidence:  0.8475'

index = string.find(' ')

number = float(string[index + 1:])

print(number, type(number))

    


