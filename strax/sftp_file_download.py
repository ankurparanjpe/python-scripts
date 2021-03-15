import pysftp
from datetime import datetime
import paramiko
import fnmatch

today = datetime.today().strftime('%Y-%m-%d')
sftp = pysftp.Connection("ftp.brodos.net", username="strax", password="HiAqgldlpOjg")

sftp.cwd('/strax/tracking')
filelist = sftp.listdir()
print(filelist)
print (today)

for file in filelist:
        if fnmatch.fnmatch(file, f"brodos_*.csv"):
                print(file)
                sftp.get(file)
                sftp.rename(file,f'/strax/tracking/Archive/{file}')

sftp.close()
