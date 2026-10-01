import random

letter_o = 'o'
o_counter = 0
letter_r = 'r'
r_counter = 0

for i in range(1000):

    chosen_letter = random.choice(['o', 'r'])
    print(chosen_letter)

    if chosen_letter == 'o':
        o_counter += 1
    else:
        r_counter += 1


probability_o = o_counter / 1000 * 100
probability_r = r_counter / 1000 * 100

print('"o" occured', o_counter, 'times so it is', probability_o, '%')
print('"r" occured', r_counter, 'times so it is', probability_r, '%')