# Esercizio 17: Calcolatrice con funzioni modulari
# Crea funzioni per eseguire le operazioni di base:  somma, sottrazione, moltiplicazione, e divisione.
# Crea una funzione principale calcolatrice che chiede all'utente di scegliere 
#       un'operazione e di inserire due numeri.
# Usa le funzioni per calcolare e stampare il risultato in base alla scelta dell'utente.
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    return a / b

def calcolatrice():
    print("Benvenuto nella calcolatrice!")
    print("Scegli un'operazione:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    scelta = input("Inserisci il numero dell'operazione desiderata: ")

    if scelta in ['1', '2', '3', '4']:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if scelta == '1':
            risultato = somma(num1, num2)
        elif scelta == '2':
            risultato = sottrazione(num1, num2)
        elif scelta == '3':
            risultato = moltiplicazione(num1, num2)
        elif scelta == '4':
            risultato = divisione(num1, num2)

        print(f"Risultato: {risultato}")
    else:
        print("Scelta non valida.")