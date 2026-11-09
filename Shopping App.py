import os
items = {}

def create():
    print("")
    print("Add a new item")
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: $"))
    items[item_name] = item_price
    print(item_name, "has been added!")
    print("")
    input("Press enter to continue...")
    os.system("cls")
    save()

def read():
    print("")
    print("Read items")
    if len(items) == 0:
        print("No item yet.")
    else:
        for item in items:
            print(item, f"${items[item]}")
    print("")
    input("Press enter to continue...")
    os.system("cls")

def delete():
    print("")
    print("Delete an item")
    if len(items) == 0:
        print("No item yet.")
    else:
        item_name = input("Enter the item to remove: ")
        if item_name in items:
            del items[item_name]
            print(item_name, "has been removed!")
        else:
            print(item_name, "is not found!")
    print("")
    input("Press enter to continue...")
    os.system("cls")
    save()

def save():
    file = open("items.txt", "w")
    for i in items:
        written = f"{i}${items[i]}"
        file.write(written + "\n")

def load():
    try:
        file = open("items.txt", "r")
        content = file.read()
        pulled_items = content.split()
        for i in pulled_items:
            data = i.split("$")
            name = data[0]
            price = data[1]
            items[name] = float(price)
    except:
        print("No previous saves!")

load()
while True:
    print("")
    print("Main menu:")
    print("C: Create a new item")
    print("R: Read (Display) your shopping cart")
    print("D: Delete an item")
    print("E: Exit the program")
    choice = input("What would you like to do?: ")

    os.system("cls") # clean the terminal

    if choice.lower() == "c":
        create()

    elif choice.lower() == "r":
        read()

    elif choice.lower() == "d":
        delete()

    elif choice.lower() == "e":
        print("Exiting program...")
        break

    else:
        print("Invalid input!")
    