import glob
import shutil
import os
dest_dir = "I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland/mail parser done"
f = os.listdir('I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland')


for file in glob.glob('*.csv'):
    print(file)
    full_dest = f'I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/macland/mail parser done/{file}'
    print(full_dest)
    
    shutil.move(file, full_dest)


