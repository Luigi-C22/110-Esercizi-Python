# Esercizio 13: Somma di due numeri
# Definisci una funzione chiamata somma che accetta due parametri a e b
# La funzione deve calcolare la somma di a e b e restituire il risultato.
# Chiama la funzione con due numeri a tua scelta e stampa il risultato.

def somma(a, b):
    return a + b

a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
print ("La somma di", a, "e", b, "è:", somma(float(a), float(b)))
