# AO 1st Flexible calculator calculator

# introduce user to the program
print("welcome to my flexible calculator!")

print("pick an operation! ")

# just for stupid proof




while True:
    # ask user for what equation they want
    equation = input("sum1, average2, max3, min4, product5, please type 1-5:\n ")
    
    # Setting the operation

    if equation == "1":
        print("alright addition, now I need numbers!")
    
    # write down process in here and others
    # after user finishes writing their numbers will calculate the sum 
        while True:
            choice = input("you can plug numbers in now, type ' done ' when you're finished")
           
            numbers = []
            def sum(numbers):
            
                total = 0
                choice = input("you can plug numbers in now, type ' done ' when you're finished")
           

            if choice > 0 or choice < 0:
                    numbers.append(choice)
             
                elif choice == "done":
                    for num in numbers:
                        total += num
                    return total 
                else: 
                 print("invalid")

            
   
        


    if equation == "2":
        print("alright average, now I need numbers!")



    if equation == "3":  
        print("alright max, now I need numbers!")




    if equation == "4":
        print("alright addition, now I need numbers!")


    if equation == "5":
        print("product, now I need numbers!")

   