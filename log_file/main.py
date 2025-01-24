import re
import logging

# Logging konfigurācija
logging.basicConfig(
    # INFO līmenis
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        #Pieglabā failā, lai izskatās 'nopietnāk'
        logging.FileHandler("processing.log", mode="w", encoding="utf-8"),
        #Konsoles izdrula
        logging.StreamHandler()
    ]
)

faila_lokacija = "testfile.txt"
#Regex, lai sadalītu rindiņu pēc timestamp
regex = r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+\S+\s+\S+:\s+(?:\[\s*\d+\.\d+\]\s+)?(.+)'

#Atver failu, lasa katru rindiņu un meklē "USB"
with open(faila_lokacija, 'r') as file:
    [logging.info(re.findall(regex, line)) for line in file if "USB" in line]

file.close()