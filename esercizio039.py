# Gestione errori nella lettura e scrittura files

#Esempio di gestione delle eccezioni:
try:
    with open("file_inesistente.txt", "r") as file:
        contenuto = file.read()
except FileNotFoundError:
    print("Errore: il file non esiste")
    