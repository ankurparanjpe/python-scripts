import glob
import pandas as pd

with open("consolidated_kiosk.csv", "w") as f:
    for ff in glob.glob("csv_files_kiosk/*.csv"):
        with open(ff) as fff:
            f.write(fff.read())

df = pd.read_csv("consolidated_kiosk.csv")

df.to_csv("consolidated_kiosk.csv", header=["store_id","Date and Time","totalamount","totalorder","totalqty"], index=False)



with open("consolidated_os.csv", "w") as f1:
    for ff1 in glob.glob("csv_files_os/*.csv"):
        with open(ff1) as fff1:
            f1.write(fff1.read())

df1 = pd.read_csv("consolidated_os.csv")

df1.to_csv("consolidated_os.csv", header=["store_id","Date and Time","totalamount","totalorder","totalqty"], index=False)
