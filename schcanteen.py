import os, pickle
stalls = {}

class Stall:

    def __init__(self, name, ):
        self.name = name
        self.product = {}
        self.stocks = {}

    def show_products(self):
        if len(self.product) > 0:
            for p in self.product:
                print(self.product[p].name, f"${self.product[p].price}")
                print("Ingredients:", self.product[p].ingredients)
        else:
            print("no products yet")

    def show_stocks(self):
        if len(self.stocks) > 0:
            count = 0
            for s in self.stocks:
                count += 1
                print(f"{count}.", s, ":", self.stocks[s])
        else:
            print("no stock yet")

    def infos(self):
        if len(self.product) > 0:
            count = 0
            print("with the current stocks...")
            for p in self.product:
                count += 1
                amount = 0

                p_ing = self.product[p].ingredients
                req_ing = []
                producable = False
                p_can = 0

                for i in p_ing:
    
                    if i in self.stocks:
                        if p_ing[i] <= self.stocks[i]:
                            p_can += 1

                    if len(p_ing) == p_can:
                        producable = True
            

                    if producable:
                        for i in p_ing:
                            req_ing.append(self.stocks[i]/p_ing[i])
                        amount = min(req_ing)
                
            
                print(f"{count}.", "You can make", amount, p + "(S)")

class Product:

    def __init__(self, name):
        self.name = name
        self.price = 0
        self.ingredients = {}



def load():
    global stalls
    with open("data.pkl", "rb") as file:
            stalls = pickle.load(file)
            print("pickle data loaded")
        


def save():
    with open("data.pkl", "wb") as file:
        pickle.dump(stalls, file)
        print("pickle data saved")



while True:

    print("")
    print("SC Inventory system Main Menu")
    print("1: Create a new stall")
    print("2 Create a new product   ")
    print("3 Create/ Add stock for stall")
    print("4: Read (Display) stalls/details")
    print("5: Exit the program")
    choice = input("What would you like to do?: ")

    os.system("cls") 
    load()

    if choice == "1":
        print("create a new stall!")
        name = input("enter the name of the new stall: ")
        new_stall = Stall(name)
        stalls[name] = new_stall
        print(name, "has been added to the database!")
        save()

    elif choice == "2":
        if len(stalls) == 0:
            print("no stalls added yet")
        else:
            stall_name = input("enter the stall name: ")
            if stall_name in stalls:
                product_name = input("enter the name of the product to add: ")
                product_price = float(input("enter the product price: $ "))
                new_product = Product(product_name)
                new_product.price = product_price
                req_ingredients = int(input("how many ingredients to make this dish? "))
                for i in range(req_ingredients):
                    print(" ")
                    i_name = input("enter in the name of the ingredient: ")
                    i_count = float(input("enter ingredient quantity: "))
                    new_product.ingredients[i_name] = i_count
                stalls[stall_name].product[product_name] = new_product
                print(product_name, "has been added to stall", stall_name)
                save()
            else:
                print("stall name not found")

    elif choice == "3":
        if len(stalls) == 0:
            print("no stalls added")
        else:
            stall_name = input("enter the stall name: ")
            if stall_name in stalls:
                print(" ")
                Stall.show_stocks(stalls[stall_name])
                print("if stock exists, itll update the value")
                stock_name = input("enter the stock name: ")
                stock_quantity = float(input("enter the quantity: "))
                stalls[stall_name].stocks[stock_name] = stock_quantity
                print("stock has been added to the stall", stall_name)
                save()
            else:
                print("that stall isnt found")

    
    
    
    
    
    elif choice == "4":
        if len(stalls) == 0:
            print("no stalls added!")
        else:
            for stall in stalls:
                print(" ")
                print(stall)
                Stall.show_products(stalls[stall])
                Stall.infos(stalls[stall])


    elif choice == "5":
        print("exiting...")
        save()
        break