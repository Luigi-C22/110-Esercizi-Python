# Esercizio 26: Funzione con finally
# Scrivi una funzione calcola_rapporto che calcola il rapporto tra due numeri.
# La funzione deve utilizzare try, except, else e finally.
# # il finally deve stampare "Chiusura programma" indipendentemente dall'esito della divisione.

def calcola_rapporto(num1, num2):
    try:
        rapporto = num1 / num2
    except ZeroDivisionError:
        print("Errore: Divisione per zero.")
        return None
    else:
        print(f"Il rapporto tra {num1} e {num2} è {rapporto}.")
        return rapporto
    finally:
        print("Chiusura programma.") 