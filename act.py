import csv
lista = []

with open("appstore_games.csv") as data:
    entrada = csv.reader(data)
    lista = list(entrada)

for linea in lista:
    if 'EN' in linea[12] and linea[7] == '0':
        print(linea[2])