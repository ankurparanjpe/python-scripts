import csv, json
import pandas as pd
import os
from  datetime import date,datetime,timedelta

#Defining variables
current_time = datetime.now()  
current_time = current_time.strftime("%H%M%S")

#Excel path and grooming data, with a temp csv. Since its easy to convert csv to json
excelpath = 'Final ver 2.0.xlsx'
df = pd.read_excel("Final ver 2.0.xlsx")
print(df)
df['channelname'] = df['channelname'].astype(str).str.replace(' ', '')
df['channelname'] = df['channelname'].astype(str).str.replace('nan', ' ')
df.to_csv('csvfile.csv',index=False)


#Creating a json data
data = {}
def make_json(csvFilePath, jsonFilePath):

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            
            key = rows['macaddress']
            data[key] = rows
            

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
csvFilePath = r'csvfile.csv'
jsonFilePath = f'mystore_tv_{current_time}.json'

make_json(csvFilePath, jsonFilePath)

#Removing unwanted key, values and creating final dict
for key in data:
    data[key].pop('customernumber', None)
    data[key].pop('macaddress', None)


with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))

#Removing temp csv file
os.remove('csvfile.csv')
