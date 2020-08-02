import re
import csv

pattern = re.compile("^(?:www\.)?([a-zA-Z0-9-]*)(?=\.|\b)")
    
# deleted the scraping code and formatting code

with open("pornography_url_data.csv", 'r') as v:
    lines = 0
    for _ in v.readlines():
        lines += 1
    print(lines)