# Python è progettato per esser facile da leggere e scrivere. 
# La sua sintassi è chiara e pulita, il che facilita la comprensione del codice. 
# Inoltre supporta la programmazione procedurale, orientata ad oggetti e funzionale. 
# Offre una vasta gamma di librerie e framework che semplificano lo sviluppo.

# Comando da terminale: python nome.py (python python-basics.py)

# Tipi di dati:
# Intero (int): Numeri interi, ad esempio 5, 10.
# Virgola mobile (float): Numeri decimali, ad esempio 3.14, 2.0.
# Stringa (str): Sequenza di caratteri, ad esempio "hello", 'python'.

# Strutture dati:
# Lista (list): Una sequenza modificabile di elementi, ad esempio my_list = [1, 2, 3].
# Tuple: Una sequenza immutabile di elementi, ad esempio my_tuple = (1, 2, 3).
# Dizionario (dict): Una collezione di coppie chiave-valore, ad esempio my_dict = {'chiave': 'valore'}.
# Insieme (set): Una collezione non ordinata di elementi unici, ad esempio my_set = {1, 2, 3}.

# Funzioni:
# Definizione: Creare una funzione con la parola chiave def.
# Chiamata: Eseguire una funzione specificandone il nome seguito da parentesi, ad esempio nome_funzione().

# Input e output:
# input(): Funzione per ottenere l'input dall'utente.
# print(): Funzione per stampare testo o variabili sulla console.

# Esercizi base.

# 1) 
print("Hello, world!")

# 2)
nome = 'Alice'
età = 25
print("Il nome è", nome, "e l'età è", età, "anni")

# 3)
a = 5
b = 10
print("La somma di ", a, "e", b, "è", a + b)

# 4)
nome = 'Bob'
età = 30
print("Il nome è {} e l'età è {}".format(nome, età))
# Le parentesi graffe {} fungono da segnaposto per i valori che saranno inseriti nella stringa.

# .format(nome, età) è il metodo format() applicato alla stringa. Questo metodo prende gli argomenti forniti (in questo caso, nome e età) e li inserisce nei segnaposto nella stringa di formato. Quindi, il valore di nome sostituirà {} nella prima parentesi graffa e il valore di età sostituirà {} nella seconda parentesi graffa.

# 5) 
frutta = ['mela', 'banana', 'fragola']
print("Lista di frutta:", frutta)

studente = {"nome": "Mario", "cognome": "Rossi", "età": 20}
print("Dizionario dello studente", studente)

# 6) 
persona = ["Alice", "Rossi", 25, "Milano"]
nome = persona[0]
età = persona[2]
print(nome, "ha", età, "anni")

# 7) 
numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print(numero, "è un numero pari")
else:
    print(numero, "è un numero dispari")

