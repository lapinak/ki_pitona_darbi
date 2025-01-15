faila_lokacija = "C:\\Users\\User\\Documents\\GitHub\\ki_pitona_darbi\\log_file\\testfile.txt"

with open(faila_lokacija, 'r') as file:
    [print(line) for line in file if 'USB' in line]

file.close()