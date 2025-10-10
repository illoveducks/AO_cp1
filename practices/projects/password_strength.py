# AO 1st password strength CP1 

# make a forever loop, breaks when requirements are met

# ask user for a password

# the computer will check how long the password is if it's above 8, then add 1 point, if not suggest making it longer
# the computer will check if one of the letters is uppercase, if it one of the letters is, it will move on and add 1 point, if not go back up and suggest adding one
# the computer then will check if is a lowercase letter, then if there is it will add a point, if not, it will go back up and suggest a lowercase letter
# the computer then will check for a special symbol if it does add 1 point, if the password doesn't have one, then it will go back up, and suggest it
# the computer will then check for a number, if it has a number add one point, congrats you made a good password! if not, go back up and suggest a number

while True:

    print("this is a password checker, please make a password and I will see how strong it is, this password checker does not end until all requirements are met")


    print(" requirements: password length must be 8 or more characters, must have numbers, must have a special symbol things like @ and things like that. Must have a lower case and uppercase letter.")

    points = 0

    password = input("please make a password:\n")

    if len(password) < 8:
        print("You may wanna make your password longer")
        continue
    elif len(password) > 8:
       print("length is good")
       points += 1
    
    if (password)is.lower > 0:
        points += 1
        print("good")
    
 










