#immutable, ordered, iterable, can be a key in dictionary
#values can repeat
#useful for returning multiple values from functions, keys in dictionaries

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

print('Tuple length is', len(krotka1int))

def do_math_calculations(number_to_calculate):
    divided_by_half = number_to_calculate / 2
    multiplied_by_two = number_to_calculate * 2
    division_outcome = str(divided_by_half)
    div_out_text = print('Division:', division_outcome)
    multiplication_outcome = str(multiplied_by_two)
    mult_out_text = print('Multliplicaiton:', multiplication_outcome)
    return (div_out_text, mult_out_text)

do_math_calculations(12)
tuple_to_list = list(do_math_calculations(44))
print('Tuple to list:', tuple_to_list, 'and its id is:', id(tuple_to_list))

