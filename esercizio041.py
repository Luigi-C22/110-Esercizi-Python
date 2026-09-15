# Esempio di scrittura di un file CSV
import csv

dati = [["Nome", "Età"], ["Alice", 22], ["Bob", 25]]

with open("output.csv", "w", newline = "") as file:
    scrittore_csv = csv.writer(file)
    scrittore_csv.writerows(dati)

with open("output.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        print(riga)
