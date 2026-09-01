# PROGETTO FINALE

# Gestione di un sistema di biblioteca.
print("Benvenuto nel sistema di gestione della biblioteca!")

# Crea una classe Libro con attributi titolo, autore e disponibile.
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return f"{self.titolo} di {self.autore} - {stato}"
    
# Crea una classe Biblioteca con un attributo catalogo che è una lista di libri.
class Biblioteca:
    def __init__(self):
        self.catalogo = []

# Aggiungi metodi aggiungi_libro, presta_libro e restituisci_libro per gestire il catalogo.
    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)

    def presta_libro(self, libro):
        if libro.disponibile:
            libro.disponibile = False
            print(f"Hai prestato il libro: {libro}")
        else:
            print("Il libro non è disponibile.")

    def restituisci_libro(self, libro):
        if not libro.disponibile:
            libro.disponibile = True
            print(f"Hai restituito il libro: {libro}")
        else:
            print("Il libro era già disponibile.")

# Crea una istanza della biblioteca e aggiungi alcuni libri.
biblioteca = Biblioteca()
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry")
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)


# Presta e restituisci un libro, aggiornando la disponibilità.
biblioteca.presta_libro(libro1)
biblioteca.restituisci_libro(libro1)
biblioteca.aggiungi_libro(libro3)



