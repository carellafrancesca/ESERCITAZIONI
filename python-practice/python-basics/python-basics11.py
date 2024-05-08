# 1)

class Calculator:
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mol(self):
        return self.a * self.b
    
    def div(self):
        if self.b == 0:
            print("Non puoi dividere per zero")
            return None
        return self.a / self.b

calc = Calculator()
#calc.a = float(input('Inserisci il primo numero:')) 
#calc.b = float(input('Inserisci il secondo numero:'))

#operation = input ("""
#Scegliere un'operazione: 
#+ , - , * , /
#""")

#if operation == '+':
#    risultato = calc.add()
#elif operation == '-':
#    risultato = calc.sub()
#elif operation == '*':
#    risultato = calc.mol()
#elif operation == '/':
#    risultato = calc.div()
#else:
#    risultato = "Il carattere inserito non è valido"

#print(risultato)    

# 2)

#inputString = str(input("Please type a sentence: "))

def countvowels(inputString):
    num_vowels = 0
    for char in inputString:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels

#print("Number of vowels in the sentence:", countvowels(inputString))

# 3)

mylist = [8, 13, 27, 39, 42, 55, 8, 61, 77, 83, 42, 95, 112, 14, 27, 38, 88, 47]
mylist = list(dict.fromkeys(mylist))
#print(mylist)

# 4)

arr = [1,2,3,4,5,6,7,9,10,11,13,14,15,16,17,19,20]
missing_elements = []
for element in range(arr[0], arr[-1]+1):
    if element not in arr:
        missing_elements.append(element)
#print(missing_elements)

# 5)

class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

class FavMovieList:
    def __init__(self):
        self.movies = []

    def add_movie_to_list(self, movie_title):
        self.movies.append(movie_title)
    
    def remove_movie_from_list(self, movie_title):
        for movie in self.movies:
            if movie.title == movie_title:
                self.movies.remove(movie)
                return True
        return False
    
    def show_fav_movie_list(self):
        for movie in self.movies:
            print(f"{movie.title}, directed by {movie.director}, released in {movie.year}. Genre: {movie.genre}")

fav_movie_list = FavMovieList()
#print("This is a list of my favorite movies:")
movie1 = Movie('Shutter Island', 'Martin Scorsese', '2010', 'Psychological Thriller')
movie2 = Movie('La La Land', 'Damien Chazelle', '2016', 'Musical')
movie3 = Movie('Pride and Prejudice', 'Joe Wright', '2005', 'Drama/Romance')
fav_movie_list.add_movie_to_list(movie1)
fav_movie_list.add_movie_to_list(movie2)
fav_movie_list.add_movie_to_list(movie3)
#fav_movie_list.show_fav_movie_list()
    
# 6)

class Item: 
    def __init__(self, description, isbought):
        self.description = description
        self.isbought = isbought
    
class WishList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def edit_item(self, item_description, item_status):
        for item in self.items:
            if item.description == item_description:
                item.isbought = item_status
                return True
        return False

    def delete_item(self, item_description):
        for item in self.items:
            if item.description == item_description:
                self.items.remove(item)
                return True
        return False
    
    def show_wishlist(self):
        for item in self.items:
            print(f"{item.description}, {item.isbought}")

wishlist = WishList()
wishlist_item = Item('Bambola giocattolo', 'Disponibile')
wishlist_item2 = Item('Tastiera', 'Non Disponibile')
wishlist_item3 = Item('Cuffie', 'Non Disponibile')
wishlist.add_item(wishlist_item)
wishlist.add_item(wishlist_item2)
wishlist.add_item(wishlist_item3)
wishlist.edit_item('Cuffie', 'Disponibile')
#wishlist.show_wishlist()

# 7)

class BankAccount:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount
    
    def get_balance(self):
        return self._balance
    
    def transfer(self, other, amount_out):
        self.withdraw(amount_out)
        other.deposit(amount_out)
    
    def print_info(self):
        first = self._first_name
        last = self._last_name
        number = self._number
        balance = self._balance

        s = f"{first} {last}, {number}, balance: {balance}"
        print(s)
    
def main():

    a1 = BankAccount("Jesse", "Pinkman", "19371554951", 10500)
    a2 = BankAccount("Walter", "White", "19371564853", 9500)

    a1.transfer(a2, 500)
    a1.deposit(2500)
    a2.deposit(8500)

    #a1.print_info()
    #a2.print_info()

main()

# 8)

class Room():
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.booked = False
    
    def book_room(self):
        if not self.booked:
            self.booked = True
            print(f"Room {self.number} booked successfully.")
        else:
            print(f"Room {self.number} is already booked.")
    
    def delete_booking(self):
        if not self.booked:
            self.booked = False
            print(f"Reservation for room {self.number} cancelled successfully")
        else:
            print(f"Room {self.number} is not reserved.")

class Hotel():
    def __init__(self):
        self.rooms = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def show_av_rooms(self):
        print("Available rooms:")
        for room in self.rooms:
            if not room.booked: 
                print(f"Room: {room.number}, Capacity: {room.capacity}")
    
    def book_room(self, room_num, num_people):
        for room in self.rooms:
            if room.number == room_num and not room.booked and room.capacity >= num_people:
                room.book_room()
                return
            #print("Sorry, the requested room is not available.")
    
    def cancel_room_book(self, room_num):
        for room in self.rooms:
            if room.number == room_num:
                room.delete_booking()
                return
            print("Invalid room number.")
        
hotel = Hotel()
room1 = Room(1, 2)
room2 = Room(2, 2)
room3 = Room(3, 1)
room4 = Room(4, 4)
room5 = Room(5, 2)
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)
hotel.add_room(room4)
hotel.add_room(room5)
#hotel.show_av_rooms()
#hotel.book_room(1, 2)
#hotel.show_av_rooms()
#hotel.cancel_room_book(1)
#hotel.show_av_rooms()
