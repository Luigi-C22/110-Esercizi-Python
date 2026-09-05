#Esempio di scrittura in un file:
with open("output.txt", "w") as file:
    file.write("Ciao mondo!\n")
    file.write("Questo é un file di testo.\n")
    file.write("Saluti a tutti!")

# Esercizio 37: Scrittura su un File di Testo
# Scrivi un programma che chiede all'utente di inserire il proprio nome.
# Il programma deve salvare il nome in un file nomi.txt.
# Ogni nome deve essere aggiunto in una nuova riga, senza cancellare quelli esistenti.

print("Devi inserire il tuo nome per salvarlo in un file di testo")
nome = input("Inserisci qui il tuo nome: ")
with open("nomi.txt", "a") as file:
    file.write(nome + "\n")
