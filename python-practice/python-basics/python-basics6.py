import random
import string

# 1)

class Prodotto:
    def __init__(self, nome, prezzo, quantita) :
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

class Inventario:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)
    
    def rimuovi_prodotto(self, nome_prodotto):
        for prodotto in self.prodotti:
            if prodotto.nome == nome_prodotto:
                self.prodotti.remove(prodotto)
                return True
        return False
    
    def modifica_prodotto(self, nome_prodotto, nuovo_prezzo, nuova_quantita):
        for prodotto in self.prodotti:
            if prodotto.nome == nome_prodotto:
                prodotto.prezzo = nuovo_prezzo
                prodotto.quantita = nuova_quantita
                return True
        return False

    def visualizza_inventario(self):
        for prodotto in self.prodotti:
            print(f"{prodotto.nome}: Prezzo: {prodotto.prezzo}, Quantità: {prodotto.quantita}")

inventario = Inventario()
prodotto1 = Prodotto('Laptop', 800, 15)
prodotto2 = Prodotto('IPhone', 900, 10)
prodotto3 = Prodotto('Tablet', 500, 10)
prodotto4 = Prodotto('Cuffie', 500, 10)
prodotto5 = Prodotto('Libri', 15, 20)
inventario.aggiungi_prodotto(prodotto2)
inventario.aggiungi_prodotto(prodotto3)
inventario.aggiungi_prodotto(prodotto4)
inventario.aggiungi_prodotto(prodotto5)
#inventario.modifica_prodotto('IPhone', 1000, 10)
#inventario.modifica_prodotto('Cuffie', 200, 20)
#inventario.rimuovi_prodotto('Libri')
#inventario.visualizza_inventario()

# 2)

valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Regina', 'Re', 'Asso']
semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']

class Carta:
    def __init__(self, valore, seme):
        self.valore = valore
        self.seme = seme

class Mazzo:
    def __init__(self):
        self.mazzo = [Carta(valore, seme) for valore in valori for seme in semi]
        random.shuffle(self.mazzo)

    def pesca_carta(self):
        if len(self.mazzo) > 0:
            return self.mazzo.pop()
        else:
            return 'Questa carta non è nel mazzo'
        
mazzo = Mazzo()
carta1 = mazzo.pesca_carta()
carta2 = mazzo.pesca_carta()
carta3 = mazzo.pesca_carta()
#print(f"Carta 1: {carta1.valore} di {carta1.seme}")
#print(f"Carta 2: {carta2.valore} di {carta2.seme}")
#print(f"Carta 3: {carta3.valore} di {carta3.seme}")

# 3)

class Book: 
    def __init__(self, title, author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability
    
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print("Book borrowed successfully!")
        else:
            print("The book is not available")
    
    def return_book(self):
        self.availability = True
        print('You returned the book')

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_book(self, title, author):
        for book in self.books:
            if book.title == title or book.author == author:
                return book
        return None
    
    def show_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Availability: {book.availability}")

library = Library()
book1 = Book('Orgoglio e Pregiudizio', 'Jane Awsten')
book2 = Book('Il Ritratto di Dorian Gray', 'Oscar Wilde', availability = False)
book3 = Book('Persone Normali', 'Sally Rooney')
book4 = Book('Harry Potter', 'J.K.Rowlig', availability=False)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
#library.show_books()
#book3.borrow_book()
#library.show_books()
#book3.return_book()
#library.show_books()

# 4)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
# random.choice() e' una funzione fornita dal modulo 'random' di Python che permette di selezionare casualmente un elemento da una sequenza 

#password = generate_password(12)
#print ("Password generata:", password)

# 5)

class Character:
    def __init__(self, name, health) :
        self.name = name
        self.health = health

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

class Player(Character):
    def __init__(self, name, health, level):
        super().__init__(name, health)
        self.level = level

#player1 = Player('Player', 100, 10)
#player2 = Enemy('Enemy', 200, 20)

# 6)

class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def edit_task(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                return True
        return False
    
    def delete_completed_tasks(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def show_task_list(self):
        print(f"Tasks per il progetto '{self.name}':")
        for task in self.tasks:
            print(f" {task.name} : {task.status}")

project = Project('Progetto')
task1 = Task('Finire il progetto', 'In corso')
task2 = Task('Consegnare il progetto', 'Da fare')
project.add_task(task1)
project.add_task(task2)
#project.show_task_list()

# 7)

class Flight:
    def __init__(self, flight_num, destination, departure_time):
        self.flight_num = flight_num
        self.destination = destination
        self.departure_time = departure_time

class Book_Flight:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_flight(self, flight_num):
        for flight in self.flights:
            if flight.flight_num == flight_num:
                return flight
        return None
    
    def cancel_flight(self, flight_num):
        for flight in self.flights:
            if flight.flight_num == flight_num:
                self.flights.remove(flight)
                print(f"Il volo {flight_num} è stato cancellato")
                return 
            print(f"Volo {flight_num} non trovato")
        
    def show_flights(self):
        print("Lista dei voli")
        for flight in self.flights:
            print(f"Numero del volo: {flight.flight_num}, Destinazione: {flight.destination}, Ora di partenza: {flight.departure_time}")

booked_flight = Book_Flight()
flight1 = Flight('ABC123', 'Roma', '15:00')
flight2 = Flight('DEF456', 'Milano', '19:30')
flight3 = Flight('GHI789', 'Parigi', '10:15')
booked_flight.add_flight(flight1)
booked_flight.add_flight(flight2)
booked_flight.add_flight(flight3)
#booked_flight.cancel_flight('GHI789')
#booked_flight.show_flights()

# 8)

class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre 
        self.duration = duration

class Cinema:
    def __init__(self):
        self.movie_list = []
        self.bookings = []
    
    def add_movie(self, movie):
        self.movie_list.append(movie)
    
    def book_a_seat(self, title, seat_number):
        if title in self.bookings:
            self.bookings[title].append(seat_number)
        else:
            self.bookings[title] = [seat_number] # Crea una nuova voce nel dizionario delle prenotazioni con il titolo del film come chiave e una lista contenente il posto prenotato come valore
    
    def show_movies(self):
        print("Lista dei film in programmazione:")
        for movie in self.movie_list:
            print(f" Film : {movie.title}, Genere : {movie.genre}, Durata : {movie.duration}")

    def show_bookings(self):
        print("Prenotazioni:")
        for movie_title, seats in self.bookings:
            print(f"Film: {movie_title}, Posti prenotati: {', '.join(seats)}")


cinema = Cinema()
movie1 = Movie('La La Land', 'Musical', '2h 8m')
movie2 = Movie('Shutter Island', 'Thriller', '2h 18m')
movie3 = Movie('Avengers: Endgame', 'Action', '3h 2m')
cinema.add_movie(movie1)
cinema.add_movie(movie2)
#cinema.show_movies()
#cinema.book_a_seat("La La Land", "A1")
#cinema.book_a_seat("La La Land", "A2")
#cinema.book_a_seat("Avengers: Endgame", "B4")
#cinema.show_bookings()