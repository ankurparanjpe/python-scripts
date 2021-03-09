import xml.etree.ElementTree as ET
import csv
import xml.sax.saxutils as saxutils
import html
"""
abc= '&quot;#'
print (saxutils.unescape(abc))
"""

tree = ET.parse("C:/Users/ANKUR/Desktop/python/Brodosprojects/testxml/specialcharacter.xml")
root = tree.getroot()

f = open('C:/Users/ANKUR/Desktop/python/Brodosprojects/testxml/specialcharacter.csv', 'w', newline='')

csvwriter = csv.writer(f)

count = 0

head = ['author','title','genre','price','description']

csvwriter.writerow(head)

for time in root.findall('book'):
    row = []
    autho = time.find('author').text
    row.append(author)
    title = time.find('title').text
    row.append(title)
    genre = time.find('genre').text
    row.append(genre)
    price = time.find('price').text
    row.append(price)
    description = time.find('description').text
    row.append(description)
f.close()

