import glob

with open("mixed file/consolidated.csv", "w") as f:
    for ff in glob.glob("*.csv"):
        with open(ff) as fff:
            next(fff)
            f.write(fff.read())
