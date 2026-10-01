import matplotlib.pyplot as plt
from faker import Faker
import random
import pandas as pd
import numpy as np

fake = Faker()

# line charts - values only
plt.plot([0, 1, 2, 3, 4, 5, 2, 4, 6, 8, 10]) # these are values on Y axis, while list positions are arguments on X axis
plt.xlabel('Arguments')
plt.ylabel('Numbers')
plt.show()

# line charts - arguments and values
plt.plot([1, 2, 3, 4, 5, 6], [1.33, 2.66, 3.99, 5.32, 6.65, 7.99]) # first list - arguments on X axis, second list - values on Y axis
plt.xlabel('Arguments')
plt.ylabel('Numbers')
plt.show()

# dot charts - arguments and values + define color and shape
plt.plot([1, 2, 3, 4, 5, 6], [1.33, 2.66, 3.99, 5.32, 6.65, 7.99], 'ro') # 'r - red, o - ovals'
plt.xlabel('Arguments')
plt.ylabel('Numbers')
plt.show()

# dot charts - arguments and values + define color and shape
plt.plot([1, 2, 3, 4, 5, 6], [1.33, 2.66, 3.99, 5.32, 6.65, 7.99], 'bs') # 'b - blue, s - squares'
plt.xlabel('Arguments')
plt.ylabel('Numbers')
plt.show()

# dot charts - arguments and values + limit the range
plt.plot([1, 2, 3, 4, 5, 6], [1.33, 2.66, 3.99, 5.32, 6.65, 7.99], 'bs') # 'b - blue, s - squares'
plt.xlabel('Arguments')
plt.ylabel('Numbers')
plt.axis((1, 6, 1, 8)) # tuple defining X values range and Y values range
plt.show()


# two lines from to lists counted from the loop
l1, l2 = [], []
for i in range (0, 5):
    x = i * 1.3
    l1.append(x)
    l2.append(x * 1.9)

# a few charts on one plot -> three separate flows
# plt.plot(x, y, format)
plt.plot(l1, l1, 'r-', l1, l2, 'go', l2, l2, 'b^')
plt.show()


# scatter plot
x, y = 1, 11
# plt.scatter(x, y, s=..., c=..., data=...)
plt.scatter(x, y)
plt.show()


x = [1, 2, 3, 4, 5, 6, 7]
y = [20, 19, 24, 26, 25, 22, 28]
z = [100, 90, 95, 120, 110, 105, 125]
plt.scatter(x, y, c=z, cmap='viridis')
plt.colorbar(label='Intensity')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Temperature in time')
plt.show()


age = [1, 2, 3, 4, 5, 6, 7]
weight_girls = [9.5, 11.5, 13.5, 15.5, 17.0, 19.0, 21.0]
weight_boys = [10.0, 12.0, 14.0, 16.5, 18.5, 21.0, 23.0]
n_girls = [30, 11, 18, 4, 38, 45, 70]
n_boys  = [32, 30, 34, 42, 39, 47, 52]
scale = 5
plt.scatter(age, weight_girls, color='deeppink', s=[n*scale for n in n_girls], label='Girls', alpha=0.6)
plt.scatter(age, weight_boys,  color='dodgerblue', s=[n*scale for n in n_boys], label='Boys', alpha=0.6)
plt.xlabel('Age (years)')
plt.ylabel('Weight (kg)')
plt.title('Average kids weight in age')
plt.legend()
plt.grid(True)
plt.show()


fig, axs = plt.subplots(2)
axs[0].plot([1, 8, 5, 2])
axs[1].plot([4, 11, 12, 9])
plt.show()


labels = ['A', 'B', 'C', 'D']
values = [8, 5, 12, 30]
plt.bar(labels, values)
plt.show()