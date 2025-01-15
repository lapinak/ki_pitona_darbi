import signal
import time

def shutdown(sig, frame):
    print('Signal received. Exiting gracefully...')
    exit(0)

signal.signal(signal.SIGINT, shutdown)

print('Running... Press Ctrl+C to exit')

try:
    while True:
        print('Working...')
        time.sleep(1)
except KeyboardInterrupt:
    print('Exception caught! Program crashed!')