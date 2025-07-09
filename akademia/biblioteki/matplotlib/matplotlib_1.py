import matplotlib.pyplot as plt
from faker import Faker
import random
import pandas as pd

fake = Faker()

plt.plot([0, 1, 2, 3, 4, 5])
plt.ylabel("Numbers")
plt.show()


plt.plot([1, 2, 3], [4.5, 9, 13.5])
plt.ylabel("Numbers")
plt.show()


plt.plot([1, 2, 3], [4.5, 9, 13.5], 'ro')
plt.axis((1, 3, 1, 15))
plt.show()


xs, xs2, xs3 = [], [], []

for i in range(0, 25):
    x = i * 0.2
    xs.append(x)
    xs2.append(x ** 2)
    xs3.append(x ** 3)


plt.plot(xs, xs, 'r--', xs, xs2, 'bo', xs, xs3, 'g^')
plt.show()


data = {
    "x" : [],
    "y" : [],
    "color" : [],
    "size" : []
}

for i in range(0, 100):
    data["x"].append(random.random())
    data["y"].append(random.randint(0, 50))
    data["color"].append(random.random())
    data["size"].append(random.random() * 100)


plt.scatter('x', 'y', c='color', s='size', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.bar(names, values)
plt.scatter(names, values)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()