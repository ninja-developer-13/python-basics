a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
class MaxNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def findMaxNumber(self):
        if self.a <= self.b:
            print(self.a, "is smaller number")
        else:
            print(self.b, "is smaller number")
obj = MaxNum(a, b)
number = obj.findMaxNumber()

