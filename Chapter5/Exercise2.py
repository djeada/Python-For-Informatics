'''
Exercise 2  
Write another program that prompts for a list of numbers as above and
at the end prints out both the maximum and minimum of the numbers
instead of the average.
'''

num_list = []
count = 0
while True:
    num = input('Enter a number: ')
    if num == 'done':
        print(min(num_list), max(num_list))
        break
    else:
        try:
            num_list.append(float(num))
        except:
            print('Invalid input')
            continue
    count += 1
