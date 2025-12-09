"""
Stack Implementation using a List in Python
This program demonstrates a basic Stack data structure with push, pop, and display operations.
"""

class Stack:
    """
    A simple Stack class implementation using Python list.
    Stack follows LIFO (Last In First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, element):
        """
        Push an element onto the stack.
        
        Args:
            element: The value to be added to the stack
        """
        self.items.append(element)
        print(f"Pushed {element} onto the stack")
    
    def pop(self):
        """
        Pop an element from the stack.
        
        Returns:
            The popped element, or None if stack is empty
        """
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        
        element = self.items.pop()
        print(f"Popped {element} from the stack")
        return element
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise
        """
        return len(self.items) == 0
    
    def display(self):
        """Display all elements in the stack from top to bottom."""
        if self.is_empty():
            print("Stack is empty!")
            return
        
        print("Stack contents (top to bottom):")
        for i in range(len(self.items) - 1, -1, -1):
            print(f"  {self.items[i]}")
        print(f"Total elements: {len(self.items)}")
    
    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)


# Main program demonstrating stack operations
if __name__ == "__main__":
    print("=" * 50)
    print("STACK IMPLEMENTATION USING PYTHON LIST")
    print("=" * 50)
    
    # Create a new stack
    stack = Stack()
    
    # Operation 1: Push 5 elements
    print("\n--- PUSHING 5 ELEMENTS ---")
    elements_to_push = [10, 20, 30, 40, 50]
    
    for element in elements_to_push:
        stack.push(element)
    
    print(f"\nStack size after pushing: {stack.size()}")
    
    # Display stack after pushing
    print("\n--- STACK AFTER PUSHING ---")
    stack.display()
    
    # Operation 2: Pop 2 elements
    print("\n--- POPPING 2 ELEMENTS ---")
    stack.pop()
    stack.pop()
    
    print(f"\nStack size after popping: {stack.size()}")
    
    # Operation 3: Display remaining stack
    print("\n--- REMAINING STACK AFTER POPPING ---")
    stack.display()
    
    print("\n" + "=" * 50)
    print("OPERATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 50)
