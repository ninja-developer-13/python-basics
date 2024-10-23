a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sumOfNumbers(self):
        sumOf = self.a +self.b
        print("Sum of two numbers: ", sumOf)
obj = Numbers(a,b)
obj.sumOfNumbers()