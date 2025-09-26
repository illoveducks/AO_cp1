# AO 1st CP1


grade = float(input("what is your grade:\n"))




if grade >= 92:
    print("congrats! You have an A. Now keep that grade and don't let it go down")
elif grade > 85 and grade < 92:
    print("you have a B+ that's pretty good, now I know you can do better! Push yourself ")
elif grade >= 83 and grade <= 85:
    print("You got a B, you can do better, but pretty good so far!")
elif grade > 80 and grade < 82:
    print("you have a B- congrats! You're doing pretty well, but you can do better for sure. ")
elif grade >= 76 and grade < 80:
    print(" You have a C+, you can do better. ")
elif grade > 73 and grade < 76:
    print("you got a C, you can try pushing your grade a bit better.")
elif grade > 70 and grade < 73:
    print("wow a C-... you're close to a D please... do better ")
elif grade < 70 and grade > 60:
    print(" wow... a D... really? there is no point in me put the and you're failing, come on push yourself harder ")
elif grade < 50 and grade > 10:
    print("an F, you're failing, i have no words push yourself harder") 
else:
    print("you don't even deserve a letter.")