faila_lokacija = ""

with open(faila_lokacija, 'r') as file:
    [print(line) for line in file if 'USB' in line]

file.close()