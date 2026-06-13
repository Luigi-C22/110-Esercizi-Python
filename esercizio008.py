# Esercizio 8: Indovina il numero
# Genera un numero casuale tra 1 e 10 (usa la libreria Random).
# Chiedi all'utente di indovinare il numero.
# Continua a chiedere finchè l'utente non indovina il numero corretto.
# Stampa il numero di tentativi.

import random
numero = random.randint(1, 10)
tentativi = 0
while tentativi < 10:
    indovina = int(input("Indovina il numero tra 1 e 10: "))
    tentativi += 1
    if indovina == numero:
        print(f"Complimenti! Hai indovinato il numero in {tentativi} tentativi.")
        break
    elif indovina < numero:
        print("Troppo basso! Riprova.")
    else:
        print("Troppo alto! Riprova.")