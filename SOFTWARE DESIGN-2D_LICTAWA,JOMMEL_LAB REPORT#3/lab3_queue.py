queue = []
def enqueue():
    ele = input("\nEnter element: ")
    queue.append(ele)

def dequeue():
    if not queue:
        print("\nQueue is empty!")
    else:
        ex = queue.pop(0)
        print("\nRemoved Element: ",ex)

def display():
    print("Queue: ",queue)

while True:
    print("\nWhat do you want to do?\n")
    print("1. Add an element\n2. Delete an element\n3. Quit program\n")
    opr = int(input("Operation: "))
    if opr==1:
        enqueue()
        display()
    elif opr==2:
        dequeue()
        display()
    elif opr==3:
        break
    else:
        print("\nInvalid operation")