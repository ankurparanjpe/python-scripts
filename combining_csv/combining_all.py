from os import chdir
from glob import glob
import pandas as pdlib

# List all CSV files in the working dir
list_of_files = [file for file in glob('*.csv')]
print(list_of_files)

# Move to the path that holds our CSV files
csv_file_path = 'D:/python scripts/combining_csv/'
chdir(csv_file_path)


# Produce a single CSV after combining all files
def produceOneCSV(list_of_files, file_out):
   # Consolidate all CSV files into one object
   result_obj = pdlib.concat([pdlib.read_csv(file) for file in list_of_files], sort=False, axis=1)
   # Convert the above object into a csv file and export
   
   result_obj.to_csv(file_out, index=False, encoding="utf-8")

file_out = "ConsolidateOutput.csv"
produceOneCSV(list_of_files, file_out)




"""
os.chdir("I:\Abteilungen\Storeship\Public\Bestellungen\Tracking Process for Telekom\MP supplier mail\strax")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ], sort=False)

combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')



path = r'I:/Abteilungen/Storeship/Public/Bestellungen/Tracking Process for Telekom/MP supplier mail/strax' # use your path

all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:

    df = pd.read_csv(filename, index_col=None, header=0)

    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True, sort=False)
frame = frame.to_csv('allfile.csv')
print (frame)
"""
