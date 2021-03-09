from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas as pd
import ctypes

df = pd.read_csv("url.csv", sep=',', encoding='unicode_escape')

urls = list(df.urls)
i=0

try:
    for url in urls:
        with open('form.csv','a+') as f:
            f.write(f"""
Hi,<br />
<br />
ein neuer Termin wurde gebucht:<br />
<br />
Service: %service_name%<br />
Kundenname: %name_kunde%<br />
E-Mail: %user_email%<br />
Telefonnummer: %tel_number%<br />
Datum und Uhrzeit: %appointment_date%<br />
<br />
<a href="https://www.brodos.net/omnichannel/termin-bestaetigen/?url={url}&service=%service_name%&name1=%name_kunde%&email=%user_email%&tel=%tel_number%&date=%appointment_date%&choice=accept">Termin akzeptieren</a>
<br />
<br />
<a href="https://www.brodos.net/omnichannel/termin-bestaetigen/?url={url}&service=%service_name%&name1=%name_kunde%&email=%user_email%&tel=%tel_number%&date=%appointment_date%&choice=decline">Termin ablehnen</a>
<br />
<br />
Wenn du deinem Kunden einen alternativen Termin vorschlagen möchtest
<a href="https://www.brodos.net/omnichannel/termin-bestaetigen/?url={url}&service=%service_name%&name1=%name_kunde%&email=%user_email%&tel=%tel_number%&date=%appointment_date%&choice=accept%20with%20a%20different%20date"
>klicke hier.</a>)
""")

            i+=1
except Exception as e:
    i += 1
    print(str(e))
    print('Sorry something went wrong while creation. Please attend manually from where its broken')
