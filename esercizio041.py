# Esempio di scrittura di un file CSV
""" import csv

dati = [["Nome", "Età"], ["Alice", 22], ["Bob", 25]]

with open("output.csv", "w", newline = "") as file:
    scrittore_csv = csv.writer(file)
    scrittore_csv.writerows(dati)

with open("output.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        print(riga) """

# Esercizio 41: Scrittura dati in un file CSV
# Crea una lista di dizionari, 
#            dove ogni dizionario rappresenta uno studente con nome e età.
# Scrivi un programma che salva questi dati in un file studenti.csv 
#            dove ogni riga rappresenta uno studente.

import csv
studenti = [{"Nome": "Alice", "Età": 22}, {"Nome": "Bob", "Età": 25},
             {"Nome": "Charlie", "Età": 20}, {"Nome": "David", "Età": 23}]

with open("studenti.csv", "w", newline="") as file:
    campi = ["Nome", "Età"]
    scrittore_csv = csv.DictWriter(file, fieldnames=campi)
    scrittore_csv.writeheader()
    scrittore_csv.writerows(studenti)

