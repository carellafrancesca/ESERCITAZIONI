# 1 - len() - lunghezza della stringa
string = "Sto imparando ad utilizzare Python"
lunghezza = len(string)
print(lunghezza)

# 2 - upper() e lower() - maiuscole e minuscole
stringa = "Hello, World!"

stringa_maiuscola = stringa.upper()
stringa_minuscola = stringa.lower()
print(stringa_maiuscola)
print(stringa_minuscola)  

# 3 - replace() - sostituisci sottostringa
nuova_stringa = stringa.replace("Hello", "Ciao")
print(nuova_stringa)

# 4 - split() - dividi la stringa in una lista
parole = stringa.split(", ")
print(parole)

# 5 strip() - rimuovi spazi bianchi iniziali e finali
stringa_con_spazi = "     Ciao, Mondo!    "
stringa_senza_spazi = stringa_con_spazi.strip()
print(stringa_senza_spazi)

# METODI CICLICI

# 6
lista_numeri = [1, 2, 3, 4, 5]
for numero in lista_numeri:
    print(numero)

# 7 - while loop - Esegui fino a quando una condizione è vera
contatore = 0
while contatore < 5:
    print(contatore)
    contatore += 1

# 8 - enumerate() - ottieni indice e valore durante l'iterazione
lista_colori = ["rosso", "verde", "blu"]
for indice, colore in enumerate(lista_colori):
    # Questo è un ciclo for che utilizza la funzione enumerate(). Durante ogni iterazione, enumerate() restituisce una tupla contenente l'indice e il valore corrispondente dalla lista. Quindi, indice e colore vengono assegnati rispettivamente all'indice e al valore dell'elemento corrente.
    print(f"Indice: {indice}, Colore: {colore}")
    # Durante ogni iterazione del ciclo, stampiamo un messaggio formattato utilizzando una f-string. La f-string ci consente di inserire direttamente i valori di indice e colore nel testo del messaggio.
