import csv, json
import pandas as pd
import os
from  datetime import date,datetime,timedelta

#Defining variables
current_time = datetime.now()  
current_time = current_time.strftime("%H%M%S")

#Excel path and grooming data, with a temp csv. Since its easy to convert csv to json
excelpath = 'Final ver 2.0.xlsx'
df = pd.read_excel("Final ver 2.0.xlsx",engine='openpyxl')
print(df)
df['channelname'] = df['channelname'].astype(str).str.replace(' ', '')
df['channelname'] = df['channelname'].astype(str).str.replace('nan', ' ')
df.to_csv('csvfile.csv',index=False)

jsonpath_kiosk = f'demo{current_time}.json'

print(df)
j = df.groupby(['customernumber'])[['macaddress']]\
.apply(lambda x: x.set_index('macaddress').to_dict(orient='index')).to_dict()

json_kiosk = json.dumps(j)
f = open(jsonpath_kiosk,'w')
f.write(json_kiosk)
f.close()
os.remove('csvfile.csv')
