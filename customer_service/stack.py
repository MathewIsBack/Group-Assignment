class Stack:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def is_empty(self):
        # check if the stack is empty
        return len(self.items) == 0

    def remove_item(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def top_item(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    

# Testing 

# stack = Stack()

# stack.add_item(3)
# stack.add_item(7)
# stack.add_item(23)

# print("Stack size:", stack.size())

# print("Top Item:", stack.top_item())

# removed = stack.remove_item()
# print("Removed item:", removed)

# # Check its empty
# print("Is stack empty?", stack.is_empty())

# # Final state of stack
# print("Current stack:", stack.items)



        