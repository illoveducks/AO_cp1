# AO 1st Order Up!


main_order = []
side_order = [

]

drink = []


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
"water": 0,
" orange juice": 0.75,
" Dr.pepper": 1,
"Coke": 1, 
}

size = {
"small": 0.75,
"medium/normal": 1.25,
"large": 1.75,

}









while True:

    print(main)

    main_order = input("what would like your main course to be? 1-3 \n ")

    if main_order == "1":
        main_order = (main["burger1"])
        break
    if main_order == "2":
        main_order = (main["chicken alfredo2"])
        break
    if main_order == "3":
        main_order = (main["chicken sandwich3"])
        break
    elif main_order != "1" and main_order != "2" and main_order != "3":
        print("invalid order")
        

while True:

    print(side_dishes)


    first_side = input("what would you like your side dish to be? type 1-5 \n ")

    if first_side == "1":
        first_side = (side_dishes["bacon1"])
        break
    if first_side == "2":
        first_side = (side_dishes["chicken nuggets2 "])
        break
    if first_side == "3":
        first_side = (side_dishes["curly fries3"])
        break
    if first_side == "4":
        first_side = (side_dishes["fries4"])
        break
    if first_side == "5":
        first_side = (side_dishes["salad5"])
        break
    
while True:

            print(side_dishes)
            
            second_side = input("what would you like your second side dish to be? type 1-5 \n ")

            if second_side == "1":
              second_side = (side_dishes["bacon1"])
              break
            if second_side == "2":
                  second_side = (side_dishes["chicken nuggets2 "])
                  break
            if second_side == "3":
                second_side = (side_dishes["curly fries3"])
                break
            if second_side == "4":
                second_side = (side_dishes["fries4"])
                break
            if second_side == "5":
                second_side = (side_dishes["salad5"])
                break











cost = main_order + first_side + second_side 

print(cost)













    








