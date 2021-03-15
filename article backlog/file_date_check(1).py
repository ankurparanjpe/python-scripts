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
from win32com.client import Dispatch

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
today1 = datetime.today().strftime('%d-%m-%Y')
email_user = 'rncteam@brodos.net'
email_send = ['rncteam@brodos.net']
message_file = """From: <rncteam@brodos.net>
Subject: Article backlog File Data/source Error!

One of the files for Article backlog report file source are older or not available in required path!
"""

try:
    stocklist_vba = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/STOCKLIST VBA.xlsm')
    stocklist = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/STOCKLIST.xlsx')
    produkte = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/PRODUKTE.xlsx')
    vertreter = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/VERTRETER.xlsx')
    kunden = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/KUNDEN.xlsx')
    zahlungsbedingungen = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/ZAHLUNGSBEDINGUNGEN.xlsx')
    vk1_backlog = os.path.getmtime(f'I:/daten/rms-reports/backlog/VK_BACKLOG_REPORT_{yesterday}.CSV')
    vk2_backlog = os.path.getmtime(f'I:/daten/rms-reports/backlog/VK_BACKLOG_REPORT_V2_{yesterday}.CSV')
    ek_backlog = os.path.getmtime(f'I:/daten/rms-reports/backlog/EK_BACKLOG_REPORT_{yesterday}.CSV')
    lagreich = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/LAGREICH.txt')
    auftrag = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/AUFTRAG.txt')
    

    """Checking weather the files are updated"""
    stocklist_vba = datetime.fromtimestamp(stocklist_vba).strftime('%d-%m-%Y')
    stocklist = datetime.fromtimestamp(stocklist).strftime('%d-%m-%Y')
    produkte = datetime.fromtimestamp(produkte).strftime('%d-%m-%Y')
    vertreter = datetime.fromtimestamp(vertreter).strftime('%d-%m-%Y')
    kunden = datetime.fromtimestamp(kunden).strftime('%d-%m-%Y')
    zahlungsbedingungen = datetime.fromtimestamp(zahlungsbedingungen).strftime('%d-%m-%Y')
    vk1_backlog = datetime.fromtimestamp(vk1_backlog).strftime('%d-%m-%Y')
    vk2_backlog = datetime.fromtimestamp(vk2_backlog).strftime('%d-%m-%Y')
    ek_backlog = datetime.fromtimestamp(ek_backlog).strftime('%d-%m-%Y')
    lagreich = datetime.fromtimestamp(lagreich).strftime('%d-%m-%Y')
    auftrag = datetime.fromtimestamp(auftrag).strftime('%d-%m-%Y')
    

    if stocklist_vba and stocklist and produkte and vertreter and kunden and zahlungsbedingungen and vk1_backlog and vk2_backlog and ek_backlog and lagreich and auftrag == today1:
        print('yes its from today')
        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(r'I:\\Abteilungen\\Reporting_und_Controlling\\private\\Reportings\\taeglich\\Artikelrückstande\\Artikelrückstände_REPORTING - Copy - Copy.xlsm')
    else:
        print('nope')
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_file) 

except Exception as e:
    print('nope')
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_file) 


