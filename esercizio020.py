# Esercizio 20: Creazione e Manipolazione di un Dizionario
# Crea un dizionario per un libro con le seguenti chiavi: titolo, autore e anno
# Aggiungi una nuova chiave genere al dizionario.
# Aggiorna l'anno di pubblicazione.
# Stampa il dizionario aggiornato

titolo = str(input("inserisci titolo: "))
autore = str(input("inserisci autore: "))
anno = int(input("Inserisci l'anno: "))


libro = {"Titolo":titolo, 
         "Autore":autore,
         "Anno":anno}
libro["Genere"] = "Romanzo"
libro["Anno"] = 1915
print(libro)
