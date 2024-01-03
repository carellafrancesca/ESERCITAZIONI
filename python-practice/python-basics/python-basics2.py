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