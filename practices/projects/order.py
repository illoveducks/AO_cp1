# AO 1st Order Up!


main_order = []
side_order = [

]

drink = []


main = {
"burger": 3.25,
"chicken alfredo": 5.00,
"chicken sandwich": 2.75,


}


side_dishes = {
"fries": 2.50,
"curly fries": 2.75,
"chicken nuggets ": 2.80,
"bacon": 1.00,
"salad": 

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





"1" == main["burger"]
"2" == main["chicken alfredo"]
"3" == main["chicken sandwich"]

main_order = input("please type a number 1-3 as your main course, P.S sorry for this restaruant fast food place not having that many things to order :( )")





while True:
    if main_order == "1":
        main_order = (main["burger"])
        break
    if main_order == "2":
        main_order = (main["chicken alfredo"])
        break
    if main_order == "3":
        main_order = (main["chicken sandwich"])
        break
    elif main_order != "1" and main_order != "2" and main_order != "3":
        print("invalid order")
        





cost = main_order + first_side + second_side + drink

print(cost)













    








