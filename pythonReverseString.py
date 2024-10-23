a = str(input("Enter a string: "))
class StringReverse:
    def __init__(self, string):
        self.string = string
    def reverse(self):
        #return self.string[::-1]
        reversed_s = ""
        stringLength = len(self.string)
        for i in range(stringLength - 1, -1, -1):
            reversed_s += self.string[i]
        return reversed_s


obj = StringReverse(a)
print("The reversed String: ",obj.reverse())
