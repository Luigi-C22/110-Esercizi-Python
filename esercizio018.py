# Esercizio 19: Creazione e Modifica di una Lista
# Crea una lista di tre elementi rappresentanti nomi di animali.
# Aggiungi un altro animale alla lista.
# Rimuovi il primo animale dalla lista.
# Stampa la lista aggiornata.

animali = ["cane", "pollo"]
print("Lista animali iniziale:", animali)
pet = input("Inserisci un animaletto:")
animali.append(pet)
print("Lista animali con append:", animali)

pet_remove = input("immetti l'animale da rimuovere:")


if pet_remove not in animali:
        print("questo animale non è in lista!")
else:
        animali.remove(pet_remove)
        print("Lista animali col primo rimosso:", animali)
