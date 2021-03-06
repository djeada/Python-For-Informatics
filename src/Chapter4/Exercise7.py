'''
Exercise 7
Rewrite the grade program from the previous chapter using a function
called computegrade that takes a score as its parameter and returns a
grade as a string.
Score   Grade
> 0.9     A
> 0.8     B
> 0.7     C
> 0.6     D
<= 0.6    F
Program Execution:
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for
input. 
'''
import sys

score = 0

def computegrade(score):
    try:
        score = float(input('Enter score: '))
        if score < 0.6 and score > 0:
            return 'F'
        elif score >= 0.6 and score < 0.7:
            return 'D'
        elif score >= 0.7 and score < 0.8:
            return 'C'
        elif score >= 0.8 and score < 0.9:
            return 'B'
        elif score >= 0.9 and score < 1:
            return 'A'
        else:
            return 'Bad score, continuing.'
    except:
        print('Bad score, exiting.')
        sys.exit(1)
            
print(computegrade(score))

