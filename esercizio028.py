# Esercizio 28: Gestione di input Non Validi
# Scrivi una funzione calcola_media 
#               che calcola la media di una lista di numeri.
# La funzione deve gestire gli errori se la lista è vuota o 
#               contiene elementi non numerici.

def calcola_media(lista):
    if not lista:
        raise ValueError("La lista è vuota. Non è possibile calcolare la media.")
    
    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            raise TypeError(f"L'elemento '{elemento}' non è un numero valido.")
    
    return sum(lista) / len(lista)

print(calcola_media([1, 6, 3, 8]))  # Output: 4.5