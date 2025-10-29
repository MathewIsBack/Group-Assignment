class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        return None
    
    def first_item(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
# queue = Queue()

# queue.enqueue(3)
# queue.enqueue(7)
# queue.enqueue(23)

# print("Queue size:", queue.size())

# print("First item:", queue.first_item())

# # removed = queue.dequeue()
# # print("Removed item:", removed)

# # Check its empty
# print("Is queue empty?", queue.is_empty())

# # Final state of stack
# print("Current queue:", queue.items)

