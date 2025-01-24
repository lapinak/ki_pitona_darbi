from scapy.all import *
#from scapy.layers.inet import IP, TCP
import multiprocessing
import signal
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

#Lai var pārtraukt programmu
def shutdown(sig, frame):
    logging.info("Pārtraukts ar lietotāja ievadi")
    exit(0)

signal.signal(signal.SIGINT, shutdown)

def port_scanning(ip_address, port):

    conf.verb = 0
    
    #TCP SYN portu skenēšanai
    syn_packet = IP(dst=ip_address)/TCP(sport=RandShort(), dport=port, flags="S")
    
    try:
        logging.info(f"Scanning port {port} on {ip_address}")
        #Gaida atbildi par nosūtīto pakotni
        response = sr1(syn_packet, timeout=2, verbose=False)
        
        #Iegūtās atbildes 0x12 - atvērts ports, 0x14 - aizvērts ports
        if response and response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                logging.info(f"Ports {port} strādā")
            elif response.getlayer(TCP).flags == 0x14:
                logging.info(f"Ports {port} ir aizvērts")     
        else:
            logging.info(f"Ports {port} neatbild.")
    except Exception as e:
        logging.error(f"Kļūda ar portu {port}: {e}")

def scan(ip_address, port_range):
    
    #Pool, lai var veidot 4 procesus, kas paralēli skenē portus
    pool = multiprocessing.Pool(processes=4)
    scan_args = [(ip_address, port) for port in port_range]
    pool.starmap(port_scanning, scan_args)
    pool.close()
    pool.join()

if __name__ == "__main__":
    #IP adrese, kuru skenē un portu diapazons
    ip_address = "" 
    port_range = range(20, 500) 
    
    scan(ip_address, port_range)
    logging.info("Uzd.pabeigts")