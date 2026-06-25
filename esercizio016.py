"""Le Funzioni Lambda sono funzioni anonime, ovvero funzioni senza nome.
Sono definite utilizzando la parola chiave `lambda`, seguita da una lista di argomenti, 
due punti e un'espressione. La sintassi generale è la seguente:"""
""" quadrato = lambda x: x ** 2
    print(quadrato(5))  # Output: 25 """

# Esercizio 16: Funzione Lambda per il calcolo del prodotto
# Definisci una funzione Lambda per calcolare il prodotto di due numeri.
# Chiedi all'utente di inserire due numeri e utilizza la funzione lambda per calcolare il prodotto.
# Stampa il risultato.

prodotto = lambda x, y: x * y

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

print("Il prodotto è:", prodotto(num1, num2))
