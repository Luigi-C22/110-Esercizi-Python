# Esercizio 21:  Operazioni sui set.
# Crea un set con tre numeri.
# Aggiungi un nuovo numero al set.
# Rimuovi un numero al set
# Crea un secondo set e calcola l'unione dei due set.

numeri = {1,2,3,}
numeri.add(4)
print(numeri)
numeri.remove(2)
print(numeri)

numeri2 = {5,6,7}
print(numeri2)

nuovo_set = numeri|numeri2
print(nuovo_set)
