# Esempio lettura e scrittura di file riga per riga
with open("file_di_testo.txt", "r") as file:
    for riga in file:
        print(riga.strip())  # Stampa la riga senza spazi bianchi iniziali e finali

# Esercizio 38:  Contatore di linee
# Crea un file documento.txt con alcune righe di testo.
# Scrivi il programma che legge il file e conta il numero di righe.

with open("documento.txt", "r") as file:
    conta_righe = sum(1 for riga in file)
    print("Il file contiene", conta_righe, "righe.")
    
