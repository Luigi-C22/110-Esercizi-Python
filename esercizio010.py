# Esercizio 10: Controllo pari e dispari
# Chiedi all'utente di inserire un numero positivo N.
# Utilizza un ciclo for per stampare tutti i numeri da 1 a N,
#            ma utilizza continue per saltare i numeri dispari.

print("Immetti un numero positivo e stampo tutti i pari fino a quel numero.")
N = int(input("inserisci il numero qui: "))
for i in range (1, N + 1):
    if i % 2 != 0:
        continue
    print(i)
