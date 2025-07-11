import matplotlib.pyplot as plt
from faker import Faker
import random
import pandas as pd
import numpy as np

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


plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("A few charts in one object")
plt.show()


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('IQ')
plt.ylabel("Probability")
plt.title('IQ histogramme')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


names = [fake.name() for _ in range(10)]
values = []
for _ in range(10):
    values.append(random.randint(0, 100))


plt.barh(names, values)
plt.show()



x = [random.uniform(0, 10) for _ in range(100)]
y = [random.uniform(0, 10) for _ in range(100)]
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', alpha=0.6)
ax.set_title('Scatter plot 1')
ax.set_xlabel('X Axis 1')
ax.set_ylabel('Y Axis 1')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.grid(True)
plt.show()



x1 = [random.uniform(0, 10) for _ in range(100)]
y1 = [random.uniform(0, 10) for _ in range(100)]
x2 = [random.uniform(0, 10) for _ in range(100)]
y2 = [random.uniform(0, 10) for _ in range(100)]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(x1, y1, color='blue', alpha=0.6)
ax1.set_title('Scatter plot 1')
ax1.set_xlabel('X axis 1')
ax1.set_ylabel('Y axis 1')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.grid(True)

ax2.scatter(x2, y2, color='red', alpha=0.6)
ax2.set_title('Scatter plot 2')
ax2.set_xlabel('X axis 2')
ax2.set_ylabel('Y axis 2')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.grid(True)

plt.tight_layout()
plt.show()