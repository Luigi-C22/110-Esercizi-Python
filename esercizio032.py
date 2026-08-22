#Esercizio 32: Incapsulamento con Attributi Privati
# Crea una classe ContoBancario con attributo privato __saldo.
# Aggiungi metodi deposita e mostra_saldo.
# Crea un'istanza della classe e verifica il funzionamento dei metodi.
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo

    def deposita(self, importo):
        self.__saldo += importo

    def mostra_saldo(self):
        print(f"Saldo:{self.__saldo}")
        

conto = ContoBancario(1000)
conto.mostra_saldo()  # Output: Saldo:1000
conto.deposita(500)
conto.mostra_saldo()  # Output: Saldo:1500
