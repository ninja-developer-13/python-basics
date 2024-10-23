class Solution:
    def __init__(self, myString):
        self.myString = myString
    def reverseString(self):
        reverse = ''
        for i in self.myString:
            reverse =  i + reverse
        return reverse
a = str(input("Enter the string: "))
obj = Solution(a)
print(obj.reverseString())
if a == obj.reverseString():
    print("String is palindrome")
else:
    print("String is not palindrome")