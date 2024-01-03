# 1
numero_intero = 10
numero_decimale = 3.14
testo = "Ciao, mondo!"

# la funzione type() per ottenere il tipo di dato della variabile

tipo_intero = type(numero_intero)
tipo_decimale = type(numero_decimale)
tipo_testo = type(testo)

print(tipo_intero, tipo_decimale, tipo_testo)

# 2
somma = 55 + 27
differenza = 76 - 18
prodotto = 14 * 2
divisione = 56 / 2

condizione_and = True and False
condizione_or = True or False
condizione_not = not True

# Operatori logici

# condizione_and = True and False:
# => L'operatore and restituisce True solo se entrambe le condizioni sono vere. Quindi, condizione_and sarà False perché True and False è False.

# condizione_or = True or False:
# => L'operatore or restituisce True se almeno una delle condizioni è vera. Quindi, condizione_or sarà True perché True or False è True.

# condizione_not = not True:
# => L'operatore not restituisce l'inversione della condizione. Se la condizione è True, not True sarà False, e viceversa. Quindi, condizione_not sarà False perché not True è False.

print(somma, differenza, prodotto, divisione)
print(condizione_and, condizione_or, condizione_not)

# 3
eta = 18
if eta >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

# 4
for i in range(5):
    print(i)

# for è una parola chiave che inizia il costrutto del ciclo for.
# i è una variabile che rappresenterà ciascun elemento dell'iterabile (nel caso specifico, la sequenza generata da range(5)).
# in è una parola chiave che specifica l'iterabile su cui verrà iterato (in questo caso, range(5)).
# range(5) genera una sequenza di numeri da 0 a 4 (5 escluso). Quindi, il ciclo for itera su questi valori.
    
# 5
contatore = 0
while contatore < 3:
    print("Iterazione:", contatore)
    contatore += 1

# while è una parola chiave che inizia il costrutto del ciclo while.
# contatore < 3 è la condizione di controllo. Il ciclo while continuerà ad eseguire il suo blocco di codice finché questa condizione è vera.
# contatore += 1: Incrementa il valore della variabile contatore di 1 ad ogni iterazione, in modo da evitare un ciclo infinito.
