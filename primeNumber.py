"""
A prime number is a number that can only be divided by
itself and 1 without remainders.
"""
from operator import truediv

a = int(input("Enter a number: "))
class CheckPrime:
    def __init__(self, a):
        self.a = a

    def checkIfPrime(self):
        flag = False
        if self.a > 1:
            for i in range(2,self.a):
                if self.a %i == 0:
                    return False
            return True

obj = CheckPrime(a)
if obj.checkIfPrime():
    print("The given number is prime")
else:
    print("The given number is not a prime")