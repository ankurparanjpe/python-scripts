import csv, json

csvpath = "orders.csv"
jsonpath = "converted.json"

with open(csvpath, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    with open(jsonpath, 'w') as json_file:
        json_file.write('[')
        for row in reader:
            json_file.write(json.dumps(row) + ',\n')
        json_file.write(']')
"""
data = {}

with open(csvpath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        orderNo = csvRow["orderNo"]
        data[orderNo] = csvRow

with open(jsonpath, "w") as jsonFile:
    jsonFile.write(json.dumps(data) + "\n")

print(f"csv is converted to json format.\nHere is the format {data}")
"""
