#immutable, ordered, iterable, can be a key in dictionary
#values can repeat
#useful for returning multiple values from functions, keys in dictionaries
from email.policy import default
from itertools import count
from operator import index
from xml.etree.ElementTree import tostring

empty_tuple = tuple()
print('Empty tuple', empty_tuple)

krotka1int = (0, 1, 2, 3, 2, 1, 11)
print('Krotka', krotka1int)

#cannot:
#krotka1int[0] = 1

print('Tuple index 0', krotka1int.index(krotka1int[0]))
print('Tuple index last', krotka1int.index(krotka1int[-1]))

value_to_check =  1
print(value_to_check, 'occurs', krotka1int.count(value_to_check), 'times')

print('Tuple lenght is', len(krotka1int))

def do_math_calculations(number_to_calculate):
    divided_by_half = number_to_calculate / 2
    multiplied_by_two = number_to_calculate * 2
    return (divided_by_half, multiplied_by_two)


tuple_outcome = do_math_calculations(12)
print('The outcome is', tuple_outcome)