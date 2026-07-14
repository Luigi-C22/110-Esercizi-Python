# Esercizio 24: Rilevazione di errori.
# Scrivi una funzione divisione_sicura che accetti due numeri
#        e restituisca il risultato della divisione.
# Fai in modo che la funzione restitusca un messaggio di errore
#    se il secondo numero è zero.

num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))

def divisione_sicura(num1, num2):
    try:
        risultato = num1 / num2
        return risultato
    except ZeroDivisionError:
        return "Errore: divisione per zero non consentita."
print(divisione_sicura(num1, num2))