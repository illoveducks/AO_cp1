# AO 1st Combate Program


import random


print("Welcome! It's been a while since I have seen a traveller... We don't get many visitors anymore.")

fighter = "fighter"

player = input(f"Choose a class, fighter, defender, broken, mage:\n")


easy = "easy"
normal = "normal"
hard = "hard"
nightmare = "nightmare"


if player == fighter:
    print("The fighter is class that uses brute force to get his way, sadly... he doesn't have much health")
    health = 20
    damage = 10
    defense = 0
    attacks = ["punch ", "adrenaline",  ]
    print(f"here are your stats, {health, damage, defense,} here are your abilities/attacks for the time being {attacks}  " )
    print("Now that you have a class you should pick what difficulty you want! There are three and one secret one, you'll have find that out yourself!")
    print(" pick between easy, normal, and hard :D\n")
    print(" easy (for the weak) makes enemies do lower damage, and less encounters ")
    print("normal is just the normal game ")
    print("hard makes enemies do more damage and ignore some armor")

difficulty = input("difficulty")

if 



