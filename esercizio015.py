# Esercizio 15: Differenza tra Scope Locale e Globale
# Crea una variabile numero globale.
# Crea una funzione modifica_numero che modifica numero all'interno della funzione.
# Stampa il valore di numero prima e dopo la chiamata alla funzione per vedere come cambia.

numero = int(input("Immetti un numero: "))  # Variabile globale
def modifica_numero():
    global numero
    numero = numero *2  # Modifica la variabile globale

print("Prima della chiamata:", numero)
modifica_numero()
print("Dopo la chiamata:", numero)
