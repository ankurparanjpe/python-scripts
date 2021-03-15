import ftplib
from  datetime import date
# Open the FTP connection
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("macland", "bsyGfvjqWpbalyK")
ftp.cwd('/tracking')
today = date.today().strftime('%Y%m%d')
print (today)


filenames = ftp.nlst("maclandgmbh_*.csv")
print(list(filenames))


try:
    for filename in filenames:
        with open(filename, 'wb') as file :
            ftp.retrbinary('RETR %s' % filename, file.write)
            file.close()
            
            ftp.rename(filename, f'/tracking/.processed/{filename}')
    ftp.quit()
            
except Exception as e:
    print (str(e))

