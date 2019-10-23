import sys

l = []

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
    for i in range(len(l)):
        print(str(i+1)+": "+l[i][0]+(" "*(30-len(l[i][0])))+" Due: "+l[i][1])

def add():
    newitem = []
    print("What event would you like to add?")
    newitem.append(input())
    print("When is it due?")
    newitem.append(input())
    l.append(newitem)
    showlist()
    save()
    menu()

def delete():
    showlist()
    print("What would you like to delete?")
    delitem = int(input())-1
    if delitem <= len(l):
        l.pop(delitem)
        save()
    else:
        print("That's not an item silly!")
    menu()

def save():
    try:
        global l
        file = open("thelist.txt","w")
        text = ""
        for item in l:
            text = text + ", ".join(item) + ";"
        file.write(text)
        file.close()
    except:
        print("Didn't work.")

def load():
    global l
    try:
        file = open("thelist.txt","r")
        mytext = file.read()
        file.close()
        flist = mytext.split(";")
        flist.pop()
        for item in flist:
            l.append(item.split(","))
        print(l)
    except:
        print("Didn't work")
    
load()   
menu()
