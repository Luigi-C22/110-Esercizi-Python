# Esercizio 2: Calcolatrice base
# Chiedi all'utente di inserire due numeri
# Utilizza gli operatori aritmetici per sommare,
#        sottrarre, moltiplicare e dividere i numeri
# Stampa i risultati di ciascuna operazione

num1 = float(input ("Inserisci il primo numero: "))
num2 = float(input ("Inserisci il secondo numero: "))
sum = num1 + num2
sottrazione = num1 - num2
moltiplicazione = num1 * num2
if num2 != 0:
    divisione = num1 / num2 

print("Somma:", sum)
print("Sottrazione:", sottrazione)
print("Moltiplicazione:", moltiplicazione)
print("Divisione:", divisione)