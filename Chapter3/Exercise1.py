'''
Exercise 1
Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
OVERTIME_RATE = 1.5

def calculate_pay(hours, rate):
    overtime_pay = 0
    if hours > 40:
        result = (40 * rate) + (hours - 40)* rate * OVERTIME_RATE
    else:
        result = (hours * rate)
    return 'Pay: ' + str(result)

print(calculate_pay(hours, rate))
