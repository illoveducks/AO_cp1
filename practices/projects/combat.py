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
    attacks = ["punch ", "adrenaline",  ]
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
    attacks = [ "flimsy punch", " Shield up! ", " Recovery " ] 
print("passive: heals over time while in battle, and starts with a minion ")

if player == 3: 
    print(" A Broken soul...One that has ventured many places, yet so lost in the world... Broken, a character that utilizes recharging ' shield ' and cannot heal. ")
    health = 1
    shard = 5
    damage = 10
    attacks = ["isolate", "glass stab", "Break ", "repair job " ]
    print("passive ' Break me away ': upon losing all your shield you release shards everywhere damaging enemies by how much damage you do cut in half")
    print(" another passive: any attack this character inflicts bleed onto enemies except for break me away. A permamnent debuff that can stack up to five ")
    

elif player == 4:
    print(" The mage utilizies mana and  mana recharge, although must be careful one wrong move can mess up your run! ")

    health = 18
    print(" damage depends on spell ")
    mana = 36
    attacks = [ "fireball", "ice shard", "arcane shield "]
    print("passive regens mana and is the only character that uses mana!")
    print(" if arcane shield is broke in one hit then you will stun the enemy for two turns! ")


print("Now that you have a class you should pick what difficulty you want! There are three and one secret one, you'll have find that out yourself!")

print(" pick between easy, normal, and hard :D\n")

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
elif difficulty > 3 and player == 3:
    print("My reality, the true story...My broken world... ")