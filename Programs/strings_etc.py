file_path = r"C:\Users\pos\Documents\Python\Python-lessons\files\new_text_file"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print('The file content')
    print(content)


my_test_string = 'fjdoas fdsa jf fjlsdak lfdskja fdjal lfdja'
print(my_test_string.upper())
print(my_test_string.lower())
print(my_test_string.title())
updated_my_test_string = my_test_string.replace('jf', 'xx')
print(updated_my_test_string)
decorated = updated_my_test_string.split(' ')
print(decorated)

string_immutability_test = 'fda'
print(string_immutability_test)
string_immutability_test = 'f'
print(string_immutability_test)