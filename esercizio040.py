#Esempio di lettura di file CSV
import csv

with open("dati.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        print(riga)


# Esercizio 40: Lettura di file CSV
# Crea un file studenti.csv contenente i nomi e le età di alcuni studenti.
# Scrivi un programma che legge il file e stampa i dati di ogni singolo studente.