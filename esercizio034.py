#esempio di polimorfismo
class Forma:
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza=larghezza
        self.altezza=altezza

    def area(self):
        return self.larghezza * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14 * (self.raggio **2)