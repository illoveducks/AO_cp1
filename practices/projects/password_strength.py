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
    print(" requirements: password length must be 8 or more characters, must have numbers, must have a special symbol things like @ and things like that. Must have a lower case and uppercase letter.")
# points are your password point strength
    points = 0
# ask user for a password
    password = input("please make a password:\n")

    if len(password) < 8:     
# the computer will check how long the password is if it's above 8, then add 1 point, if not suggest making it longer
        print("You may wanna make your password longer")
        continue
    elif len(password) >= 8:
       points += 1
    elif re.findall("[A-Z]"):
        break
    
        
    # the computer will check if one of the letters is uppercase, if it one of the letters is, it will move on and add 1 point, if not go back up and suggest adding one
 










