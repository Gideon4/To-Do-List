import sys

d = {}
numoitems = 0

def menu():
    choice = ""
    print("Where would you like to go")
    print("a: Add an item.")
    print("d: Delete an item.")
    print("q: Quit.")
    choice = input()
    if choice == "a":
        add()
    elif choice == "d":
        delete()
    elif choice == "q":
        sys.exit
    else:
        print("That's not an option, silly!")
        menu()

def showlist():
    print(d)

def add():
    global numoitems
    newitem = []
    print("What event would you like to add?")
    newitem.append(input())
    print("When is it due?")
    newitem.append(input())
    d[numoitems] = newitem
    numoitems += 1
    showlist()
    menu()

def delete():
    showlist()
    print("What would you like to delete?")
    delitem = input()
    if delitem in d:
        del d[int(delitem)]
    else:
        print("That's not an item silly!")
    menu()

menu()
