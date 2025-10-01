# AO class Shopping List Manager

shop_list = []

while True:
    print("to add things 1, to remove 2, to show the list 3, to leave 4")
    action = input("please type a number 1-4:\n")
   
   
    if action == "1":
        item = input("Add item:\n")
        shop_list.append(item)
        print(f"{item} added.")
    elif action == "2":
        item = input(" remove item:\n")
        if item in shop_list:
            shop_list.remove(item)
            print(f"{item} removed.")
        else:
            print("this item is not on your list.")
    elif action == "3":
        print(shop_list)
        
    elif action == "4":
        print("goodbye!")
        break