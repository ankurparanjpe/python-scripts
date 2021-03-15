import ftplib
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

message_failed = """From: <rncteam@brodos.net>
Subject: Duttenhofer Pricelist Error!

Duttenhofer Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Duttenhofer Pricelist Success!

Duttenhofer Pricelist successfully uploaded on FTP!
"""



try:
    session = ftplib.FTP('datahost01.duttenhofer.net','DataEx_Brodos','lkZr5bF7Jh')
    file = open('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Duttenhofer/csvfiles/GesamtPRL.csv','rb')                 
    session.storbinary('STOR /Einkauf/GesamtPRL.csv', file)     
    file.close()                                    
    session.quit()
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

