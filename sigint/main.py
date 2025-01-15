import signal
import time

def shutdown(sig, frame):
    print('\nSignal received. Exiting gracefully...')
    exit(0)

# Try commenting out this line to see the KeyboardInterrupt exception
signal.signal(signal.SIGINT, shutdown)

print('Running... Press Ctrl+C to exit')

try:
    while True:
        print('Working...')
        time.sleep(1)
except KeyboardInterrupt:
    print('\nKeyboardInterrupt exception caught! Program crashed!')