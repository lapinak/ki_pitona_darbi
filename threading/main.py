import os
import threading
import pandas as pd
import time
import sys

# Outputā kaut kas mēdz neiet ar garum/mīkstinājuma zīmēm
sys.stdout.reconfigure(encoding='utf-8')

compiled = []
lock = threading.Lock()

def process_excel(file_path):

    try:
        # Lasa Excel failu
        start_time = time.time()
        dataset = pd.read_excel(file_path)
        
        # Izvelk kolonnas ar vārdu, uzvārdu un iestādes nosaukumu, jo tas nepieciešams galvenajā failā. 
        processed_dataset = dataset[['Vārds Uzvārds', 'Iestādes nosaukums']]
        
        with lock:
            compiled.append(processed_dataset)
            end_time = time.time()
            avg_time = end_time - start_time
            print(f"Diegs izbeidzās {avg_time:.3f} sekundēs")
    except Exception as e:
        print(f"Kļūda velkot globālo sarakstu {file_path}: {e}")

def main(input_dir, output_file):

    # Nākamreiz izdomā kaut ko vienkāršāku man nestrādā
    #Salas failus no mapītes
    excel_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]

    if not excel_files:
        print("Tukša mape")
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
    print("Excel faili gatavi")

#Jānorāda avota mapīte un gala fails
if __name__ == "__main__":
    input_directory = ""
    output_file = ""
    main(input_directory, output_file)
