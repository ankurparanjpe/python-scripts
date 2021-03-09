import ftplib
from  datetime import date
# Open the FTP connection
ftp = ftplib.FTP("ftp.brodos.net")
ftp.login("all4you", "GSUnMmew9gsQSYLVEq8l")
ftp.cwd('/Tracking/Archive')
today = date.today().strftime('%Y%m%d')
print (today)


filenames = ftp.nlst("all4you_tracking_"+str(today)+"*.csv")
print(list(filenames))

try:
    for filename in filenames:
        with open( filename, 'wb') as file :
            ftp.retrbinary('RETR %s' % filename, file.write)
            file.close()
            #ftp.rename('/Tracking/Archive/'+str(filename),'/Tracking/all4you'+str(today)+'.csv')
            ftp.quit()

except Exception as e:
    print (str(e))
