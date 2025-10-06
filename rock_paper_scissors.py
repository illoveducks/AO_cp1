# AO 1st Rock paper Scissors!

print("welcome to my rock paper scissors game!")

import random

rock = "rock"
paper = "paper"
scissors = "scissors"
score = "score"
quit = "quit"
child_game = [rock, paper, scissors]

my_points = 0 
your_points = 0

import random

while True:
    
    print("let's see who wins in this child's game!")
    
    start = input(f" rock, paper, scissors: Pick one We'll see who wins, to see the scores type score, to leave type quit:\n")
  
    if my_points > 15 or your_points > 15:
        print("haha...I had fun, but it's time we take a break alright? See you soon!")
        break
    if start == score:
        print(f"here are the scores! here are mine {my_points} and yours! {your_points} ")
        continue
    if start == quit:
        print("goodbye! I had fun, hope you did to!")
        break
    if random.choice(child_game) == rock and start == paper:
        print("Aw, man, the paper succumbs the rock... You win! That's a point for you! ")
        your_points += 1
        continue
    elif random.choice(child_game) == rock and start == scissors:
        print("Hah! Got you this time!")
        my_points += 1
        continue
    elif random.choice(child_game) == rock and start == rock:
        print("Oooo it's a tie! ")
        continue
    if random.choice(child_game) == scissors and start == paper:
        print(" Snip snip! I win this round! ")
        my_points +=1
        continue
    elif random.choice(child_game) == scissors and start == rock:
        print(" Aw... the rock broke my scissors... :( you win this round!")
        your_points += 1
        continue
    elif random.choice(child_game) == scissors and start == scissors:
        print("I wish there was like a little war between scissors... Like thumb wars...Oh well! It's a draw!")
        continue
    if random.choice(child_game) == paper and start == rock:
        print("Yay! A point for me! Paper goes over rock!")
        my_points += 1
        continue
    elif random.choice(child_game) == paper and start == scissors:
        print(" aw... how rude of cutting my paper into pieces! You're cleaning that up right...? ")
        your_points += 1
        continue
    elif random.choice(child_game) == paper and start == paper:
        print("handshake, hehe...it's a tie ")
        continue
   

    if start != rock and paper and scissors and score and quit:
        print("sorry, that's not a thing in this game... :( ")
        continue
    if my_points > 15 or your_points > 15:
        print("haha...I had fun, but it's time we take a break alright? See you soon!")
        break
    




