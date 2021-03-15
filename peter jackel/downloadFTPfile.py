import ftplib
from  datetime import date
# Open the FTP connection
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("mplieferanten", "bv5Fe38Nder4")
ftp.cwd('/PeterJaeckel/tracking')
today = date.today().strftime('%Y%m%d')
print (today)


filenames = ftp.nlst("*.csv")
print(list(filenames))

try:
    for filename in filenames:
        with open( filename, 'wb') as file :
            ftp.retrbinary('RETR %s' % filename, file.write)
            file.close()
            #ftp.rename('/Tracking/Archive/'+str(filename),'/Tracking/all4you'+str(today)+'.csv')
            ftp.rename(filename, f'archive/{filename}')

    ftp.close()
            
except Exception as e:
    print (str(e))

