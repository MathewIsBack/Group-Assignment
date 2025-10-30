from stack import Stack
from queue import Queue
from linked_list import SinglyLinkedList
from customer import Customer

def main():
    # manage customers with queue like in real life
    customer_queue = Queue()

    # create some customers
    c1 = Customer("Evan", 101)
    c2 = Customer("Precious", 102)
    c3 = Customer("Charlie", 103)
    c4 = Customer("John", 104)

    # add customers to queue
    customer_queue.enqueue(c1)
    customer_queue.enqueue(c2)
    customer_queue.enqueue(c3)
    customer_queue.enqueue(c4)

    print("Customer Queue:")
    while not customer_queue.is_empty():
        customer = customer_queue.dequeue()
        print("Serving:", customer)


    print("\n---------------------------\n")

    # ----------------------------
    # Stack Example: Completing Tasks
    # ----------------------------
    task_stack = Stack()
    task_stack.add_item("Task 1: Process forms")
    task_stack.add_item("Task 2: Approve requests")
    task_stack.add_item("Task 3: Send emails")

    print("Task Stack (LIFO):")
    while not task_stack.is_empty():
        task = task_stack.remove_item()
        print("Completing:", task)

    print("\n---------------------------\n")

    # ----------------------------
    # Linked List Example
    # ----------------------------
    ll = SinglyLinkedList()
    ll.append(c1)
    ll.append(c2)
    ll.append(c3)
    ll.append(c4)

    print("Linked List Nodes:")
    print(ll.display())


if __name__ == "__main__":
    main()