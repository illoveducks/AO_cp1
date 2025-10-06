# AO 1st Rock paper Scissors!

print("welcome to my rock paper scissors game!")


import random

rock = "rock "
paper = "paper"
scissors = "scissors"
child_game = ["rock", "paper", "scissors"]

my_points = 0 
your_points = 0
while True:
    
    print("let's see who wins in this child game!")
    
    start = input(f"{rock} {paper} {scissors} Pick one We'll see who wins to quit the game, please type 4:\n")
    
    if random.choice(child_game) == rock and start == paper:
        print("Aw, man...You win! That's a point for you! ")
        your_points += 1
        continue


    
    
    
    
    
    if start 
    print("sorry, that's not a thing in this game... :( ")
    
    
    
    if start == "4":
        print("goodbye! I had fun, hope you did to!")
        break
    




