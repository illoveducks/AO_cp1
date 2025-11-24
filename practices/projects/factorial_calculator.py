# AO 1st Factorial calculator

# display choose a number that is not a negative or decimal

# choice is a insert of a number
# for in choices
# if choice is not a number that is a whole
# Display ( not viable )
# else:
# for in rnage (num, choice):
    # Multiply * choice
    # c= display original number and i 
    # return c

    # while true
    # function on numbers() uh... what?


num = 1


print("pick a number that is not a negative or decimal ")

while True:
    try:
        choice = int(input("type a number \n "))
 # This is something I added, this checks something just to make sure that if it's a calue error that it goes back up

    except ValueError:
        print("please type a whole number.")
        continue


        

    if choice < 0:
        print("no negatives ")
        continue

    elif choice == choice and choice > 1:
        
        for i in range(1, choice + 1):
            num = num * i
        print("original choice:", choice, "factorial: ", num)
    break
        
                                              



                                                # there's a logic error, the code runs well, but it doesn't break
                                                  # The