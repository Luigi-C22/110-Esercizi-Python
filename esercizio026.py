# Esercizio 26: Funzione con finally
# Scrivi una funzione calcola_rapporto che calcola il rapporto tra due numeri.
# La funzione deve utilizzare try, except, else e finally.
# # il finally deve stampare "Chiusura programma" indipendentemente dall'esito della divisione.

def calcola_rapporto(num1, num2):
 while True:   
    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))
        rapporto = num1 / num2
    except ZeroDivisionError:
        print("Errore: Divisione per zero.")
        
    else:
        print(f"Il rapporto tra {num1} e {num2} è {rapporto}.")
        break
    finally:
        print("Chiusura programma.") 

(calcola_rapporto(0, 0))  # Esempio di chiamata alla funzione
      