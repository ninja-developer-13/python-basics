class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushing 10, 20, 30:", stack)
    print("Top item:", stack.peek())

    popped_item = stack.pop()
    print("Popped item:", popped_item)
    print("Stack after popping:", stack)
    print("Is the stack empty?", stack.is_empty())
    print("Current stack size:", stack.size())
