stack = []
def push():
    ele = input("\nEnter element: ")
    stack.append(ele)

def pop():
    if not stack:
        print("\nStack is empty!")
    else:
        ex = stack.pop()
        print("\nRemoved Element: ",ex)
        
def display():
    print("Stack: ",stack)

while True:
    print("\nWhat do you want to do?\n")
    print("1. Add an element\n2. Delete an element\n3. Quit program\n")
    opr = int(input("Operation: "))
    if opr==1:
        push()
        display()
    elif opr==2:
        pop()
        display()
    elif opr==3:
        break
    else:
        print("\nInvalid operation")