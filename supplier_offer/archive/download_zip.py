import requests
import zipfile

url = 'https://service.jacob.de/content/csvTool/BrodosSmall.zip'
r = requests.get(url, allow_redirects=True)
open('zipfile.rar', 'wb').write(r.content)


with zipfile.ZipFile('D:/python scripts/supplier_offer/zipfile.rar', 'r') as zip_ref:
    zip_ref.extractall('D:/python scripts/supplier_offer')
