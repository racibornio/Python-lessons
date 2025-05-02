dict_1 = {}
print("Empty dictionary 1:", dict_1)

for iter in range(0, 5):
    value = input("Value:")
    dict_1[iter] = value

print("Dictionary with 1st data pair:", dict_1)

dict_2 = {}
print("Empty dictionary 2:", dict_1)

for i in range(1, 6):
    key = input("Key:")
    value = input("Value:")
    dict_2[key] = value


print("Dictionary 2:", dict_2)