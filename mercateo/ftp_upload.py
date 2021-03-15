import ftplib
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from  datetime import date,datetime,timedelta

today = datetime.today().strftime('%d.%m.%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: Mercateo Pricelist Error!

Mercateo Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Mercateo(availability) Pricelist Success!

Mercateo(availability) Pricelist successfully uploaded on FTP! And a copy placed on "NORMAL_PRICEIMPORT" folder.
"""



try:
    session = ftplib.FTP('ftp.mercateo.com','845_brodos','99593e6e')
    file = open(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Mercateo/availability/availability-data-catalog-25274.csv','rb')                 
    session.storbinary(f'STOR /845/availability/availability-data-catalog-25274.csv', file)    
    file.close()                                    
    session.quit()
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

