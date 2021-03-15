import ftplib
from  datetime import date,datetime
import requests
from zipfile import ZipFile
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from subprocess import call
import re
import fnmatch

"""Defining variables"""
today = datetime.today().strftime('%d-%m-%Y')

message_zip = """From: <rncteam@brodos.net>
Subject: Zip file download has failed for stocklist!

Zip file download has failed for stocklist!
"""
email_user = 'rncteam@brodos.net'
email_send = ['rncteam@brodos.net']
message_file = """From: <rncteam@brodos.net>
Subject: Stocklist File Date Error!

One of the files for stocklist report are older!
"""



"""Trying to download all file and moving to /done folder in FTP.
In case it failed, it will send an error message."""
#Entering FTP
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("article-report", "ij8johh6iGh8eiJoh8pe")
ftp.cwd('/export')


filenames = ftp.nlst(f"Exportfile-{today}.zip")
print (filenames)

try:
    for filename in filenames:
        with open(filename,'wb') as f:
            ftp.retrbinary('RETR %s' % filename, f.write)
            f.close()
            #ftp.rename(latest_name, f'/export/done/{latest_name}')
            ftp.quit()
            #os.rename(f'{latest_name}', f'{latest_name}')
            #print(f"File {latest_name} downloaded and renamed to Feed.csv")
            with ZipFile(f"Exportfile-{today}.zip", 'r') as zip_ref:
                zip_ref.extractall('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Exportfile')

except Exception as e:
    print (str(e))
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_zip)

os.remove(f"Exportfile-{today}.zip")


