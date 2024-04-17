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


    

    
