# Kod testowy umieszczający elementy na stosie i usuwający elementy ze stosu.

from Stack import *

oStack = Stack()
oStack.push(5)
oStack.push(12)
oStack.push('Dowolne dane')
oStack.push('Inne dowolne dane')
oStack.push(True)
oStack.show()

while True:
    print()
    item = oStack.pop()
    print('Następna wartość na stosie to:', item)
    if oStack.getSize() == 0:
        break
    oStack.show()

print('Stos jest pusty.')
