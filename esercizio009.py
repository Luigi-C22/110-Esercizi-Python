# Esercizio 9: Tavola Pitagorica
# Utilizza un ciclo for nidificato per creare una tavola pitagorica (Tabellina)
# Stampa la moltiplicazione tra i numeri d 1 a 10
""" 
for i in range(1,11):
    for j in range(1,11):
        print(i * j, end="\t")
    print()  # Stampa una nuova riga dopo ogni riga della tavola pitagorica
 """
# Soluzione alternativa con f-string per una formattazione più pulita
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")  # Formatta il numero con 4 spazi per l'allineamento
    print()  # Stampa una nuova riga dopo ogni riga della tavola pitagorica