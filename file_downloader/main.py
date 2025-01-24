import urllib.request
import signal
import sys
import logging

# Outputā kaut kas mēdz neiet ar garum/mīkstinājuma zīmēm
sys.stdout.reconfigure(encoding='utf-8')

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

def shutdown(sig, frame):
    logging.warning("Faila lejupielāde apturēta")
    exit(0)

signal.signal(signal.SIGINT, shutdown)

def show_progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    percentage = (downloaded * 100) / total_size
    logging.info(f"Lejupielādē: {percentage:.1f}%")

# Saites ievade 
url = input("Lejupielādes saite: ")

# Lietotājs var nosaukt failu, kas lejupielādējams
filename = input("Nosauc lejupielādējamo falilu: ")

logging.info("Sāk lejupielādi...")
logging.info("Ctrl+c, lai apturētu lejupielādi")
urllib.request.urlretrieve(url, filename, show_progress)
logging.info("\nPabeigts!")