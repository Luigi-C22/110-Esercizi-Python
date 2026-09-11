#Esempio di lettura di file CSV
import csv

""" with open("dati.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        print(riga) """


# Esercizio 40: Lettura di file CSV
# Crea un file studenti.csv contenente i nomi e le età di alcuni studenti.
# Scrivi un programma che legge il file e stampa i dati di ogni singolo studente.

with open("studenti.csv", "r") as file:
    lettore_csv = csv.reader(file)
    for riga in lettore_csv:
        for i in range(0, len(riga), 2):
            nome = riga[i].strip()
            eta = riga[i + 1].strip()
            print(f"Nome studente: {nome}, Età: {eta}")
