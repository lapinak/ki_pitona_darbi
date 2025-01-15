import re

faila_lokacija = ""
regex = r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+\S+\s+\S+:\s+(?:\[\s*\d+\.\d+\]\s+)?(.+)'

with open(faila_lokacija, 'r') as file:
    [print(re.findall(regex, line)) for line in file if 'USB' in line]

file.close()