import time

def dividing(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Don\'t divide by zero")

dividing_outcome = dividing(1, 0)
print("The outcome is", dividing_outcome)

asterisks = "**********"
spacebars = " "

for i in range(1, 6):
    print(spacebars * i, asterisks)
    time.sleep(0.5)


for i in range(5, 0, -1):
    print(spacebars * i, asterisks)
    time.sleep(0.5)