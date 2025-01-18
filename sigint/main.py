import signal
import time
import sys

# Outputā kaut kas mēdz neiet ar garum/mīkstinājuma zīmēm
sys.stdout.reconfigure(encoding="utf-8")

#CTRL+C ievade, kas skaisti pārtrauc koda darbību
def shutdown(sig, frame):
    print("Ctrl+c strādā")
    exit(0)

signal.signal(signal.SIGINT, shutdown)

print("Ctrl+c, lai izietu")

#Cikls, kas darbina kodu līdz to izslēdz vai tiek saņemts CTRL+C
try:
    while True:
        print("Strādā...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Ja šis parādās, tad kaut kas nav pareizi!")