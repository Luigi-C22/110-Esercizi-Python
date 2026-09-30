# Esempio della libreria Math
""" import math
raggio = 5 
area_cerchio = math.pi * raggio ** 2
circonferenza = 2 * math.pi * raggio
print(f"L'area del cerchio con raggio {raggio} è: {area_cerchio:.3f}")
print(f"La circonferenza del cerchio con raggio {raggio} è: {circonferenza:.3f}") """

# Esercizio 43: calcolo dell'ipotenusa
# Crea una funzione che calcola l'ipotenusa di un triangolo rettangolo dati i cateti a e b.
# usa math.sqrt() per il calcolo della radice quadrata.

import math
def ipotenusa(a, b):
    lato_ipotenusa = math.sqrt(a**2 + b**2)
    return lato_ipotenusa

print("l'ipotenusa è: ", ipotenusa(3, 4))
