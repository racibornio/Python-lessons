class Testy():
    def __init__(self, parA, parB):
        print("Init called.")
        self.parA = parA
        self.parB = parB
        pass


    def meth_1(self):
        print(f'Arg. a: {self.parA}, arg. b: {self.parB}')


obj1 = Testy(15, 800)
obj1.meth_1()

var1 = False
print(var1)
var1 = not var1
print(var1)
var1 = not var1
print(var1)
var1 = not var1
print(var1)