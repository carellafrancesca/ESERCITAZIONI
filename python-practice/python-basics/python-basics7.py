import re
import string

# 1)

class Event:
    def __init__(self, event_name, event_date, location):
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.seats_available = 100

class EventBookingSystem:
    def __init__(self):
        self.event_list = []
    
    def add_event(self, event):
        self.event_list.append(event)

    def book_a_seat(self, event_name, seats_available_num):
        for event in self.event_list:
            if event_name == event_name:
                if event.seats_available >= seats_available_num:
                    event.seats_available -= seats_available_num
                    print(f"Prenotazione effettuata per {seats_available_num} posti all'evento {event_name}")
                else:
                    print("Spiacenti, non ci sono abbastanza posti disponibili per questo evento.")
            return
        print(f"Evento '{event_name}' non trovato.")

    
    def show_event_list(self):
        print("Lista degli eventi in programmazione")
        for event in self.event_list:
            print(f"{event.event_name}, sarà il {event.event_date} e avrà come location {event.location}")

#booking = EventBookingSystem()
#event1 = Event('Concerto dei Coldplay', '15/07/2024', 'Stadio Olimpico - Roma')
#booking.add_event(event1)
#booking.book_a_seat('Concerto dei Coldplay', 5)
#booking.show_event_list()

# 2)

class ShoppingItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

class ShoppingList:
    def __init__(self):
        self.products = []
    
    def add_to_chart(self, product):
        for existing_product in self.products:
            if existing_product.name == product.name and existing_product.item_id == product.item_id:
                # se l'articolo è già presente nel carrello, aggiorna la quantità e il prezzo
                existing_product.quantity += product.quantity
                existing_product.price += product.price 
                return
        self.products.append(product)
        #print(f"Added item with ID {product.item_id} to the chart.")
    
    def remove_from_chart(self, item_id):
        for product in self.products:
            if product.item_id == item_id:
                #print(f"Found item with ID: {item_id}")
                if product.quantity > 1:
                    product.quantity -= 1
                else:
                    self.products.remove(product)
                print("Item removed successfully.")
                return True
        print("Item not found.")
        return False
    
    def calucate_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price * product.quantity
        return total_price

    def show_chart(self):
        for product in self.products:
            print(f"{product.name}: Prezzo: {product.price}, Quantità: {product.quantity}")

#list = ShoppingList()
#item1 = ShoppingItem(1, 'Cuffie', 1, 90)
#item2 = ShoppingItem(2, 'Computer', 1, 900)
#item3 = ShoppingItem(3, 'Libro', 1, 15)
#item4 = ShoppingItem(4, 'Cuffie', 1, 90)
#list.add_to_chart(item1)
#list.add_to_chart(item2)
#list.add_to_chart(item3)
#list.add_to_chart(item4)
#list.remove_from_chart(4)
#total_price = list.calucate_total_price()
#list.show_chart()
#print('Totale del carrello:', total_price)

# 3)

class Recipe():
    def __init__(self, dish_name, ingredients, timing):
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.timing = timing

class Recipe_Book():
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self, recipe):
        self.recipe_list.append(recipe)

    def search_recipe(self, ingredients, timing):
        for recipe in self.recipe_list:
            if recipe.ingredients == ingredients or recipe.timing == timing:
                return recipe
            return None
    
    def edit_recipe(self, recipe_name, new_ingredients, new_timing):
        for recipe in self.recipe_list:
            if recipe.dish_name == recipe_name:
                recipe.ingredients = new_ingredients
                recipe.timing = new_timing
                return True
        return False
    
    def delete_recipe(self, recipe_name):
        for recipe in self.recipe_list:
            if recipe.dish_name == recipe_name:
                self.recipe_list.remove(recipe)
                return True
        return False
    
    def show_recipe_list(self):
        for recipe in self.recipe_list:
            print(f"Piatto: {recipe.dish_name}, Ingredienti: {recipe.ingredients}, Tempo: {recipe.timing}")
        
#recipe_book = Recipe_Book()
#ingredients1 = ['250ml di Latte', '200g di Farina00', '65g di Zucchero', '1 Uovo', '1 cucchiaino di Lievito in polvere']
#recipe1 = Recipe('Pancakes', ingredients1, '10')
#recipe_book.add_recipe(recipe1)
#recipe_book.show_recipe_list()

# 4) 

class PhoneNumber():
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number

class Phone_Book():
    def __init__(self):
        self.phone_book = []
    
    def add_contact(self, phone_number):
        self.phone_book.append(phone_number)
    
    def show_phone_book(self):
        for phone_number in self.phone_book:
            print(f"Contatto: {phone_number.full_name}, Numero: {phone_number.phone_number}")
    
    def search_phone_number(self, full_name, phone_number):
        for phone_number in self.phone_book:
            if phone_number.phone_number == phone_number or phone_number.full_name == full_name:
                return phone_number
            return None
    
    def edit_phone_number(self, updated_full_name, updated_phone_number):
        for phone_number in self.phone_book:
            if phone_number.full_name == updated_full_name:
                phone_number.phone_number = updated_phone_number
                return True
        return False
    
    def delete_phone_number(self, contact_name):
        for phone_number in self.phone_book:
            if phone_number.full_name == contact_name:
                self.phone_book.remove(phone_number)
                return True
        return False
    
#phone_book = Phone_Book()
#contact1 = PhoneNumber('Mario Rossi', '123456789')
#contact2 = PhoneNumber('Giuseppe Verdi', '123456789')
#contact3 = PhoneNumber('Maria Neri', '654321789')
#phone_book.add_contact(contact1)
#phone_book.add_contact(contact2)
#phone_book.add_contact(contact3)
#phone_book.edit_phone_number('Giuseppe Verdi', '987654321')
#phone_book.delete_phone_number('Maria Neri')
#phone_book.show_phone_book()

# 5)

def email_validator(email):
    valid_email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not re.search(valid_email_regex, email):
        return False
    return True

def password_validator(password):
    if len(password) < 8 and re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search("[0-9]", password):
        return True
    return False

#email = input('Inserisci una email:')
#if email_validator(email):
#    print ("L'email è valida")
#else:
#    print("L'email non è valida")

#password = input('Inserisci una password:')
#if password_validator(password):
#    print ("La password è valida")
#else:
#    print("La password non è valida")

# 6)

def analizza_testo(testo):
    # rimuovere la punteggiatura e suddividere il testo in parole
    parole = testo.translate(str.maketrans('','', string.punctuation)).split()
    # translate() : restituisce una stringa in cui alcuni caratteri specificati vengono sostituiti con il carattere descritto in un dizionario o una tabella di mappatura
    # maketrans() : restituisce una tabella di mappatura che può essere utilizzata con il metodo per sostituire i caratteri specificati
    num_parole = len(parole)

    # conta le frasi, tenendo conto della punteggiatura specificata
    num_frasi = testo.count('.') + testo.count('!') + testo.count('?')

    #print("Statistiche del testo:")
    #print("Numero di parole:", num_parole)
    #print("Numero di frasi:", num_frasi)

#testo = input('Inserisci il testo da analizzare:')
#analizza_testo(testo)