# 1)

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

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

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
#print('Original list', sample_list)

length = len(sample_list) # ottenere la lunghezza della lista
chunk_size = int(length / 3) # dividere la lunghezza per 3 per ottenere il pezzo 'tagliato'
start = 0
end = chunk_size

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
result_set = set(full_list)
print("Result:", result_set)