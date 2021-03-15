import ftplib
import fnmatch
import os

ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("macland", "bsyGfvjqWpbalyK")
ftp.cwd('/tracking/converted')

for file_path in os.listdir('I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland'):
    if fnmatch.fnmatch(file_path, '*.csv'):
        with open(file_path,'rb') as file:                 # file to send
            ftp.storbinary('STOR %s' %file_path, file)
            print(file_path)

file.close()                                    # close file and FTP
ftp.quit()
