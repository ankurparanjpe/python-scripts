import glob
import shutil
import os
dest_dir = "I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/komsa/mailparser done"
for file in glob.glob(r'I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/komsa/*.xlsx'):
    print(file)
    shutil.move(file, dest_dir)

