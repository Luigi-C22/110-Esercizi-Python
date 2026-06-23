# Esercizio 14: Calcolo dell'area del rettangolo
# Definisci una funzione area_rettangolo che accetta la base e l'altezza come parametri.
# La funzione deve calcolare e restituire l'area del rettangolo.
# Chiedi all'utente di inserire i valori di base e altezza, calcola l'area e stampa il risultato.

def area_rettangolo(base, altezza):
    return base * altezza

base = float(input("Inserisci la base del rettangolo m2: "))
altezza = float(input("Inserisci l'altezza del rettangolo m2: "))  
print("L'area del rettangolo è:", area_rettangolo(base, altezza), "metri quadrati.")
