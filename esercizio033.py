#Esempio
class Animale:
    def __init(self, nome):
        self.nome = nome

    def parla(self):
        pass

class Cane(Animale):
    def parla(self):
        print("Woof!")

class Gatto(Animale):
    def parla(self):
        print("Meow!")



# Esercizio 33: Ereditarietà
# Crea una classe Veicolo con un attributo marca e un metodo descrizione.
# Crea una sottoclasse Auto che eredita da Veicolo e aggiunge un metodo tipo che stampa "Questa è un'auto."
# Crea una istanza della classe Auto e chiama i metodi descrizione e tipo.

