class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
       self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def ad(self, data): #add node
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def rem(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            print("Linked List is empty after deleting the node.")

        else:
            self.head = self.head.next
            self.head.prev = None

    def trav(self): #traversing forward
        if self.head is None:
            print("Linked List is empty")
            
        else:
            print("Nodes of the Doubly Linked List: ")
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next    


DLL = DoublyLinkedList()
DLL.ad(0)
DLL.ad(20)
DLL.ad(115)
DLL.ad(90)
DLL.rem()
DLL.rem()
DLL.trav()