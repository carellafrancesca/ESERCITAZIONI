from datetime import datetime, date
#import datetime

# 1)

class Student:
    def __init__(self, full_name):    
        self.full_name = full_name
        self.grades_list = []
    
    def add_grade(self, grade):
        self.grades_list.append(grade)
    
    def average(self):
        if self.grades_list:
            return sum(self.grades_list) / len(self.grades_list)
        else:
            None

class Register:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.full_name] = student
    
    def add_grade(self, student_name, grade):
        if student_name in self.students :
            self.students[student_name].add_grade(grade) 
        else:
            print('Non ci sono studenti con questo nome: {student_name} sul registro')

    def student_average(self, student_name):
        if student_name in self.students:
            return self.students[student_name].average()
        else:
            print('Non ci sono studenti con questo nome: {student_name} sul registro')
    
    def class_average(self):
        average_class = [student.average() for student in self.students.values() if student.average() is not None]
        if average_class:
            return sum(average_class) / len(average_class)
        else:
            return None
        
#student1 = Student('Mario Rossi')
#student2 = Student('Giuseppe Verdi')
#student3 = Student('Francesca Rosa')

#register = Register()
#register.add_student(student1)
#register.add_student(student2)
#register.add_student(student3)
#register.add_grade('Mario Rossi', 6)
#register.add_grade('Mario Rossi', 8)
#register.add_grade('Giuseppe Verdi', 5)
#register.add_grade('Giuseppe Verdi', 6.5)
#register.add_grade('Francesca Rosa', 7)
#register.add_grade('Francesca Rosa', 8)

#print('La media di Mario Rossi:', register.student_average('Mario Rossi'))
#print('La media di Giuseppe Verdi:', register.student_average('Giuseppe Verdi'))
#print('La media di Francesca Rosa:', register.student_average('Francesca Rosa'))
#print('La media della classe:', register.class_average())

# 2)

class Table():
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.reserved = False
    
    def reserve_table(self):
        if not self.reserved:
            self.reserved = True
            print(f"Table {self.number} reserved successfully.")
        else:
            print(f"Table {self.number} is already reserved.")
    
    def delete_reservation(self):
        if not self.reserved:
            self.reserved = False
            print(f"Reservation for table {self.number} cancelled successfully")
        else:
            print(f"Table {self.number} is not reserved.")

class Restaurant():
    def __init__(self):
        self.tables = []
    
    def add_table(self, table):
        self.tables.append(table)
    
    def show_av_tables(self):
        print("Available tables:")
        for table in self.tables:
            if not table.reserved:
                print(f"Table: {table.number}, Capacity: {table.capacity}")
    
    def reserve_table(self, table_number, num_people):
        for table in self.tables:
            if table.number == table_number and not table.reserved and table.capacity >= num_people:
                table.reserve_table()
                return
            print("Sorry, the requested table is not available.")

    def cancel_table_res(self, table_number):
        for table in self.tables:
            if table.number == table_number:
                table.delete_reservation()
                return
            print("Invalid table number.")
            
#restaurant = Restaurant()
#table1 = Table(1, 4)
#table2 = Table(2, 4)
#table3 = Table(3, 6)
#table4 = Table(4, 8)
#table5 = Table(5, 4)
#table6 = Table(6, 4)
#table7 = Table(7, 2)
#table8 = Table(8, 2)
#restaurant.add_table(table1)
#restaurant.add_table(table2)
#restaurant.add_table(table3)
#restaurant.add_table(table4)
#restaurant.add_table(table5)
#restaurant.add_table(table6)
#restaurant.add_table(table7)
#restaurant.add_table(table8)
#restaurant.show_av_tables()
#restaurant.reserve_table(1, 4)
#restaurant.cancel_table_res(1)
#restaurant.show_av_tables()

# 3)

#now = datetime.now() # prende la data di oggi
#print("Enter your date of birth (YYYY-MM-DD):")
#dob_input  = input()
#birthday = datetime.strptime(dob_input, "%Y-%m-%d") #per parsare ciò che ha inserito l'utente in un oggetto data
#difference = now - birthday 
#age_in_years = difference.days // 365 # calcola l'età di una èersona in anni
#print(f"You are {age_in_years} years old.")

# 4)

def num_of_days(date1, date2):
    if date2 > date1:
        return (date2-date1).days
    else:
        return (date1-date2).days

date1 = date(2020, 12, 13)
date2 = date(2022, 4, 22)
#print(num_of_days(date1, date2), "days")

# 5)

#intDay = datetime.date(year=2021, month=4, day=12).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#print(days[intDay])

# 6)

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%d %m %Y')
    day_num = date_obj.weekday()
    return day_num >= 5

def day_of_week(date_str):
    date_obj = datetime.strptime(date_str, '%d %m %Y')
    day_num = date_obj.weekday()
    return day_num

date_str = '13 07 2021'
weekday_num = day_of_week(date_str)

#if is_weekend(date_str):
#    print(f"It's a weekend.")
#else: 
#    print(f"It's a weekday.")

# 7)

#year = int(input("Input year: "))

#if year % 4 == 0:
#    print("Year is leap.")
#    if year % 100 == 0 and year % 400 != 0:
#        print ("Year is common.")
#else:
#    print("Year is common.")

# 8)

inputDateList = ['23-07-2021', '05-06-2023', '15-11-2018', '02-01-2022', '30-12-2020', '13-04-2025']
inputDateList.sort(key=lambda date : datetime.strptime(date, "%d-%m-%Y"))
#print("List Sorting by Date:\n", inputDateList)
