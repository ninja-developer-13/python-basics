a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
class MinNum:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def findMinOfThree(self):
        if self.a <= self.b and self.a <= self.c:
            smallest = self.a
        elif self.b <= self.a and self.b <= self.c:
            smallest = self.b
        else:
            smallest = self.c
        return smallest

obj = MinNum(a, b, c)
number = obj.findMinOfThree()
print("The min of three numbers: ", number)
