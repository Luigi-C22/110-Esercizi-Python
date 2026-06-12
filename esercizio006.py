# Esercizio 6: Verifica della maggiore età
# Chiedi all'utente di inserire la sua età.
# Se l'età è maggiore di 18, stampa "Sei maggiorenne".
# Se l'età è uguale a 18, stampa "Hai appena compiuto 18 anni!".
# Altrimenti, stampa "Sei maggiorenne".

print("Inserisci il tuo nome e la tua età")
nome = str(input("Nome:"))
eta = int(input("Età:"))
if eta > 18:
    print(f"{nome} Sei maggiorenne")
elif eta == 18:
    print(f"{nome} Hai appena compiuto 18 anni!")
else:
    print(f"{nome} Sei minorenne")
    
