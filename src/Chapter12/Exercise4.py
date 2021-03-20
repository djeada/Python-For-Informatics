"""
Exercise 4
Change theurllinks.pyprogram to extract and count paragraph(p) tags from the
retrieved HTML document and display the count of the para-graphs as the output
of your program. Do not display the paragraph text - onlycount them.
Test your program on several small web pages as well as some largerweb pages.
"""

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import os

url = input("Enter url: ")

try:
    fhand = urllib.request.urlopen(url)
    soup = BeautifulSoup(fhand.read(), "html.parser")

except:
    print("Please enter a valid URL")
    os.sys.exit(1)

print(len(soup("p")))
