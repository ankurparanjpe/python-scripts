import ftplib
from  datetime import date
# Open the FTP connection
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("packagetrkprod", "Jhnwfw2xjpf")
ftp.cwd('/upload')

filenames = ftp.nlst("*.csv")
print(list(filenames))

ftp.retrbinary('STOR ankur.done')
file.close()
ftp.quit()


