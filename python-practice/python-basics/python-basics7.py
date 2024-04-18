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
            print(f"{event.name}, sarà il {event.event_date} e avrà come location {event.location}")

# 2)

class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class ShoppingList:
    def __init__(self):
        self.products = []
    
    def add_to_chart(self, product):
        for existing_product in self.products:
            if existing_product.name == product.name:
                # se l'articolo è già presente nel carrello, aggiorna la quantità e il prezzo
                existing_product.quantity += product.quantity
                existing_product.price += product.price 
                return
        self.products.append(product)
    
    def remove_from_chart(self, product_name):
        for product in self.products:
            if product.name == product_name:
                if product.quantity > 1:
                    product.quantity -= 1
                else:
                    self.products.remove(product)
                return True
        return False
    
    def show_chart(self):
        for product in self.products:
            print(f"{product.name}: Prezzo: {product.price}, Quantità: {product.quantity}")

#list = ShoppingList()
#item1 = ShoppingItem('Cuffie', 1, 90)
#item2 = ShoppingItem('Cuffie', 1, 90)
#item3 = ShoppingItem('Libro', 1, 10)
#item4 = ShoppingItem('Microfono', 1, 150)
#list.add_to_chart(item1)
#list.add_to_chart(item2)
#list.add_to_chart(item3)
#list.add_to_chart(item4)
#list.remove_from_chart(item2)
#list.show_chart()

# 3)

