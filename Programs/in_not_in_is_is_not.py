list_one = [4, 6, 7, 3, 55, 3, 6, 111, 2]

a_number = 5
b_number = 111

print('a_number == b_number?', a_number is b_number)
print('a_number != b_number?', a_number is not b_number)

a_number = b_number

print('After "a_number = b_number" a_number == b_number?', a_number is b_number)
print('After "a_number = b_number" a_number != b_number?', a_number is not b_number)

if a_number in list_one:
    print(a_number, 'occurs')
else:
    print(a_number, 'doesn not occur')


if b_number not in list_one:
    print(b_number, 'does not occur')
else:
    print(b_number, 'occurs')


