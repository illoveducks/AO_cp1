# AO 1st password strength CP1 

# make a forever loop, breaks when requirements are met

# the computer will check how long the password is if it's above 8, then add 1 point, if not suggest making it longer
# the computer will check if one of the letters is uppercase, if it one of the letters is, it will move on and add 1 point, if not go back up and suggest adding one
# the computer then will check if is a lowercase letter, then if there is it will add a point, if not, it will go back up and suggest a lowercase letter
# the computer then will check for a special symbol if it does add 1 point, if the password doesn't have one, then it will go back up, and suggest it
# the computer will then check for a number, if it has a number add one point, congrats you made a good password! if not, go back up and suggest a number
# could import " re " which is just regular expressions would make life easier




# This just makes life easier, by a lot, stands for regular expressions
import re 
# make a forever loop, breaks when requirements are met
while True:


# Just stating the requirements
    print(" requirements: password length must be 8 or more characters, must have numbers, must have one of the given symbols !@#$%^&* any of those work must have one. Must have a lower case and uppercase letter.")
# points are your password point strength
    points = 0
# ask user for a password
    password = input("please make a password:\n")
    if len(password) < 8:     
# the computer will check how long the password is, if it's shorter than 8 char, then it will put you back up
        print("You may wanna make your password longer: weaker than weak if you've only gotten here.")
        continue
    else: 
        points += 1 # adds a point if condition is met
    if not re.search("[A-Z]", password):
    # checks for a capital letter if none, puts youy back up
        print("password must have an upper case letter: weak")
        continue
    else:
        points += 1 # adds a point if condition is met
    if not re.search("[a-z]", password):
    # checks for a lowercase letter if none puts you back up
        print("password must contain a lower case letter: somewhat weak")
        continue
    else: points += 1 # adds a point if the condition is met
    if not re.search("[0-9]", password): # checks for a number, if none puts you back up
        print("please add a number.  medium if you've made it this far  ")
        continue
    else: 
        points += 1 # adds a point of a condition make
    if not re.search("[!@#$%^&*]", password): # checks for a special symbol, if none puts you back up
        print("add one of the given symbols please: somewhat strong")
        continue
    else:
        print("Congrats! You've made a strong passowrd. ")
        points += 1 # final point added
        print(points, "points That is pretty strong! ")
        break 










