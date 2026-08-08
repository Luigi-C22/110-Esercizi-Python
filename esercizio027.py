class ErroreNegativo(Exception):
    pass    

def radice_quadrata(x):
    if x < 0:
        raise ErroreNegativo("Non è possibile calcolare la radice quadrata di un numero negativo.")
    return x ** 0.5

print(radice_quadrata(-6))