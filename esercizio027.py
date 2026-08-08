""" class ErroreNegativo(Exception):
    pass    

def radice_quadrata(x):
    if x < 0:
        raise ErroreNegativo("Non è possibile calcolare la radice quadrata di un numero negativo.")
    return x ** 0.5

print(radice_quadrata(-6)) """

# Esercizio 27: Eccezione personalizzata per Valore Negativo
# Crea un'eccezione personalizzata ErroreEtaNegativa.
# Scrivi una funzione controlla_eta che solleva questa eccezione
#                                               se l'età inserita è negativa.
# La funzione deve restituire un messaggio "Età valida" se l'età è positva.

class ErroreEtaNegativa(Exception):
    pass

def controlla_eta(eta):
    if eta < 0:
        raise ErroreEtaNegativa("L'età non può essere negativa.")
    return "Età valida"

print(controlla_eta(-5))  # Questo solleverà l'eccezione ErroreEtaNegativa