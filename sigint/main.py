import signal
import time

def shutdown(sig, frame):
    print('Ctrl+c strādā')
    exit(0)

signal.signal(signal.SIGINT, shutdown)

print('Ctrl+c, lai izietu')

try:
    while True:
        print('Strādā...')
        time.sleep(1)
except KeyboardInterrupt:
    print('Ja šis parādās, tad kaut kas nav pareizi!')