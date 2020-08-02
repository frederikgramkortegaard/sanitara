""" """

import csv
from collections import defaultdict 


# Load Pornography url data into lookup table
pornography_lookup_table = defaultdict(int)

print(f"loading pornography_url_lookup_table: from ./data/pornography_url_data.csv")
with open('./data/pornography_url_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    
    # skip labels
    reader.__next__()
    for row in reader:
        if row != []:
            pornography_lookup_table[row[0]] = 1
    
# Load Phishing url data into lookup table
phishing_lookup_table = defaultdict(int)

print(f"loading phishing_url_lookup_table: from ./data/phishing_url_data.csv")
with open('./data/phishing_url_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    
    # skip labels
    reader.__next__()
    for row in reader:
        if row != []:
           phishing_lookup_table[row[0]] = 1
    

index_of_lookup_tables = defaultdict(int) 
index_of_lookup_tables["pornography"] = pornography_lookup_table
index_of_lookup_tables["phishing"] = phishing_lookup_table