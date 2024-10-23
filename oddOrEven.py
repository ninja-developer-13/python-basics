a = int(input("Enter the number: "))
class Number:
    def __init__(self, a):
        self.a = a
    def checkOddorEven(self):
        if self.a % 2 == 0:
            print("The given number is an even number.")
        else:
            print("The given number is an odd number.")


obj = Number(a)
obj.checkOddorEven()
