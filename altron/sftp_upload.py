import ftplib
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import pysftp

message_failed = """From: <rncteam@brodos.net>
Subject: Alltron Pricelist Error!

Alltron Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Alltron Pricelist Success!

Alltron Pricelist successfully uploaded on SFTP!
"""


try:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host="91.213.100.42", username="A3273",password="221mB6q175Dx27523t.3G2cV",cnopts=cnopts) as sftp:       
        with sftp.cd("/pricelistimport"):
            sftp.put('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/w_Alltron/xlsxcopies/Preisliste Ausgabe.csv')
            
            smtpObj = smtplib.SMTP('172.17.7.101')
            smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

