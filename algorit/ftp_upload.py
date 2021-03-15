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
Subject: Algorit Pricelist Error!

Algorit Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Algorit Pricelist Success!

Algorit Pricelist successfully uploaded on FTP!
"""



try:
    session = ftplib.FTP('ftp.algorit.de','ftp1104443-rodos','GX9nVCbHkt2FY8WUCzgo')
    file = open(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Algorit/testingcsvs/Brodos Preisliste {today}.csv','rb')                 
    session.storbinary(f'STOR Brodos Preisliste {today}.csv', file)    
    file.close()                                    
    session.quit()
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

