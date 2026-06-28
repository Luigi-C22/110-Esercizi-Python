# Esercizio 19: Crea una tupla con tre colori.
# Stampa il secondo colore della tupla.
# Tenta di aggiungere un nuovo colore e nota l'errore per capire l'immutabilità delle tuple.

# L'utente inserisce ad esempio: cane, gatto, criceto
risposta = input("Inserisci gli animali separati da una virgola: ")

# split(",") crea una lista separando le parole dove c'è la virgola, 
# e tuple() la trasforma immediatamente
#animali_tupla = tuple(risposta.split(","))

# Puliamo eventuali spazi bianchi di troppo attorno alle parole (opzionale)
animali_tupla = tuple(animale.strip() for animale in animali_tupla)

print("La tua tupla:", animali_tupla)