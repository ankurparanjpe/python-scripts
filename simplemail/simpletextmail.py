import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os
import fnmatch

email_user = 'ankurparanjpe10@gmail.com'
email_password = 'qu@ke6arena'
email_send = 'kazisahebaz@gmail.com'

subject = 'Iam sorry Sahebaz'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Sending mail from Python script.'
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,body)


try:
        print ('email sent')
except:
        print ('error sending mail')
        time.sleep(5)

server.quit()
