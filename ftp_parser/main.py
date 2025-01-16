import threading
import ftplib
import queue

sites = [
    "ftp.dlptest.com",
    "speedtest.tele2.net",
    "ftp.ubuntu.com",
    "ftp.gnu.org",
    "ftp.mozilla.org",
    "ftp.funet.fi",
    "ftp.sunet.se",
    "ftp.freebsd.org",
    "ftp.debian.org",   
    "ftp.tu-chemnitz.de"
]

def check_ftp(work_queue, results):
    while True:
        try:
            site = work_queue.get(timeout=1) 
        except queue.Empty:
            break

        thread_name = threading.current_thread().name
        print(f"{thread_name} Pārbauda {site}")

        try:
            ftp = ftplib.FTP()
            ftp.connect(site, timeout=10)
            ftp.login() 
            
            files = []
            def handle_line(line):
                if len(files) < 5:
                    files.append(line)
            ftp.retrlines('LIST', handle_line)
            
            top_files = files[:5]
            results[site] = top_files

            print(f"\n{thread_name} Pabeidza {site}:")
            for file in top_files:
                print(f"  {file}")

            ftp.quit()
            
        except Exception as e:
            results[site] = f"Error: {e}"
            print(f"\n{thread_name} error {site}: {e}")


work_queue = queue.Queue()
results = {}

for site in sites:
    work_queue.put(site)

threads = []
for i in range(3):
    t = threading.Thread(target=check_ftp, args=(work_queue, results), name=f"Thread-{i+1}")
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nVajadzētu būt, ka viss")