import glob
import shutil
import os
dest_dir = "I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/strax/mail parser done"
for file in glob.glob(r'I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/strax/*.csv'):
    print(file)
    shutil.move(file, dest_dir)

