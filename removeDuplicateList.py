#method1
# convert the list into set and convert again into list
myList = [1,2,2,4,4,5,5,5,7]
removeDuplicates = set(myList)
print(list(removeDuplicates))

#method2
myDict = list(dict.fromkeys(myList))
print("using dict: ",myDict)

#method3 using list comprehension
seen = set()
myNewList = [x for x in myList if not (x in seen or seen.add(x))]
print("using list comprehension: ",myNewList)

#method4 using for
def remove_duplicates(myList):
    unique_list = []
    for item in myList:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

result = remove_duplicates(myList)
print("using for: ",result)  # Output: [1, 2, 3, 4, 5]
