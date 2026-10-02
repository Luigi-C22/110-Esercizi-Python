# La libreria random
# Esempio di uso della libreria random

""" import random
numero_casuale = random.randint(1,100)
print("Il numero casuale generato è:", numero_casuale)
 """

# Esercizio 44: Simulazione del lancio del dado
# Crea una funzione lancia_dado che simula il lancio di un dado a 6 facce,
#           restituendo un numero tra 1 e 6.
# Esegui la funzione 10 volte e stampa il risultato di ogni lancio.
import random

lancia_dado = random.randint(1, 6)
print("Il numero ottenuto lanciando il dado è:", lancia_dado)

for i in range(3):
    lancia_dado = random.randint(1, 6)
    print(f"Il numero ottenuto al lancio {1+i} è: {lancia_dado}");
