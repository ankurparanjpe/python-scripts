import pandas as pd
from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y')

df = pd.read_excel("D:/python scripts/download_mailattachment/Brodos taegliche LS Liste mit UPS NR (133601).xlsx")
df = df[df.columns[0:5]]
df.to_csv(f'Peter Jackel {today}.csv')
print (df)

