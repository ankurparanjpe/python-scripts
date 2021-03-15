import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os
import fnmatch
import datetime
import shutil

email_user = 'ankurparanjpe10@gmail.com'
email_password = 'qu@ke6arena'
email_send = 'bveavzus@mailparser.io'
today = datetime.datetime.today().strftime('%Y%m%d')
subject = f'FTP Macland_tracking_{today}'
try:
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        
        body = 'Macland has shared tracking details!'
        msg.attach(MIMEText(body,'plain'))

        for filename in os.listdir('I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland'):
                if fnmatch.fnmatch(filename, 'maclandgmbh_*.csv'):
                    attachment  =open(filename,'rb')
                    part = MIMEBase('application','octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= "+filename)
                    msg.attach(part)
                    text = msg.as_string()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email_user,email_password)

                    server.sendmail(email_user,email_send,text)
                    print(filename)
                    print ('email sent')
                    server.quit()
except Exception as e:
        print (str(e))
