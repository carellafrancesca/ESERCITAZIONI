# 1) Conteggio delle occorrenze di una parola

def conteggio_parole(frase, parola):
    parole = frase.split()
    # La frase viene divisa in una lista di parole utilizzando il metodo split(). Il risultato è una lista di tutte le parole presenti nella frase.
    conteggio = parole.count(parola)
    # Viene utilizzato il metodo count() per contare quante volte la parola specificata appare nella lista di parole parole.
    return conteggio

test_frase = "Python è un linguaggio di programmazione, e Python è molto potente."
test_parola = "Python"
print(conteggio_parole(test_frase, test_parola))

# 2) Calcolo della potenza

def potenza(base, esponente):
    return base ** esponente

base = 3
esponente = 5
print(f"{base} elevato a {esponente} è {potenza(base, esponente)}")

# La f-string è utilizzata per formattare la stringa in modo che possa includere direttamente i valori di variabili o espressioni all'interno del testo della stringa senza doverli concatenare o formattare separatamente.

# All'interno della f-string, {base} viene sostituito con il valore della variabile base, {esponente} con il valore di esponente, e {potenza(base, esponente)} con il risultato della chiamata alla funzione potenza(base, esponente).

# 3) Somma degli elementi di una lista

def somma_lista(lista):
    return sum(lista)
    # sum è una funzione built-in di Python che serve per calcolare la somma degli elementi di una sequenza

lista_numeri = [1,2,3,4,5,6,7,8]
print(f"La somma degli elementi nella lista è {somma_lista(lista_numeri)}")
# La parte {somma_lista(lista_numeri)} all'interno della f-string è un'espressione che viene valutata durante la creazione della stringa.

# 4) Generazione di password casuali
import random
import string

def genera_password (lunghezza):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    # La stringa caratteri viene creata concatenando le lettere ASCII (maiuscole e minuscole) da string.ascii_letters, i numeri da string.digits e i caratteri di punteggiatura da string.punctuation.

    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    
    # random.choice(caratteri): random.choice() viene utilizzato per selezionare casualmente un carattere dalla stringa caratteri.

    # for _ in range(lunghezza): Questo è un ciclo for che si ripete per la lunghezza specificata della password (lunghezza).
    # L'underscore _ viene utilizzato come variabile temporanea per indicare che il valore non è utilizzato nel corpo del ciclo.

    # ''.join(...): join è un metodo delle stringhe che unisce una sequenza di stringhe in un'unica stringa.
    # In questo caso, tutte le scelte casuali fatte nel ciclo sono concatenate per formare una stringa.

    return password

lunghezza_password = 10
print(f"La password generata è: {genera_password(lunghezza_password)}")

# 5) Unione di liste senza duplicati

def unione_senza_duplicati(lista1, lista2):
    unione = list(set(lista1) | set(lista2))

    # set(lista1) e set(lista2) convertono ciascuna delle liste in un insieme, eliminando eventuali duplicati, poiché gli insiemi non contengono duplicati.

    # set(lista1) | set(lista2) esegue l'operazione di unione tra i due insiemi, mantenendo solo gli elementi unici.

    return unione

lista_a = [1, 2, 3, 4, 7, 8, 13, 17, 18, 20]
lista_b = [3, 4, 5, 6, 8, 10, 12, 15, 17, 23]
print(f"L'unione delle liste è: {unione_senza_duplicati(lista_a, lista_b)}")

