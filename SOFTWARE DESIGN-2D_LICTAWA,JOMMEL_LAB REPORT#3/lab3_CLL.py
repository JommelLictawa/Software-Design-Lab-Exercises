class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def ad(self, data):
        new = Node(data)
        if self.head.data is None:
            self.head = new
            self.tail = new
            new.next = self.head

        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head

    def trav(self):
        n = self.head
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            print("Nodes of the Circular Linked List: ")
            print(n.data)
            while(n.next != self.head):
                n = n.next
                print(n.data)
                
CLL = CircularLinkedList()
CLL.ad(10)
CLL.ad(13)
CLL.ad(4)
CLL.ad(87)
CLL.trav()