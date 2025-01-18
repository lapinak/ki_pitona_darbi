### FTP parser uzdevums

FTP saites tiek iekļautas koda sākumā, sarakstā. Tiek izdrukāti pirmie 5 faili no katras saites, ja tādi ir atrasti, un izveidoti 3 threads darbības veikšanai. Piemērs terminālī:

```bash
Thread-1 Pārbauda ftp.dlptest.com
Thread-2 Pārbauda speedtest.tele2.net
Thread-3 Pārbauda ftp.ubuntu.com

Thread-3 Pabeidza ftp.ubuntu.com:
  drwxr-xr-x    7 998      998          4096 Jan 18 16:52 ubuntu
Thread-3 Pārbauda ftp.gnu.org

Thread-2 error speedtest.tele2.net: 530 Permission denied.
Thread-2 Pārbauda ftp.mozilla.org

Thread-3 Pabeidza ftp.gnu.org:
  lrwxrwxrwx    1 0        0               8 Aug 20  2004 CRYPTO.README -> .message
  -rw-r--r--    1 0        0           17864 Oct 23  2003 MISSING-FILES
  -rw-r--r--    1 0        0            4178 Aug 13  2003 MISSING-FILES.README
  -rw-r--r--    1 0        0            2748 May 23  2023 README
  -rw-r--r--    1 0        0          405121 Oct 23  2003 before-2003-08-01.md5sums.asc
Thread-3 Pārbauda ftp.funet.fi

Thread-3 Pabeidza ftp.funet.fi:
  lrwxrwxrwx    1 0          0                  17 Jun 18  2019 README -> /pub/files/README
  lrwxrwxrwx    1 0          0                  25 Feb 26  2024 README.PRIVACY -> /pub/files/README.PRIVACY
  drwxr-xr-x    2 0          0                 125 Dec  7  2015 dev
  -rw-r--r--    1 108        42                318 May 31  2007 favicon.ico
  lrwxrwxrwx    1 0          0                  16 Jun 18  2019 index -> /pub/files/index
Thread-3 Pārbauda ftp.sunet.se

Thread-3 Pabeidza ftp.sunet.se:
  -rw-r--r--    1 ftp      ftp          1597 Sep 12  2022 HEADER.html
  lrwxrwxrwx    1 ftp      ftp             3 Mar 16  2010 Public -> pub
  drwxr-xr-x    3 ftp      ftp            16 Dec 16 19:56 about
  drwxr-sr-x   25 ftp      ftp            28 Dec 31 14:21 cdimage
  drwxr-xr-x    2 ftp      ftp             3 Jun 14  2006 conspiracy
Thread-3 Pārbauda ftp.freebsd.org

Thread-3 Pabeidza ftp.freebsd.org:
  -rw-r--r--    1 ftp      ftp          5430 Dec 06  2023 favicon.ico
  -rw-r--r--    1 ftp      ftp           669 Dec 06  2023 index.html
  drwxr-xr-x    3 ftp      ftp             3 Dec 06  2023 pub
Thread-3 Pārbauda ftp.debian.org

Thread-1 error ftp.dlptest.com: 530 Login incorrect.
Thread-1 Pārbauda ftp.tu-chemnitz.de

Thread-1 Pabeidza ftp.tu-chemnitz.de:
  -rw-r--r--    1 0        0        2986082933 Jan 18 05:16 INDEX
  drwxr-xr-x   12 0        0              10 Oct 14 11:58 pub
  -rw-r--r--    1 0        0               0 Mar 02  2023 test

Thread-2 error ftp.mozilla.org: timed out

Thread-3 error ftp.debian.org: timed out

Vajadzētu būt, ka viss
```