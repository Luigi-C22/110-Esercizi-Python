# Esercizio 22: Applicazione di Operazioni Comuni
# Crea una lista di numeri da 1 a 10 e calcola la somma di tutti gli elementi.
# Crea una tupla con cinque parole e verifica se una parola specifica esiste nella tupla.
# Crea un dizionario di cinque prodotti (nome e prezzo) e trova il prezzo totale di tutti i prodotti.
# Crea due set di numeri e trova l'intersezione.

numeri = list(range(1, 11))
somma = sum(numeri)
print("La somma dei numeri da 1 a 10 è:", somma)

parole = ("cane", "gatto", "uccello", "pesce", "coniglio")
parola_da_verificare = "gattino"
if parola_da_verificare in parole:
    print(f"La parola '{parola_da_verificare}' esiste nella tupla.")
else:
    print(f"La parola '{parola_da_verificare}' non esiste nella tupla.")

prodotti = {
    "latte": 1.5,
    "pane": 2.0,
    "uova": 3.0,
    "formaggio": 4.5,
    "burro": 2.5
}
prezzo_totale = sum(prodotti.values())
print("Il prezzo totale dei prodotti è:", prezzo_totale)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersezione = set1 & set2
print("L'intersezione dei due set è:", intersezione)    
