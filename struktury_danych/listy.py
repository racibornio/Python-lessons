#mutable, ordered, iterable, cannot be a key in dictionary unless with 'frozenset'
#values can repeat

list_of_intigers = [0, 1, 2, 3, 4, 5]
list_of_strings = ["a", "b", "c"]
list_of_bools = [True, True, False, True]
empty_list = []
print('Empty list', empty_list)

print(list_of_intigers)
print(list_of_intigers[0])
print(list_of_intigers[-1]) #print last item

list_of_intigers.append(6) #add an element at the end
print('6th position added', list_of_intigers)

list_of_intigers.insert(1, 0.5) #adds an element on an indicated index with an indicated value
print('new 1st position added', list_of_intigers)

del list_of_intigers[1] #deletes an indicated index
print('New 1st position deleted', list_of_intigers)

popped_value = list_of_intigers.pop() #deletes an indicated index but allows to work with an item yet
print('Last position popped', list_of_intigers)
print('Popped value', popped_value)

list_of_intigers.pop(3) #deletes an indicated index
print('3rd position popped', list_of_intigers)

value_to_remove = 4
list_of_intigers.remove(value_to_remove) #removes by the value - removes only the first occurence
print(value_to_remove, 'removed by value:', list_of_intigers)

removed_value = "c"
list_of_strings.remove(removed_value) #also allows to work with an item yet - removes only the first occurence
print(removed_value, "has been removed.")

print(list_of_strings)

list_of_lists = [ [1, 3, 5, 7, 9], [2, 4, 6, 8, 0], ['a', 'e', 'i', 'o', 'u'], ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'] ]

print(list_of_lists[0][0],list_of_lists[1][0],list_of_lists[2][0],list_of_lists[3][0])

mute_list = [0]
print('Initial mute_list', mute_list)
mute_list[0] = 1
print('mute_list after mutation', mute_list)