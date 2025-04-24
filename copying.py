import copy

my_list = ['A', 'B', 'C', 'D']
print('my_list list id:', id(my_list), 'values:', my_list)

another_list = copy.copy(my_list)
print('my_list list id:', id(my_list), 'values:', my_list)
print('another_list list id:', id(another_list), 'values:', another_list)

list_copied_deeply = copy.deepcopy(my_list)
print('deeply copied list id:', id(list_copied_deeply), 'values:', list_copied_deeply)

another_list[1] = 'XXX'
print('my_list', my_list)
print('another_list', another_list)

lista1 = [[1, 2], [3, 4]]
lista2 = copy.copy(lista1)
lista2[0][0] = 99
print(lista1)  # [[99, 2], [3, 4]]

lista3 = [[5, 6], [7, 8]]
lista4 = copy.deepcopy(lista3)
lista4[0][0] = 99

print(lista3)  # [[1, 2], [3, 4]]

