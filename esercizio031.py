# Esercizio 31: Creazione attributi e metodi
# Crea una classe Libro con attributi titolo e autore.
# Aggiungi un metodo descrizione che stampa le informazioni del libro.
# Crea una istanza della classe libro e chiama il metodo descrizione.

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def descrizione(self):
        print(f"{self.titolo} scritto da {self.autore}")

descrizione_libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
descrizione_libro.descrizione()


