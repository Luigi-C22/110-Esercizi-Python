""" class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

#creazione di un oggetto
persona1 = Persona("Mario", 30)
persona1.saluta()  """

# Esercizio 30:  Creazione di una classe
# Crea una classe Animale con un costruttore (__init__) che accetti un nome ed una specie.
# Aggiungi un metodo descrivi che stampi il nome e la specie dell'animale.
# Crea una istanza della classe Animale e chiama il metodo descrivi.

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def descrivi(self):
        print(f"Questo è un {self.specie} chiamato {self.nome}.")

# Crea una istanza della classe Animale e chiama il metodo descrivi.
animale1 = Animale("Bongo", "leone")
animale1.descrivi()
