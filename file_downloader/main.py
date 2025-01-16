import urllib.request
import signal
import sys

# Outputā kaut kas mēdz neiet ar garum/mīkstinājuma zīmēm
sys.stdout.reconfigure(encoding='utf-8')

def shutdown(sig, frame):
    print("Faila lejupielāde apturēta")
    exit(0)

signal.signal(signal.SIGINT, shutdown)

def show_progress(block_num, block_size, total_size):
    downloaded = block_num * block_size
    percentage = (downloaded * 100) / total_size
    print(f"Lejupielādē: {percentage:.1f}%", end='\r')

# Saites ievade 
url = input("Lejupielādes saite: ")

# Lietotājs var nosaukt failu, kas lejupielādējams
filename = input("Nosauc lejupielādējamo falilu: ")

print("Sāk lejupielādi...")
print("Ctrl+c, lai apturētu lejupielādi")
urllib.request.urlretrieve(url, filename, show_progress)
print("\nPabeigts!")