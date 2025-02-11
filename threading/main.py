import os
import threading
import pandas as pd
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

compiled = []
lock = threading.Lock()

def process_excel(file_path):

    try:
        # Lasa Excel failu
        start_time = time.time()
        dataset = pd.read_excel(file_path)
        
        # Izvelk kolonnas ar vārdu, uzvārdu un iestādes nosaukumu, jo tas nepieciešams galvenajā failā. 
        processed_dataset = dataset[["Vārds Uzvārds", "Iestādes nosaukums"]]
        
        with lock:
            compiled.append(processed_dataset)
            end_time = time.time()
            avg_time = end_time - start_time
            logging.info(f"Thread pabeigts {avg_time:.3f} sekundēs")
    except Exception as e:
        logging.error(f"Kļūda velkot globālo sarakstu {file_path}: {e}")

def main(input_dir, output_file):

    #Salasa failus no mapītes
    excel_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    if not excel_files:
        logging.warning("Tukša mape")
        return

    threads = []
    for file_path in excel_files:
        thread = threading.Thread(target=process_excel, args=(file_path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    combined_dataset = pd.concat(compiled, ignore_index=True)

    # Saglabā gala Excelī
    combined_dataset.to_excel(output_file, index=False)
    logging.info("Excel fails sagatavots")

#Jānorāda avota mapīte un gala fails
if __name__ == "__main__":
    input_directory = ""
    output_file = "apvienots_saraksts.xlsx"
    main(input_directory, output_file)
