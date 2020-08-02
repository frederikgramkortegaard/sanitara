""" """

import csv
from collections import defaultdict 

index_of_lookup_tables = defaultdict(int) 

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
    
index_of_lookup_tables["pornography"] = pornography_lookup_table

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
    
index_of_lookup_tables["phishing"] = phishing_lookup_table

# Load Blacklist data into lookup table
blacklist_lookup_table = defaultdict(int)

print(f"loading blacklist lookup table: from ./data/blacklist.csv")
with open('./data/blacklist.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        if row != []:
           blacklist_lookup_table[row[0]] = 1

index_of_lookup_tables["blacklist"] = blacklist_lookup_table

# Load Whitelist data into lookup table
whitelist_lookup_table = defaultdict(int)

print(f"loading whitelist lookup table: from ./data/whitelist.csv")
with open('./data/whitelist.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for row in reader:
        if row != []:
           whitelist_lookup_table[row[0]] = 1

index_of_lookup_tables["whitelist"] = whitelist_lookup_table