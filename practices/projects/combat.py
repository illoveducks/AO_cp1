# AO 1st Combate Program


import random


print("Welcome! It's been a while since I have seen a traveller... We don't get many visitors anymore.")



player = int(input(f"Choose a class, fighter1, defender2, broken3, mage4:\n"))


easy = "easy"
normal = "normal"
hard = "hard"
nightmare = "nightmare"


if player == 1:
    
    print("The fighter is class that uses brute force to get his way, sadly... he doesn't have much health")
    health = 20
    damage = 10
    defense = 0
    attacks = ["punch1 ", "adrenaline2",  ]
    print(f"here are your stats, {health, damage, defense,} here are your abilities/attacks for the time being {attacks}  " )
    print("Now that you have a class you should pick what difficulty you want! There are three and one secret one, you'll have find that out yourself!")
   
    print(" pick between easy, normal, and hard :D\n")
    print(" easy (for the weak) makes enemies do lower damage, and less encounters ")
    print("normal is just the normal game ")
    print("hard makes enemies do more damage and ignore some armor")




elif player == 2:
    print(" Defender has a neat passive where he spawns with a minion! This is sort of the summoner class. That utilizes his minions.")
    health = 50
    damage = 1
    defense = 15
    attacks = [ "flimsy punch1", " Shield up!2 ", " Recovery 3" ] 
    print("passive: heals over time while in battle, and starts with a minion ")


elif player == 3: 
    print(" A Broken soul...One that has ventured many places, yet so lost in the world... Broken, a character that utilizes recharging ' shield ' and cannot heal. ")
    health = 1
    shard = 5
    damage = 10
    attacks = ["isolate1", "glass stab2", "Break3 ", "repair job4 " ]
    print("passive ' Break me away ': upon losing all your shield you release shards everywhere damaging enemies by how much damage you do cut in half")
    print(" another passive: any attack this character inflicts bleed onto enemies except for break me away. A permamnent debuff that can stack up to five ")
    

elif player == 4:
    print(" The mage utilizies mana and  mana recharge, although must be careful one wrong move can mess up your run! ")

    health = 18
    print(" damage depends on spell ")
    mana = 36
    attacks = [ "fireball", "ice shard", "arcane shield ", "focus "]
    print("passive regens mana and is the only character that uses mana!")
    print(" if arcane shield is broke in one hit then you will stun the enemy for two turns! ")

if player > 4 or player < 1:
    print("...The lost... ")
    health = 1
    shard = 3
    damage = 12
    print("Passive: every attack inflicts bleed, stacks up to 5")
    print("Upon dying as this charcter you die, forever. ")


print("Now that you have a class you should pick what difficulty you want! There are three and one secret one, you'll have find that out yourself!")

print(" pick between easy1, normal2, and hard3 :D")

print(" easy (for the weak) makes enemies do lower damage, and less encounters ")

print("normal is just the normal game ")

print("hard makes enemies do more damage and ignore some armor")



difficulty = int(input("difficulty:\n"))

if difficulty == 1:
    print(" Aw... Sort of disapointing but we'll go with it. ")
elif difficulty == 2:
    print("nothing wrong with this!")
elif difficulty == 3:
    print("daring one aren't you...")
elif difficulty > 3 or difficulty < 1:
    print("A nightmare that swept the town... ")




    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        print("Welcome to the training grounds! Where every traveller starts their journey! ")
        print("go attack that dummy!")

if player == 1:
    pass
while True:
    if player == 1:
        print(f"{attacks}, this is your moveset, your attacks do {damage}, when not affected by something special like an item. Go ahead hit the dummy!")
    moveset = int(input("punch1, adrenaline2, you have to type the number by the way\n"))
    if moveset == 1:
        print("you hit the dummy, the dummy falls over, ")
        print("Yay! You...Uh...? Killed a dummy? Oh well...? ")
        break
    elif moveset == 2:
        print("Adrenaline makes you do 5+ extra damage sadly you can only stack this one time... last two turns ")
    if moveset > 2 or moveset < 1:
        print("you don't have anything else equipped. to do that!")

while True:
    if player == 2:
        print(f"{attacks}, this is your moveset, your attacks do {damage}, when not affected by something special like an item. Go ahead and let your minion do the work")




