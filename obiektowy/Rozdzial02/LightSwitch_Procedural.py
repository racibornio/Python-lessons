# Wyłącznik światła utworzony w podejściu proceduralnym.

def turnOn():
    global switchIsOn
    # Włączenie światła.
    switchIsOn = True

def turnOff():
    global switchIsOn
    # Wyłączenie światła.
    switchIsOn = False

# Kod główny.
switchIsOn = False     # Globalna zmienna boolowska.

# Kod testowy.
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
