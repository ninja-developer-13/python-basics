import itertools
class Solution:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def mergeTwoSortedLists(self):
        # Convert input strings to sorted lists of characters
        l1 = sorted(self.str1)
        l2 = sorted(self.str2)
        # Use itertools.chain to merge the two lists
        l3 = itertools.chain(l1, l2)
        return list(l3)
str1 = str(input("Enter first string: "))
str2 = str(input("Enter second string: "))
obj = Solution(str1, str2)
print(obj.mergeTwoSortedLists())