# 1)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

#for x, y in zip(list1, list2[::-1]): # [::-1] inidica di partire dalla fine (in questo caso nella seconda lista)
    #print(x,y)

# 2)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1)) # dalla lista, prendere/filtrare gli elementi che hanno 'None' come valore per 'rimuoverli'
#print(res)

# 3)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
list1[2][2].append(7000)
#print(list1)

# 4)

list_num = [5, 10, 15, 20, 25, 50, 20]
index = list_num.index(20)
list_num[index] = 200
#print(list_num)

# 5)

list_ = [5, 20, 15, 20, 25, 50, 20, 60, 15, 30, 20]

while 20 in list_:
    list_.remove(20)
#print(list_)

# 6)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
# dict() questa funzione crea un dizionario cioè una raccolta non ordinata, modificabile e indicizzata
# zip() è una funzione che prende gli iterabili (possono essere zero o più), li aggrega in una tupla e li restituisce
#print(res_dict)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Fourty': 40, 'Fifty': 50, 'Sixty': 60}
dict3 = {**dict1, **dict2} # ** = è un operatore utilizzato per unire due dizionari. La sintassi "**" viene spesso utilizzata in Python con l'abbreviazione "**kwargs"
#print(dict3)

# 7)

employees = ['Kelly', 'Emma', 'Lucy']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults) # fromkeys() questo metodo restituisce un dizionario con le chiavi e il valore specificati
#print(res) 

# 8)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

newDict = {ky: sample_dict[ky] for ky in keys}
#print(newDict)

for ky in keys:
    sample_dict.pop(ky)
    #print(sample_dict)

# 9)

num_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

#if 300 in num_dict.values():
    #print('300 is present in a dict')

# 10)

person_dict = {
  "name": "Kelly",
  "lastname": "Clarkson",
  "age":25,
  "salary": 8000,
  "city": "New york",
}

person_dict['location'] = person_dict.pop('city')
#print(person_dict)

# 11)

el_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}

#print(min(el_dict, key = el_dict.get))
#print(max(el_dict, key = el_dict.get))

# 12)

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 7500},
    'emp4': {'name': 'Jeff', 'salary': 500}
}

sample_dict['emp4']['salary'] = 7500
#print(sample_dict)

# 13)

color_set = {"Yellow", "Orange", "Black", "Purple"}
color_list = ["Blue", "Green", "Red", "White"]

color_set.update(color_list)
#print(color_set)

# 14)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

#new_set = set1.intersection(set2)
#print(new_set)

#both_set = set1.union(set2)
#print(both_set)

#set1.difference_update(set2)
#print(set1)

#set3.difference_update({90, 100})
#print(set3)

#print(set1.symmetric_difference(set2))

#if set1.isdisjoint(set2):
#    print("Two sets have no items in common")
#else:
#    print("Two sets have items in common")
#    print(set1.intersection(set2))

#set1.symmetric_difference_update(set2)
#print(set1)

#set1.intersection_update(set2)
#print(set1)

# 15)

tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
#print(tuple1)

tuple_elements = ("Orange", [10, 20, 30], (5, 15, 25))
# understand indexing
# tuple_elementstuple_elements[0] = 'Orange'
# tuple_elements[1] = [10, 20, 30]
# list1[1][1] = 20

#print(tuple_elements[1][1])
#print(tuple_elements[2][1])

tuple_num = (10, 20, 30, 40, 50)
a, b, c, d, e = tuple_num
#print(a) 
#print(b) 
#print(c) 
#print(d) 
#print(e)

tuple_num1 = (11, 22)
tuple_num2 = (99, 88)
#print(tuple_num1)
#print(tuple_num2)
#tuple_num1, tuple_num2 = tuple_num2, tuple_num1
#print(tuple_num1)
#print(tuple_num2)

tuple_numbers = (11, 22, 33, 44, 55, 66)
#tuple_numbers_2 = tuple_numbers[3:-1]
#print(tuple_numbers_2)

tuple_nested_numbers = (11, [22, 33], 44, 55, 66)
#tuple_nested_numbers[1][0] = 222
#print(tuple_nested_numbers)

tuple_multiple_num = (15, 8, 26, 31, 38, 15, 47, 51, 64, 15, 77, 81, 97, 15, 104)
#print(tuple_multiple_num.count(15))

##def check(t):
#    return all(i == t[0] for i in t)

#tuple_same_num = (45, 45, 45, 45)
#print(check(tuple_same_num))