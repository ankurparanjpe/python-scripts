import string
import fnmatch
import os

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\r'


for file_path in os.listdir('I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland'):
    if fnmatch.fnmatch(file_path, 'maclandgmbh_*.csv'):
        print(file_path)
        with open(file_path, 'rb') as open_file:
            content = open_file.read()

            content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

        with open(file_path, 'wb') as open_file:
            open_file.write(content)
