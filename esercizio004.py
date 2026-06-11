# Esercizio 4: Formattazione di una stringa
# Chiedi all'utente di inserire il proprio nome e cognome.
# Concatenali e stampa il nome completo in maiuscolo.
# utilizza il metodo .lower() per stampare il nome completo in minuscolo.

print("Inserisci il tuo nome e il tuo cognome.")
nome = input("Nome: ")
cognome = input("Cognome: ")
nome_completo = nome + " " + cognome
print(f"Il tuo nome completo è: {nome_completo}")
print(f"Il tuo nome completo è: {nome_completo.upper()}")
print(f"Il tuo nome completo è: {nome_completo.lower()}")
