# Esercizio 19: Creazione e Modifica di una Lista
# Crea una lista di tre elementi rappresentanti nomi di animali.
# Aggiungi un altro animale alla lista.
# Rimuovi il primo animale dalla lista.
# Stampa la lista aggiornata.

animali = ["cane", "gatto", "pesce", "rana", "uccello"]
print("Lista animali iniziale:", animali)
animali.append("Rinoceronte")
print("Lista animali con append:", animali)

animali.pop(0)
print("Lista animali col primo rimosso:", animali)
