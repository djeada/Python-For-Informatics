"""
Exercise 2
Change your socket program so that it counts the number of characters it has
received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire document and count the total number
of characters and display the count of the number of characters at the end
of the document.
"""

import socket
import os

url = input("Enter url: ")

try:
    words = url.split("/")
    if words[0] != "http:":
        host_url = words[0]
        url = "http://" + url
    else:
        host_url = words[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_url, 80))
    mysock.send("GET " + url + " HTTP/1.0\n\n")
except:
    print("Please enter a valid URL")
    os.sys.exit(1)

count = 0
while True:
    data = mysock.recv(512)
    count += len(data)
    if (len(data) < 1) or count >= 3000:
        break
    print(data)

mysock.close()
