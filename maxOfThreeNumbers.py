a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
class MaxNum:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def findMaxOfThree(self):
        if self.a >= self.b and self.a >= self.c:
            largest = self.a
        elif self.b >= self.a and self.b >= self.c:
            largest = self.b
        else:
            largest = self.c
        return largest

obj = MaxNum(a, b, c)
number = obj.findMaxOfThree()
print("The max of three numbers: ", number)
