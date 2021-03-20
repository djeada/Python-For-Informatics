"""
Exercise 1  
Change the socket program socket1.py to prompt the user for the URL so it can
read any web page. You can use split('/') to break the URL into its component
parts so you can extract the host name for the socket connect call. Add error
checking using try and except to handle the condition where the user enters
an improperly formatted or non-existent URL.
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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()
