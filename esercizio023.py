# Esercizio 23: Sistema di Inventario per un Negozio

# Crea un dizionario per rappresentare l'inventario del negozio, con i prodotti come
#      chiavi e i loro prezzi come valori.
inventario = {
    "mela": {"prezzo":0.5, "quantità": 10},
    "banana": {"prezzo":1, "quantità": 15},
    "arancia": {"prezzo":0.4, "quantità": 8},
    "pera": {"prezzo":0.6, "quantità": 12},
    "pesca": {"prezzo":0.7, "quantità": 5},
    "kiwi": {"prezzo":0.8, "quantità": 7},
    "uva": {"prezzo":1.0, "quantità": 20},
    "mango": {"prezzo":1.5, "quantità": 3},
}

# Usa una lista per registrare le vendite di vari prodotti.
vendite = ["mela", "kiwi", "banana", "arancia","mango", "mango", "mela", "kiwi", "pera", "banana", "mela"]

# Aggiorna l'inventario sottraendo gli articoli venduti.
totale_vendite = 0
for prodotto in vendite:
        if prodotto in inventario and inventario[prodotto]["quantità"] > 0:
            totale_vendite += inventario[prodotto]["prezzo"]
            inventario[prodotto]["quantità"] -= 1
        else:
            print(f"Prodotto {prodotto} non disponibile o esaurito.")

# Stampa il valore totale delle vendite e l'inventario aggiornato.
print(f"Valore totale delle vendite: {totale_vendite}")

print("Inventario aggiornato:")
for prodotto, dettagli in inventario.items():
    print(f"{prodotto}: {dettagli['quantità']} unità disponibili")