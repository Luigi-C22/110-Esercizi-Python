#Esempio di lettura di file CSV
import csv

with open("dati.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        print(riga)
        