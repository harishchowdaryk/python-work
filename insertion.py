class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new= Node(data)
        last = self.head
        new.next = None

        if self.head is None:
            self.head = new
            return

        while last.next:
            last = last.next

        last.next = new

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

