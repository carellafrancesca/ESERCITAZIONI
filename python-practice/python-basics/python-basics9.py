# 1)

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

# lista [ Iniziale : Fine : IndexJump ]

odd_elemets = list1[1::2]
# inizia dal primo index (se 3 = 0, 6 = 1, 9 = 2), con un conteggio che va due a due 
#print('Element at odd-index positions from list one')
#print(odd_elemets)

even_elements = list2[0::2]
# inizia a contare dall'index con 0 (quindi il 4) e anche qui il conteggio va due a due (quindi poi viene preso il 12, il 20, il 28 ...)
#print('Element at even-index positions from list two')
#print(even_elements)

#print("Printing Final third list")
res.extend(odd_elemets)
res.extend(even_elements)
#print(res)

# 2)

num_list = [34, 54, 67, 89, 11, 43, 94]

element = num_list.pop(4)
#print('List After removing element at index 4', num_list)
element = num_list.insert(2, element)
#print('List after Adding element at index 2', num_list)
num_list.append(element)
#print('List after Adding element at last', num_list)

# 3)

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89, 17, 33, 51, 67, 2, 17]
#print('Original list', sample_list)

length = len(sample_list) # ottenere la lunghezza della lista
chunk_size = int(length / 3) # dividere la lista in tre parti (partendo dalla lunghezza della lista per la suddivisione)
start = 0 
end = chunk_size
# start = 0 - end = chunk_size per definire da dove partire, quando nel metodo for in range() definiamo il modo in cui verranno suddivisi i numeri

for i in range(3): # runnare il loop per 3 volte
    indexes = slice(start, end)
    list_chunk = sample_list[indexes]
    #print('Chunk', i, list_chunk)
    #print("After reversing it ", list(reversed(list_chunk)))
    # per ogni iterazione, ottere la parte tagliata grazie al metodo slice() e per invertire le cifre utilizzare reversed()

    start = end
    end += chunk_size
    # per ogni iterazione, il valore di inizio e di fine cambieranno

# 4)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
       count_dict[item] = 1 

#print("Printing count of each item  ", count_dict)

# 5)

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
third_list = [12, 14, 18, 20, 24, 30, 32]

full_list = zip(first_list, second_list, third_list)
# zip() è una funzione che prende gli iterabili (possono essere zero o più), li aggrega in una tupla e li restituisce
result_set = set(full_list) # set() viene utilizzato per convertire qualsiasi elemento iterabile in una sequenza di elementi iterabili con elementi distinti, comunemente chiamati set 
#print("Result:", result_set)

# 6)

def multiplication_or_sum(num_1, num_2):
    product = num_1 * num_2

    if product <= 1000:
        return product
    else:
        return num_1 + num_2

result = multiplication_or_sum(20, 30)
result_2 = multiplication_or_sum(50, 60)
#print("Result:", result)
#print("Result:", result_2)

# 7)

previous_num = 0
#print("Stampa della somma dei numeri correnti e precedenti in un intervallo (10)")

for i in range(10):
    sum = previous_num + i
    #print("Numero corrente:", i, "Numero precedente:", previous_num, "Somma:", sum)
    previous_num = i

# 8)

#word = input('Enter word:')
#print("Original String:", word)
#string_len = len(word)

#print("Printing only even index chars")

#x = list(word)
#for i in x[0::2]:
#    print(i)

#for i in range(0, string_len -1, 2): # 0 per partire dal primo carattere, string_len -1 perché l'index inizia con lo 0, 2 per prendere il carattere presente all'indice pari come 0,2,4...
    #print("index[",i,"]", word[i])

# 9)

def remove_chars(word, n):
    #print('Original string:', word)
    x = word[n:]
    return x

#print("Removing characters froma string")
#print(remove_chars("pynative", 4))
#print(remove_chars("pynative", 2))

# 10)

def num_check(numberList):
    #print ('Elenco fornito:', numberList)
    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
#print("Il risultato è", num_check(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
#print("Il risultato è", num_check(numbers_y))

# 11) 

list_num = [10, 20, 33, 46, 55, 64, 70, 82, 95]
#print("L'elenco fornito è", list_num)
#print("Divisibile per 5:")
#for num in list_num:
    #if num % 5 == 0:
        #print(num)

# 12)

string = ("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.")
count_string = string.count("Lorem Ipsum")
#print("Il termine Lorem Ipsum è comparso", count_string, "volte")

# 13) - STRINGHE

#str1, str2, str3 = input("Enter three string:").split()
#print('Name1:', str1)
#print('Name2:', str2)
#print('Name3:', str3)

#quantity = 3
#totalMoney = 1000
#price = 450
#statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
#print(statement1.format(quantity, totalMoney, price))

# 14)

numbers = [12, 75, 150, 180, 145, 525, 50]

#for item in numbers:
#    if item > 500:
#        break
#    elif item > 150:
#        continue
#    elif item % 5 == 0:
#        print(item)

# 15)

#def func1(*args): # *args è usato per passare alla funzione una serie di valori senza che siano nominati i parametri
    #for i in args:
        #print(i)

#func1(20, 40, 60)
#func1(80, 100)

# 16)

def outer_fun(a,b):
    def addition(a,b):
        return a + b
    
    add = addition(a, b)
    return add + 5

result = outer_fun(5, 10)
#print(result)

# 17)

def display_student(name, age):
    print(name, age)

#display_student("Emma", 26)
show_student = display_student
#show_student("Emma", 26)

# 18)

x = [4, 6, 8, 24, 12, 2]
#print(max(x))

# 19)

def get_middle_three_Chars(str1):
    #print("Original String is", str1)
    middle = int(len(str1) / 2)
    res = str1[middle - 1:middle + 2]
    #print("Middle three chars are:", res)

get_middle_three_Chars("JhonDipPeta")
get_middle_three_Chars("JaSonAy")