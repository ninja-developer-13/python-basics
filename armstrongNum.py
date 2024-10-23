a = int(input("Enter a number: "))
class ArmstrongNum:
    def __init__(self, a):
        self.a = a
    def isArmstrong(self):
        sum = 0
        temp = self.a
        while temp > 0:
            digit = temp % 10
            sum += digit ** len(str(self.a))
            temp //= 10
        return sum
obj = ArmstrongNum(a)
armstrong = obj.isArmstrong()
if a == armstrong:
    print(a, "is armstrong")
else:
    print(a, "is not armstrong")
