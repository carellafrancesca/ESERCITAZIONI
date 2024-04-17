# 1)

class Event:
    def __init__(self, event_name, event_date, location):
        self.event_name = event_name
        self.event_date = event_date
        self.location = location

class EventBookingSystem:
    def __init__(self):
        self.event_list = []
    
    def add_event(self, event):
        self.event_list.append(event)
    
    def show_event_list(self):
        print("Lista degli eventi in programmazione")
        for event in self.event_list:
            print(f"{event.name}, sarà il {event.event_date} e avrà come location {event.location}")


    

    
