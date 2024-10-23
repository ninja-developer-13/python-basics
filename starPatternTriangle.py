#Write a program to print the following pattern.
# *
# * *
# * * *
# * * * *
# * * * * *
def starPatternTriangle(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end=" ")
        print("\r")
n = int(input("Enter the sequence: "))
starPatternTriangle(n)


