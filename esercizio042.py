# Progetto finale: Sistema di Registrazione delle vendite.
""" Creiamo un programma che registra e salva in un file CSV i dati di vendita
 di un negozio.
   Il programma richiederà al proprietario del negozio di inserire:
     il nome del prodotto,
     la quantità
     e il prezzo totale.
   Salverà quindi i dati in un file vendite.csv"""

#Esercizio 42: Sistema di registrazione delle vendite.
# Crea un programma che chiede all'utente di inserire prodotto, quantità e prezzo.
# Salva ogni registrazione nel file vendite.csv, con una riga per ogni vendita.
# Aggiugni una opzione per visualizzare tutte le vendite presenti nel file.

import csv

print("Benvenuto nel sistema di registrazione delle vendite.")

prodotto = input("Inserisci il nome del prodotto: ")
quantita = input("Inserisci la quantità venduta: ")
prezzo = input("Inserisci il prezzo totale: ")

with open('vendite.csv', mode='a', newline='') as file:
    campi = ['Prodotto', 'Quantità', 'Prezzo']
    writer = csv.DictWriter(file, fieldnames=campi)
    writer.writerow({'Prodotto': prodotto, 'Quantità': quantita, 'Prezzo': prezzo})

print("Vendita registrata con successo!")

with open('vendite.csv', mode='r') as file:
    file.seek(0)
    reader = csv.reader(file)
    
    
    print("Vendite registrate:")
    for row in reader:
      totale_incasso = sum(float(row[2]) """ for row in reader """) 
      print(f"Prodotto: {row[0]}, Quantità: {row[1]}, Prezzo: {row[2]}, euro")
    
    print(f"\nTotale incasso: {totale_incasso} euro")