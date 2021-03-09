import os
import datetime
import glob
import shutil
import fnmatch
today = datetime.date.today().strftime('%Y%m%d')
os.rename(f'all4you_tracking_{today}.csv', f'done/all4you_tracking_{today}.csv')

