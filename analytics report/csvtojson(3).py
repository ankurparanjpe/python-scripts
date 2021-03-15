import csv, json
import pandas as pd

#for kiosk
csvpath_kiosk = "consolidated_kiosk.csv"
jsonpath_kiosk = "sales_analytics_report_combine_kiosk.json"


df = pd.read_csv(csvpath_kiosk)

j = df.groupby(['store_id'])[['Date and Time','totalamount', 'totalorder', 'totalqty']]\
.apply(lambda x: x.set_index('Date and Time').to_dict(orient='index')).to_dict()

json_kiosk = json.dumps(j)
f = open(jsonpath_kiosk,'w')
f.write(json_kiosk)
f.close()

#for os
csvpath_os = "consolidated_os.csv"
jsonpath_os = "sales_analytics_report_combine_os.json"


df1 = pd.read_csv(csvpath_os)

k = df1.groupby(['store_id'])[['Date and Time','totalamount', 'totalorder', 'totalqty']]\
.apply(lambda x: x.set_index('Date and Time').to_dict(orient='index')).to_dict()

json_os = json.dumps(k)
ff = open(jsonpath_os,'w')
ff.write(json_os)
ff.close()
