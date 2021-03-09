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
email_send = 'ankurparanjpe10@gmail.com'

subject = 'subject'
try:
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        
        body = 'Hi there, sending this email from Python!'
        msg.attach(MIMEText(body,'plain'))

        for filename in os.listdir('D:/Python projects/Brodosprojects/ftp download'):
                if fnmatch.fnmatch(filename, 'Warenausgang*'+str(datetime.date.today())+'.csv'):
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
                    newname = 'D:/Python projects/Brodosprojects/ftp download/done/' + str(filename)
                    prevname = 'D:/Python projects/Brodosprojects/ftp download/' + str(filename)
                    shutil.move(prevname, newname)
                    print(filename)
                    print ('email sent')
except:
        print ('error sending mail')


server.quit()
