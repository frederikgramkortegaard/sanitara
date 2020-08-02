import re
import csv

pattern = re.compile("^(?:www\.)?([a-zA-Z0-9-]*)(?=\.|\b)")
    
# deleted the scraping code and formatting code

with open('./phishing_url_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    
    with open("./tmp.csv", 'w') as v:

        # skip labels
        reader.__next__()
        for row in reader:
            row = row[1]
            if row.startswith('"'):
                v.write(row[1:] + "\n")
            else:
                v.write(row + "\n")