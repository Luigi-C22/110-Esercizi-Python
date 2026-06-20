""" Progetto: Gioco del numero magico
    In questo gioco l'utente deve indovinare un 'numero magico' 
    scelto casualmente dal progrmma, con una serie d indizi. """

# Esercizio 11: Gioco del 'Numero magico'
# Genera un numero casuale tra 1 e 100.
# Chiedi all'utente di indovinare il numero.
# Dopo ogni tentativo, fornisci un feedback: se il numero è più alto o più basso.
# Utilizza while per continuare fino a quando l'utente indovina.
# Usa break per terminare il ciclo una volta che il numero è stato indovinato.
# Stampa il numero di tentativi.

import random
numero_magico = random.randint(1, 100)
tentativi = 0
while True:
    tentativo = int(input("Indovina il numero magico (tra 1 e 100): "))
    tentativi += 1
    if tentativo < numero_magico:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_magico:
        print("Troppo alto! Riprova.")
    else:
        print(f"Bene! Hai indovinato. Il numero magico era proprio {numero_magico}!! E ce l'hai fatta in {tentativi} tentativi.")
        break

