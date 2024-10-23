a = int(input("Enter a number: "))
class Number:
    def __init__(self, a):
        self.a = a
    def checkPositiveOrNegative(self):
        if self.a > 0:
            print("The number is positive")
        elif self.a < 0:
            print("The number is negative")
        elif self.a == 0:
            print("The number is zero")
obj = Number(a)
obj.checkPositiveOrNegative()