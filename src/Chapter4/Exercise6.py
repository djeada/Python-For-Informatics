"""
Exercise 6
Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours
and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
import sys

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    sys.exit(1)


def calculate_pay(hours, rate):
    if hours > 40:
        return (40 * rate) + (hours - 40) * rate * 1.5
    else:
        return hours * rate


print("Pay: %.2f" % calculate_pay(hours, rate))
