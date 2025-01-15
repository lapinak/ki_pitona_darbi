import re

faila_lokacija = ""
regex = r'\bJan\s\d{1,2}\s\d{2}:\d{2}:\d{2}\b'

with open(faila_lokacija, 'r') as file:
    [print(re.findall(regex, line)) for line in file if 'USB' in line]

file.close()