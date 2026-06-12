# Esercizio 7: Somma dei numeri da 1 a N
# Chiedi all'utente di inserire un numero positivo N.
# Utilizza un ciclo for per calcolare la somma di tutti i numeri da 1 a N.
# Stampa il risultato.

print("Inserisci un numero positivo: ")
N = int(input("Immetti il numero: "))
somma = 0
for i in range(1, N + 1):
    somma += i
print (f"Somma dei numeri da 1 a {N} è: {somma}")

