import ftplib
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import pysftp

message_failed = """From: <rncteam@brodos.net>
Subject: Computer center Pricelist Error!

Computer center Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Computer center Pricelist Success!

Computer center Pricelist successfully uploaded on FTP! And a copy sent to required stakeholders.
"""

try:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host="fileconnect.computacenter.com", username="brodos_accord",password="wLzRv6gOzxLK1zg6ExAE9", cnopts= cnopts) as sftp:       
        with sftp.cd("/"):
            sftp.put('I:/Abteilungen/Konzern-und-Geschaeftskunden/public/A Preislisten CC + Bechtle + Mercateo/xlsxcopies/ComputacenterPRL.csv')
            
            smtpObj = smtplib.SMTP('172.17.7.101')
            smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 



