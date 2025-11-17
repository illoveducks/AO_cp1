# AO 1st Order Up!


# dictionaries a lot of them

main = {
"burger1": 3.25,
"chicken alfredo2": 5.00,
"chicken sandwich3": 2.75,


}


side_dishes = {
"fries4": 2.50,
"curly fries3": 2.75,
"chicken nuggets2 ": 2.80,
"bacon1": 1.00,
"salad5": 1.50

}


drinks = {
"water1": 0.0,
" orange juice2": 0.75,
" Dr.pepper3": 1,
"Coke4": 1, 
}

size = {
"small1": 0.75,
"medium/normal2": 1.25,
"large3": 1.75,

}


# every while statement breaks after the customers order is valid





# a loop just in case a user decides to be stupid
while True:
#shows main courses
    print(main)
# asks user what he or she wants for their main course
    main_order = input("the number beside them is the price, what would like your main course to be? tipe 1-3 \n ")
# depending what number sets the value as that
    if main_order == "1":
        main_order = (main["burger1"])
        break
    if main_order == "2":
        main_order = (main["chicken alfredo2"])
        break
    if main_order == "3":
        main_order = (main["chicken sandwich3"])
        break
    # stupid proof
    elif main_order != "1" and main_order != "2" and main_order != "3":
        print("invalid order")
        
# a loop just in case
while True:

    print(side_dishes)
    # show side dishes
    # ask user what he wants
    first_side = input("the number beside them is the price, what would you like your side dish to be? type 1-5 \n ")

    # sets the value depending on what the user adds
    if first_side == "1":
        first_side = (side_dishes["bacon1"])
        print("bacon added")
        break
    if first_side == "2":
        first_side = (side_dishes["chicken nuggets2 "])
        print("chicken nuggets added")
        break
    if first_side == "3":
        first_side = (side_dishes["curly fries3"])
        print("curly fries added")
        break
    if first_side == "4":
        first_side = (side_dishes["fries4"])
        print("fries added to order")
        break
    if first_side == "5":
        first_side = (side_dishes["salad5"])
        print(" salad added to order")
        break
    # stupid proof
    elif first_side != "1" or first_side != "2" or  first_side != "3" or first_side != "4" or first_side != "5": 
        print("invalid order") 
# a loop just in case
while True:
            # show side dishes
            print(side_dishes)
            # ask user what he wants
            second_side = input("what would you like your second side dish to be? type 1-5 \n ")

            # what happens depending on what number the user does, the order on the side dish
            if second_side == "1":
              second_side = (side_dishes["bacon1"])
              print("added bacon")
              break
            if second_side == "2":
                  second_side = (side_dishes["chicken nuggets2 "])
                  print("chicken nuggets added to order")
                  break
            elif second_side == "3":
                second_side = (side_dishes["curly fries3"])
                print("curly fires added to order")
                break
            elif second_side == "4":
                second_side = (side_dishes["fries4"])
                print("fries added to order")
                break
            elif second_side == "5":
                second_side = (side_dishes["salad5"])
                print("salad added to order")
                break
            # stupid proof
            elif  second_side != "1" or second_side != "2" or  second_side != "3" or second_side != "4" or second_side != "5": 
             print("invalid order") 


# a loop just in case
while True:
# shows drinks
    print(drinks)
    # asks what you want
    drink_choice = input("please pick a drink type 1-4 \n ")
# sets value depending on what drink they want
    if drink_choice == "1":
        drink_choice = (drinks["water1"])
        break
    elif drink_choice == "2":
            drink_choice = (drinks[" orange juice2"])  
            break  
    elif drink_choice == "3":
        drink_choice = (drinks[" Dr.pepper3"])
        break
    elif drink_choice == "4":
        drink_choice = (drinks["Coke4"])
        break
    # stupid proof
    elif  drink_choice != "1" or drink_choice != "2" or  drink_choice != "3" or drink_choice != "4":
            print("invalid order") 
# another loop just in case
while True:
    print(size) # shows sizes
    # asks what size you want
    size_choice = input("what size drink do you want type 1-3 \n")

# sets value
    if size_choice == "1":
         size_choice = (size["small1"])
         print("small drink added")
         break # break on all the statements so it doesn't keep going
    if size_choice == "2":
         size_choice = (size["medium/normal2"])
         print(" medium drink added ")
         break
    if size_choice == "3":
         size_choice = (size["large3"])   
         print(" large drink added ") 
         break
    # stupid proof
    elif size_choice != "1" or size_choice != "2" or size_choice != "3":
         print("invalid order")


# calculates order
cost = main_order + first_side + second_side + drink_choice + size_choice

# calculates tax
tax = cost * .1

# final price after combine the two
final_price = cost + tax

# tells person how much the tax is.
print("sales tax is 10% ")

# shows order
print( "main order:",main_order,
        "side:", first_side,
      "side:",  second_side,
      "drink:", drink_choice,
      "size:", size_choice,
      "this costs", final_price,
      "thank you for ordering at this place.")



















    








