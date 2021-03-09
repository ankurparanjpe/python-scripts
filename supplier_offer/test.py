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

df2.append(df3, ignore_index = True)
df4 = df2.drop_duplicates(subset=['ean'],keep='first')
print(df4)


