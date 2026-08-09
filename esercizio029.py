# Esercizio 29: Divisione sicura con input da file.
# Crea un file di testo numeri.txt contenente una serie di numeri 
#                                                separati da nuove righe.
# Scrivi una funzione leggi_numeri che legge i numeri 
#              dal file e calcola la divisione di ciascun numero per 10.
# La funzione deve gestire eventuali errori dovuti alla presenza 
#                                         di valori non numerici nel file.

def leggi_numeri(nome_file):
    try:
        with open(nome_file, 'r') as file:
            for line in file:
                try:
                    numero = float(line.strip())
                    risultato = numero / 10
                    print(f"{numero} diviso 10 è {risultato}")
                except ValueError:
                    print(f"Valore non numerico trovato: {line.strip()}")
    except FileNotFoundError:
        print("Il file numeri.txt non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

leggi_numeri('numeri.txt')