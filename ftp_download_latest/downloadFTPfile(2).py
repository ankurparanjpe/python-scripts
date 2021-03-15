import ftplib
from  datetime import date
import os
from dateutil import parser
# Open the FTP connection
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("transaction-support", "gq36aTbdQpdf3")
ftp.cwd('/order_delivery_monitoring')
today = date.today().strftime('%d-%m-%Y')
print (today)


filenames = ftp.retrlines('LIST')
print (filenames)


lines = []
ftp.dir("", lines.append)

latest_time = None
latest_name = None

for line in lines:
    tokens = line.split(maxsplit = 9)
    time_str = tokens[5] + " " + tokens[6] + " " + tokens[7]
    time = parser.parse(time_str)
    if (latest_time is None) or (time > latest_time):
        latest_name = tokens[8]
        latest_time = time

print(latest_name)

try:
    with open( latest_name, 'wb') as file :
        ftp.retrbinary('RETR %s' % latest_name, file.write)
        file.close()
        #ftp.rename(latest_name, f'/order_payment_confirm_since_last_two_month_report/archive/{latest_name}')
        ftp.quit()
        os.rename(f'{latest_name}', 'Feed.csv')
        print(f"File {latest_name} downloaded and renamed to Feed.csv")
except Exception as e:
    print (str(e))
