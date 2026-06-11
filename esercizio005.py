# Esercizio 5: Creazione di una Mini Calcolatrice
# Chiedi all'utente di inserire due numeri.
# Fornisci un menù per scegliere un'operazione: somma, sottrazione, moltiplicaazione o divisione.
# Esegui l'operazione  selezionata e mostra il risultato.
# Gestisci eventuali errori, come la divisione per zero.

print("Inserisci due numeri.")
num1 = float(input("Primo numero: "))
num2 = float(input("Secondo numero: "))

print("Scegli l'operazione da eseguire: ")
print("1. Somma")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

scelta = input("inserisci il numero corrispondente all'operazione da eseguire: ")
if scelta == "1":
    risultato = num1 + num2
    print(f"Il risultato dell'addizione è : {risultato}")

elif scelta == "2":
    risultato = num1 - num2
    print(f"Il risultato della sottrazione è: {risultato}")

elif scelta == "3":
    risultato = num1 * num2
    print(f"Il risultato della moltiplicazione è: {risultato}")

elif scelta == "4":
    if num2 != 0:
        risultato = num1/num2
        print(f"Il risultato della divisione è: {risultato}")
    else:
        print("ERRORE: Divisione per zero non consentita")

