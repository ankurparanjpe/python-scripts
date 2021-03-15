import glob
import shutil
import os
from datetime import date

today = date.today().strftime('%Y%m%d')
dest_dir = "I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/peter jackel/archieve/"

filenames = glob.glob('*.csv')
for file in filenames:
    print(file)
    shutil.move(file, f'{dest_dir}{today}{file}')

