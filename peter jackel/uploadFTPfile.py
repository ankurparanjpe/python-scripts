import ftplib
from  datetime import date
import glob, os


ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("packagetrkprod", "Jhnwfw2xjpf")
ftp.cwd('/upload')

filenames = glob.glob('*.csv')

print (filenames)

for filename in filenames:
    with open(filename, 'rb') as file:
        ftp.storbinary('STOR %s' % filename, file)
        file.close()
      

for file in filenames:
    with open(file, 'rb') as f:
        ftp.storbinary('STOR %s' % file+'.done', f)
        f.close()
            
ftp.quit()
