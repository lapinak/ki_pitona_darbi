### FTP parser uzdevums

FTP saites tiek iekļautas koda sākumā, sarakstā. Tiek izdrukāti pirmie 5 faili no katras saites, ja tādi ir atrasti, un izveidoti 3 threads darbības veikšanai. Piemērs terminālī:

```bash
2025-01-24 20:37:23,786 - INFO - Thread-1 Pārbauda ftp.dlptest.com
2025-01-24 20:37:23,787 - INFO - Thread-2 Pārbauda speedtest.tele2.net
2025-01-24 20:37:23,788 - INFO - Thread-3 Pārbauda ftp.ubuntu.com
2025-01-24 20:37:24,281 - INFO - 
Thread-3 Pabeidza ftp.ubuntu.com:
  drwxr-xr-x    7 998      998          4096 Jan 24 17:42 ubuntu
2025-01-24 20:37:24,328 - INFO - Thread-3 Pārbauda ftp.gnu.org
2025-01-24 20:37:24,865 - ERROR - 
Thread-2 error speedtest.tele2.net: 530 Permission denied.
2025-01-24 20:37:24,867 - INFO - Thread-2 Pārbauda ftp.mozilla.org
2025-01-24 20:37:25,286 - INFO - 
Thread-3 Pabeidza ftp.gnu.org:
  lrwxrwxrwx    1 0        0               8 Aug 20  2004 CRYPTO.README -> .message
  -rw-r--r--    1 0        0           17864 Oct 23  2003 MISSING-FILES
  -rw-r--r--    1 0        0            4178 Aug 13  2003 MISSING-FILES.README
  -rw-r--r--    1 0        0            2748 May 23  2023 README
  -rw-r--r--    1 0        0          405121 Oct 23  2003 before-2003-08-01.md5sums.asc
2025-01-24 20:37:25,402 - INFO - Thread-3 Pārbauda ftp.funet.fi
2025-01-24 20:37:25,919 - INFO - 
Thread-3 Pabeidza ftp.funet.fi:
  lrwxrwxrwx    1 0          0                  17 Jun 18  2019 README -> /pub/files/README
  lrwxrwxrwx    1 0          0                  25 Feb 26  2024 README.PRIVACY -> /pub/files/README.PRIVACY
  drwxr-xr-x    2 0          0                 125 Dec  7  2015 dev
  -rw-r--r--    1 108        42                318 May 31  2007 favicon.ico
  lrwxrwxrwx    1 0          0                  16 Jun 18  2019 index -> /pub/files/index
2025-01-24 20:37:25,949 - INFO - Thread-3 Pārbauda ftp.sunet.se
2025-01-24 20:37:26,310 - INFO - 
```

Log faila izraksts saglabāts pie failiem.