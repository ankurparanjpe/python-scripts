import csv
import time
import pandas as pd
import numpy as np
import requests
import zipfile
import locale
import os
from babel.numbers import format_decimal
from datetime import datetime
import glob


start_time = time.time()
current_time = datetime.now()
current_time = current_time.strftime("%d%m%Y%H%M%S")
epoch_time = int(time.time())

#Downloading the file from URL
url = 'https://service.jacob.de/content/csvTool/BrodosSmall.zip'
r = requests.get(url, allow_redirects=True)
open('zipfile.rar', 'wb').write(r.content)

#Unzipping to location
with zipfile.ZipFile('D:/python scripts/supplier_offer/zipfile.rar', 'r') as zip_ref:
    zip_ref.extractall('D:/python scripts/supplier_offer')
time.sleep(3)

#Creating a csv
with open('BrodosSmall.txt',newline='') as f:
    r = csv.reader(f,delimiter='\t')
    data = [line for line in r]
    for l in data:
        l[4] = l[4].capitalize()
with open('abc.csv','w',newline='') as f:
    w = csv.writer(f, delimiter=',',escapechar='"')
    w.writerows(data)

#working on csv for different filters
df = pd.read_csv("abc.csv",low_memory=False)
df.columns = df.columns.str.lower()

df.dropna(inplace=True)

df.query('price > 0 and price < 7500', inplace=True)

df.query('quantity >= 1', inplace=True)

df['price'] = df['price'].astype(str).str.replace('.',',')

df = df.rename(columns={'delivery time': 'delivery-time-min_1'})

df.query('`delivery-time-min_1` >= 1' and '`delivery-time-min_1` < 5', inplace=True)

num = df['product-id'].astype(str).str.isnumeric()
df = df.loc[num]

df['product-id'] = df['product-id'].apply(lambda x: x.lstrip('0'))
#df['product-id'] = df['product-id'].apply(lambda x: '{:.0f}'.format(x))

df['product-id'] = df['product-id'].astype('str')

mask = (df['product-id'].str.len() > 7) & (df['product-id'].str.len() < 14)
df = df.loc[mask]
df.drop_duplicates(subset=['product-id'],keep=False,inplace=True)
print(df)




#blacklisted items are removed here
df5 = pd.read_csv('Blacklist_EAN_Jacob.csv')
df5.drop(columns=['SupplierID','SystemID'], inplace=True)
df5.drop_duplicates(subset=['EAN'],keep='first',inplace=True)
df['product-id'] = df['product-id'].astype(float)
df5['EAN'] = df5['EAN'].astype(float)

df = pd.merge(df,df5, left_on="product-id", right_on="EAN", how = 'outer', indicator=True).query('_merge=="left_only"').drop('_merge', axis=1)
     


#Grroming and merging active and inactive
df2 = pd.read_csv('Active_article/Active_articles.csv')

df3 = pd.read_csv('Active_article/Inactive_articles.csv', sep=';',low_memory=False)
df2.drop(columns=['ARTICLEID', 'ARTICLENUMBER', 'ARTICLENAME', 'PRODUCTCODE'], inplace=True)
print(df2)

df3.drop(columns=['DESCRIPTION', 'VO', 'VOTEXT', 'VALIDFROM', 'VALIDTO'], inplace=True)
print(df3)

num1 = df3['CUSTOMERNO'].astype(str).str.isnumeric()
df3 = df3.loc[num1]
df2['EAN'] = df2['EAN'].astype(float)
df3['CUSTOMERNO'] = df3['CUSTOMERNO'].astype(float)


df2.rename(columns={"EAN": "ean"}, inplace=True)
df3.rename(columns={"CUSTOMERNO": "ean"}, inplace=True)

df4 = df2.append(df3, ignore_index = True)
df4.drop_duplicates(subset=['ean'],keep='last',inplace=True)
print(df4)



#Comparing active/inactive article with our dataframe
df['product-id'] = df['product-id'].astype(float)
df4['ean'] = df4['ean'].astype(float)

final = pd.merge(df,df4, left_on="product-id", right_on="ean", how = 'inner')
final.drop(columns=['ean'], inplace=True)
final['product-id'] = final['product-id'].apply(lambda x: '{:.0f}'.format(x))

print (final)



#Inserting required cols
final.insert(4, 'product-tax-code', 16)
final.insert(5, 'product-id-type', 'EAN')
final.insert(7, 'currency', 'EUR')
final.insert(8, 'minimum_order_quantity', 1)
final.insert(9, 'evp', '')
final.insert(10, 'shipping-charge', '<li>zzgl. 3,00€ Versand pro<br>Bestellung<li>ab 999,99€ Bestellwert<br>versandkostenfrei<li>Lieferzeit 3 Werktage')
final.insert(11, 'shipping-charge_1' , '3,00')
final.insert(12, 'shipping-charge-free_1', '999,99')
final.insert(13, 'shipping-kind_1',1)
final.insert(15, 'delivery-time-max_1', 3)
#df.insert(15, 'shipping-charge-alternative_1','')
#df.insert(16, 'shipping-charge-alternative-value_1','')
final = final[['sku','price','product-id','quantity','product-tax-code','product-id-type','condition-type','shipping-charge','currency','minimum_order_quantity','evp','shipping-charge_1','shipping-charge-free_1','shipping-kind_1','delivery-time-min_1','delivery-time-max_1']]
final.to_csv('Jacob_output.csv',sep=',', index=False)



#Inserting Headers
with open('Jacob_output.csv',newline='') as f:
    r = csv.reader(f,delimiter=',')
    data = [line for line in r]
with open('Jacob_output.csv','w',newline='') as f:
    w = csv.writer(f, delimiter=',',escapechar='"')
    f.writelines(['"Header Start"' + "\n"])
    f.writelines(['"supplierid:193519330"' + "\n"])
    f.writelines([f'"startdate:{epoch_time}123"' + "\n"])
    f.writelines(['"days:365"' + "\n"])
    f.writelines(['"overwrite:No"' + "\n"])
    f.writelines(['"supplierName:Jacob Elektronik GmbH"' + "\n"])
    f.writelines(['"supplierEmailId:kabbara@jacob-elektronik.de"' + "\n"])
    f.writelines(['"fileSource:FTP"' + "\n"])
    f.writelines(['"offerExpiryNotificationTime:72"' + "\n"])
    f.writelines(['"Header End"' + "\n"])
    w.writerows(data)


os.remove("abc.csv")

zipfile = glob.glob('zipfile.rar')[0]
os.rename('./{}'.format(zipfile), f'Supplier_input_files/zipfile_{current_time}.rar')
filename = glob.glob('Jacob_output*.csv')[0]
os.rename('./{}'.format(filename), f'Output_files/Jacob_output_{current_time}.csv')


print("--- %s seconds ---" % (time.time() - start_time))
input()



