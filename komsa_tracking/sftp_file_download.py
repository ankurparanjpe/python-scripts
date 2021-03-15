import pysftp
from datetime import datetime
import paramiko
import fnmatch

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
today = datetime.today().strftime('%Y-%m-%d')
sftp = pysftp.Connection("ftp.komsa.de", username="brodos", password="UxPK1ue0", cnopts=cnopts)

sftp.cwd('/brodos/OUT/')
filelist = sftp.listdir()
print(filelist)
print (today)

for file in filelist:
        if fnmatch.fnmatch(file, f"*_Brodos_Auslieferungen.xlsx"):
                print(file)
                sftp.get(file)
                sftp.rename(file,f'/brodos/OUT/done/{file}')
                sftp.close()
