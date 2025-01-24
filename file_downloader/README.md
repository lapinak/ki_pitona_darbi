### Failu lejupielāde

Iekļauta iespēja ar CTRL + C iziet no lejupielādes, ja šķiet, ka kaut kas nav labi. 
Programma ļauj padot saiti ar vēlamo lejupielādes atrašanās vietu terminālī. 

Output terminālī, ja viss ir kārtībā:

```bash
Nosauc lejupielādējamo falilu: gramata
2025-01-24 20:48:49,830 - INFO - Sāk lejupielādi...
2025-01-24 20:48:49,831 - INFO - Ctrl+c, lai apturētu lejupielādi
2025-01-24 20:48:50,505 - INFO - Lejupielādē: 0.0%
2025-01-24 20:48:50,642 - INFO - Lejupielādē: 0.3%
2025-01-24 20:48:50,779 - INFO - Lejupielādē: 0.6%
2025-01-24 20:48:50,911 - INFO - Lejupielādē: 1.0%
...
2025-01-24 20:48:54,774 - INFO - Lejupielādē: 98.5%
2025-01-24 20:48:54,777 - INFO - Lejupielādē: 98.9%
2025-01-24 20:48:54,778 - INFO - Lejupielādē: 99.2%
2025-01-24 20:48:54,786 - INFO - Lejupielādē: 99.5%
2025-01-24 20:48:54,788 - INFO - Lejupielādē: 99.8%
2025-01-24 20:48:54,792 - INFO -
Pabeigts!
```

Output terminālī, ja tiek apturēta lejupielāde ar CTRL + C:

```bash
Nosauc lejupielādējamo falilu: gramata
2025-01-24 20:48:49,830 - INFO - Sāk lejupielādi...
2025-01-24 20:48:49,831 - INFO - Ctrl+c, lai apturētu lejupielādi
2025-01-24 20:48:50,505 - INFO - Lejupielādē: 0.0%
2025-01-24 20:48:50,642 - INFO - Lejupielādē: 0.3%
2025-01-24 20:48:50,779 - INFO - Lejupielādē: 0.6%
2025-01-24 20:48:50,911 - INFO - Lejupielādē: 1.0%
...
2025-01-24 20:46:26,476 - INFO - Lejupielādē: 75.8%
2025-01-24 20:46:26,477 - INFO - Lejupielādē: 75.9%
2025-01-24 20:46:26,478 - INFO - Lejupielādē: 75.9%
2025-01-24 20:46:26,479 - WARNING - Faila lejupielāde apturēta
```

Log faila izraksts saglabāts pie failiem.