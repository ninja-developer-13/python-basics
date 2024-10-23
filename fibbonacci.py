def fibonacci(n):
    a, b = 0, 1  # Starting values
    for i in range(n):
        print(a, end=' ')  # Print the current number
        a, b = b, a + b  # Update to the next two Fibonacci numbers

# Input from the user
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci(num_terms)