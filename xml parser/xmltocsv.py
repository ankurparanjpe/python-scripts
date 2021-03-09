import xml.etree.ElementTree as ET
import csv

xmlp = ET.XMLParser(encoding = "utf-8")
tree = ET.parse("D:/python scripts/xml parser/book.xml", parser =xmlp)
root = tree.getroot()

f = open('D:/python scripts/xml parser/booktest.csv', 'w', newline='', encoding='utf-8')

csvwriter = csv.writer(f)

count = 0

head = ['Author','Title','Genre','Price','Publish date', 'description']

csvwriter.writerow(head)

for time in root.findall('book'):
    row = []
    Author = time.find('author').text
    row.append(Author)
    Title = time.find('title').text
    row.append(Title)
    Genre = time.find('genre').text
    row.append(Genre)
    Price = time.find('price').text
    row.append(Price)
    Publish = time.find('publish_date').text
    row.append(Publish)
    Description = time.find('description').text
    row.append(Description)
    csvwriter.writerow(row)
f.close()
