"""
Exercise 2  
Write a program to prompt for a file name, and then read through the file and
look for lines of the form:
X-DSPAM-Confidence:  0.8475
When you encounter a line that starts with 'X-DSPAM-Confidence:' pull apart
the line to extract the floating point number on the line. Count these lines
and the compute the total of the spam confidence values from these lines. When
you reach the end of the file, print out the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
"""

file_name = input("Enter a file name: ")
lines = [line for line in open(file_name, "r")]

confidence_sum = 0
confidence_count = 0
for line in lines:
    if line.find("X-DSPAM-Confidence") == -1:
        pass
    else:
        confidence_index = line.find(" ") + 1
        confidence = float(line[confidence_index:])
        confidence_sum += confidence
        confidence_count += 1
print("Average spam confidence: ", (confidence_sum / confidence_count))
