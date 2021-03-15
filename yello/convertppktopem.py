import pysftp

def upload_file(file_path):

    private_key = "private_keyname_20191701.pem"  # can use password keyword in Connection instead
    srv = pysftp.Connection(host="ftp.brodos.net", username="yello", private_key=private_key)
    srv.chdir('/yello')  # change directory on remote server
    srv.put(file_path)  # To download a file, replace put with get
    srv.close()  # Close connection

upload_file("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Yello/xlsxcopies/PRL Yello.csv")
