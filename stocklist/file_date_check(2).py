import ftplib
from  datetime import date,datetime,timedelta
import requests
from zipfile import ZipFile
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from subprocess import call

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
today1 = datetime.today().strftime('%d-%m-%Y')
email_user = 'rncteam@brodos.net'
email_send = ['rncteam@brodos.net']
message_file = """From: <rncteam@brodos.net>
Subject: Stocklist File Data/source Error!

One of the files for stocklist report file source are older or not available in required path!
"""

try:
    export_file = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Exportfile/tmp/MEGA-{today1}.csv')
    stat_file = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/STAT.txt')
    artset_file = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/ARTSET.txt')
    lager_file = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/LAGER.txt')
    artikel_file = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/ARTIKEL.txt')
    lieferantenrueckstaende = os.path.getmtime(f'I:/daten/rms-reports/backlog/EK_BACKLOG_REPORT_{yesterday}.csv')
    kundenrueckstaende =  os.path.getmtime(f'I:/daten/rms-reports/backlog/VK_BACKLOG_REPORT_{yesterday}.csv')

    """Checking weather the files are updated"""
    export_file = datetime.fromtimestamp(export_file).strftime('%d-%m-%Y')
    stat_file = datetime.fromtimestamp(stat_file).strftime('%d-%m-%Y')
    artset_file = datetime.fromtimestamp(artset_file).strftime('%d-%m-%Y')
    lager_file = datetime.fromtimestamp(lager_file).strftime('%d-%m-%Y')
    artikel_file = datetime.fromtimestamp(artikel_file).strftime('%d-%m-%Y')
    lieferantenrueckstaende = datetime.fromtimestamp(lieferantenrueckstaende).strftime('%d-%m-%Y')
    kundenrueckstaende = datetime.fromtimestamp(kundenrueckstaende).strftime('%d-%m-%Y')

    if artikel_file and stat_file and artset_file and lager_file and artikel_file and export_file and lieferantenrueckstaende and kundenrueckstaende == today1:
        print('yes its from today')
        call(['I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/STOCKLIST (RDP-Excel Monster).bat'])
    else:
        print('nope')
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_file) 

except Exception as e:
    print('nope')
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_file) 


