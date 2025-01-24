import os
import time
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


def list_files_hierarchically(directory, indent=0):
    
    for entry in os.scandir(directory):
        print("-" * indent + entry.name)
        if entry.is_dir(follow_symlinks=False):
            list_files_hierarchically(entry.path, indent + 1)
        else:
            print_file_stats(entry.path, indent)

def print_file_stats(filepath, indent):

    try:
        stats = os.stat(filepath)
        size = stats.st_size
        ctime = time.ctime(stats.st_ctime)
        mtime = time.ctime(stats.st_mtime)
        #Ja ķepiņās pamaina zīmi, tas pamaina indent izskatu, smukāk vispār bija ar atstarpēm un | zīmi
        print(" " * indent + f"[Faila izmērs: {size}")
        print(" " * indent + f"Izveidots: {ctime}")
        print(" " * indent + f"Mainīts: {mtime}]")
    except FileNotFoundError:
        logging.error("-" * indent + "Fails nav atrasts")
    except PermissionError:
        logging.critical("-" * indent + "Pieeja liegta")

#Šeit path uz directory
root_directory = "C:\\Users\\User\\Documents\\GitHub\\ki_pitona_darbi\\threading"

if os.path.isdir(root_directory):
    print(f"Faili '{root_directory}':")
    list_files_hierarchically(root_directory)
else:
    logging.error(f"Error: '{root_directory}' Windows ir nolādēts :) .")
