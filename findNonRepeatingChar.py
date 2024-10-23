class Solution:
    def __init__(self, myString):
        self.myString = myString

    def extractString(self):
        for char in self.myString:
            if self.myString.count(char) == 1:
                return char
        return None  # Return None if no non-repeating character is found

# Get user input
a = input("Enter the string: ")
obj = Solution(a)
print(obj.extractString())
