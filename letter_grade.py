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
elif grade < 74 and grade > 72:
    print("you have a C, do better. ")
elif grade > 70 and grade < 72:
    print("You got a C-, no words")
elif grade > 66 and grade < 70:
    print("A D+, do better")
elif grade > 64 and grade < 66:
    print("D, ouch, you can do better")
elif grade > 60 and grade < 64:
    print(" A D... Really?")
else:
    print(" You're a failure, that's what an F is, you should be in a different class, or do better.")