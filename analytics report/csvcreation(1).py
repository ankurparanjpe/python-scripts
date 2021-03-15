import csv, json
import pandas as pd
from datetime import datetime
import os
import glob

current_time = datetime.now()
current_time = current_time.strftime("%d%m%Y%H%M%S")
df = pd.read_excel('reporting.xlsx', 'kiosk')
print(df)
df.to_csv(f'csv_files_kiosk/sales_analytics_report_kiosk_{current_time}.csv', header=None, index = False)

df1 = pd.read_excel('reporting.xlsx', 'OS')
print(df1)
df1.to_csv(f'csv_files_os/sales_analytics_report_os_{current_time}.csv', header=None, index = False)
input()
