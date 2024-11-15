def main ():
    shopping_cart = []
    while True:
        option = int(input("1)Add item to shopping_cart\n2)See shopping cart list\n3)Remove item from shopping cart (according to index)\n4)Edit item in shopping cart list (according to index)\n5)Remove all items from the shopping cart\n6)Exit\n"))
        if 1 <= option and option <= 6:
            if option == 1:
                add_item(shopping_cart)
            if option == 2:
                see_cart(shopping_cart)
            if option == 3:
                remove_item(shopping_cart)
            if option == 4:
                edit(shopping_cart)
            if option == 5:
                clear(shopping_cart)
            if option == 6:
                print(shopping_cart)
                break
        else:
            print("Error: Not an option")

def add_item(cart: list):
    item = input("Insert an item to add to the end of the shopping cart: ")
    cart.append(item)
def see_cart(cart: list):
    print(cart)
def remove_item(cart: list):
    print(cart)
    while True:
        try:
            index = int(input("Insert an index to remove an item from the shopping cart: "))
            try:
                cart.pop(index)
                break
            except IndexError:
                print("Index is outside of range")
        except ValueError:
            print("Not an integer index")
    
def edit(cart: list):
    print(cart)
    while True:
        try:
            index = int(input("Insert an index to edit an item from the shopping cart: "))
            break
        except ValueError:
            print("Not an integer index")
    cart.pop(index)
    item = input("Insert the replacement value: ")
    cart.insert(index, item)
def clear(cart: list):
    cart.clear()

main()