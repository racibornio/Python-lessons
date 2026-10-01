import random

list_one = []

for i in range(0, 10):
    list_one.append(random.randint(0, 100))
    print('Just added', list_one[i], 'List content:', list_one)


def a_tuple():
    a = random.randint(-100, 100)
    b = random.randint(-300, -200)
    c = random.randint(100, 2000)
    return a, b, c

print(a_tuple())

tuple_result = a_tuple()
print(tuple_result)