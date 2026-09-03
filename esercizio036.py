#Esempio di lettura file
""" with open("file_di_testo.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)
 """
# Esercizio 36: Lettura di un File di Testo
# Crea un file di testo saluti.txt contenente alcuni saluti in diverse lingue.
# Scrivi un programma che legge il contenuto del file e lo stampa a schermo.

with open("saluti.txt", "r") as file:
    contenuto_del_file = file.read()
    print(contenuto_del_file)
    