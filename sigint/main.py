import signal
import time
import sys
import logging

# Outputā kaut kas mēdz neiet ar garum/mīkstinājuma zīmēm
sys.stdout.reconfigure(encoding="utf-8")

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

#CTRL+C ievade, kas skaisti pārtrauc koda darbību
def shutdown(sig, frame):
    logging.warning("Ctrl+c strādā, programmu apstādināja lietotājs")
    exit(0)

signal.signal(signal.SIGINT, shutdown)

logging.info("Ctrl+c, lai izietu")

#Cikls, kas darbina kodu līdz to izslēdz vai tiek saņemts CTRL+C
try:
    while True:
        logging.info("Strādā...")
        time.sleep(1)
except KeyboardInterrupt:
    logging.error("Ja šis parādās, tad kaut kas nav pareizi!")