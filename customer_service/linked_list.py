class Node:

    def __init__(self, data):
        self.data = data  # Value stored in the node
        self.next = None  # pointer to the next node

class SinglyLinkedList:

    def __init__(self):
        self.head = None  # The first node in the list (default: None)

    def append(self, data):
        # add a new node to the end of the list
        new_node = Node(data)

        if not self.head:
            self.head  = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, value):

        current = self.head

        while current:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def delete(self, value):
        current = self.head

        if not current:
            return False
        
        if current.data == value:
            self.head = current.next
            return True
        
        previous = None
        while current:
            if current.data == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False
    
    def display(self):

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else 'Empty list'
    

# linked_list = SinglyLinkedList()

# # Add some elements
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)
# linked_list.append(40)

# print("Linked List:", linked_list.display())

# found = linked_list.find(20)
# print("Found node:", found.data if found else "Not found")

# # Delete a node
# deleted = linked_list.delete(30)
# print("Deleted 30:", deleted)
# print("Updated List:", linked_list.display())

        


