a = int(input("Enter a number: "))
class CheckPol:
    def __init__(self,a):
        self.a = a
    def checkPolNumber(self):
        temp = self.a
        reverse = 0
        while temp > 0:
            remainder = temp % 10
            #to extract last digit
            reverse = (reverse*10) + remainder
            temp //= 10
        return reverse
obj = CheckPol(a)
reverseNum = obj.checkPolNumber()
if a == reverseNum:
    print("The given number is Polindrome")
else:
    print("The given number is not Polindrome")