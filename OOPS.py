# Classes are user defined blueprint or prototype # like sum, mul, sub, div operations in a calc
# will have methods, class vars, instance vars, constructor etc.

class Calculator:

    num = 100
    x = 0
    y = 0

   # def __init__(self):
   #     print('Default Constructor Method Executed Automatically when object is created')

    def __init__(self, a, b):
        print('Default Constructor Method with a & b Executed Automatically when object is created')
        self.x = a
        self.y = b

    def printdata(self):
        print("print data () executed")

    def adddata(self):
        print(self.x + self.y)

    def subdata(self):
        print(self.x - self.y)

    def summing(self):
        print(self.x + self.y + Calculator.num)

    def subing(self):
        print(self.x - self.y + self.num)

calc = Calculator(4, 6) #syntax to create objects in python
calc.printdata()
print(calc.num)
calc.adddata()
calc.summing()

calc1 = Calculator(16, 4)
calc1.printdata()
print(calc1.num)
calc1.subdata()
calc1.subing()
