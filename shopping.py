items = []

def create():
    e = input("what would u like to add?")
    items.append(e)
    print("conrgats u just added " + e)

def delete():
    f = input("what do u want to delete?")
    if f in items:
        items.remove(f)
        print("congrats u just deleted " + f)
    else:
        print("item not found")



while True:
    print("Main menu:")
    print("C: Create a new item")
    print("R: Read (Display) your shopping cart")
    print("D: Delete an item")
    print("E: Exit the program")
    choice = input("What would you like to do?: ")

    if choice.lower() == "c":
        create()

    elif choice.lower() == "r":
        if len(items) > 0:
            print(items)
        else:
            print("invalid, add some things first")

    elif choice.lower() == "d":
        delete()

    elif choice.lower() == "e":
        print("exiting....")
        break

    else:
        print("invalid input")


