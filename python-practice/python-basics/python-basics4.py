# 1) Calcolatrice

num1 = float(input("Inserisci il primo numero:"))
num2 = float(input("Inserisci il secondo numero:"))

# float(): La funzione float() viene utilizzata per convertire l'input dell'utente in numeri decimali (float). 

somma = num1 + num2
diff = num1 - num2
prodotto = num1 * num2
quoziente = num1 % num2

print(f"Somma: {somma}")
print(f"Differenza: {diff}")
print(f"Prodotto: {prodotto}")
print(f"Quoziente: {quoziente}")

# In generale, un formato f-string inizia con una "f" o "F" prima delle virgolette di apertura. All'interno di una f-string, puoi includere variabili e espressioni direttamente tra parentesi graffe {} e Python le valuterà e le inserirà nel testo della stringa quando viene stampato. 

# 2)
nome = "Alice"
eta = 25

# Utilizzo generale di un f-string
messaggio = f"Ciao, mi chiamo {nome} e ho {eta} anni."

print(messaggio)
# In questo esempio, i valori delle variabili nome e eta vengono inseriti direttamente nella stringa attraverso le parentesi graffe all'interno dell'f-string.

# 3) Calcolo dell'area di un cerchio

import math
# La libreria math in Python fornisce un set di funzioni matematiche più avanzate rispetto alle operazioni matematiche di base disponibili nel core del linguaggio. Alcune delle funzioni comuni incluse in math includono operazioni trigonometriche, logaritmi, radici quadrate e costanti matematiche.

raggio = float(input("inserisci il raggio del cerchio: "))
area = math.pi * raggio**2
# In questo caso, stai utilizzando math.pi, che rappresenta la costante matematica π (pi greco).

print(f"L'area del cerchio è: {area}")

# 4) Stampa numeri primi

# Definizione di una funzione chiamata is_primo
def is_primo(numero):
    # Itera su tutti i numeri da 2 fino alla radice quadrata di 'numero' + 1
    for i in range(2, int(numero**0.5) + 1):
        # Controlla se 'numero' è divisibile per 'i'
        if numero % i == 0:
            return False
    return True

# Itera su tutti i numeri da 2 a 20
for num in range(2, 21):
    # Chiamata alla funzione is_primo per verificare se 'num' è primo
    if is_primo(num):
        print(num)
        # Stampa il numero se è primo. L'argomento end=' ' fa sì che la stampa successiva continui sulla stessa riga, separando i numeri con uno spazio.

# 5) Contare le vocali
        
stringa = input("Inserisci una stringa: ")
vocali = "aeiouAEIOU"
# Inizializza un contatore a zero
contatore = 0

# Itera attraverso ogni carattere nella stringa inserita dall'utente
for carattere in stringa:
    # Verifica se il carattere corrente è una vocale
    if carattere in vocali:
        # Se è una vocale, incrementa il contatore di 1
        contatore += 1

print(f"Numero di vocali nella stringa: {contatore}")