# Gestione errori nella lettura e scrittura files

#Esempio di gestione delle eccezioni:
try:
    with open("file_inesistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError:
    print("Errore: il file non esiste")


# esercizio 39: Gestione errori nella lettura e scrittura files
# Scrivi un programma che tenta di aprire un file dati.txt.
# Se il programma non esiste, deve stampare "il file non è stato trovato".

try: 
    with open("dati.txt", "r") as file:
        contenuto_del_file = file.read()
except FileNotFoundError:
    print("il file non è stato trovato")
    