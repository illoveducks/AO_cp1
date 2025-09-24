# 1st AO User sign in


print("please type in your username and password")

user_input = input("username:\n")

user_inputpass = input("password:\n")

user1 = ("bobthebuilder8")
user1pass = ("PassWorld157")

user2 = ("JimmyTheChild168")
user2pass = ("IlikeCats12")

user3 = ("DucksareCool")
user3pass = ("DucksAremyFav!")


users = (user1)

if user_input == user1 and user_inputpass == user1pass:
    print("welcome back!", user1, "Nice to see you again, do whatever you want to do have fun! ")
elif user_input == user2 and user_inputpass == user2pass:
    print("welcome back!", user2, "do as you please, continue your journey. ")
elif user_input == user3 and user_inputpass == user3pass:
    print("Hey welcome back!", user3, "Do your duck things I guess.") 
else:
    print("you may hae typed your username or password wrong, or you don't have an account")