# Esercizio 25: Gestione delle eccezioni
# Scrivi una funzione input_numero che chiede all'utente di inserire un numero.
# Se l'utente inserisce un valore non numerico, la funzione deve restituire un messaggio di errore
# Se l'utente inserisce zero, la funzione deve restituire un messaggio di errore specifico per la divisione per zero.

def input_numero():
    try:
        numero = float(input("Inserisci un numero: "))
        if numero == 0:
            print("Errore: Non puoi inserire zero, la divisione per zero non è consentita.")
            return None
        return numero
    except ValueError:
            print("Errore: Devi inserire un valore numerico.")
    except ZeroDivisionError:
            print("Errore: Non puoi inserire zero, la divisione per zero non è consentita.")