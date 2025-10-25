# AO 1st Combate Program
# sorry for not making this... turn based...I sort of took inspiration from limbus company it's a game. Where both the player and entity go at the same time. 
# This has helped me a lot to learn so... yeah... I'm finding this fun, 
import random as ran


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
    status = []
    attacks = ["punch1 ", "adrenaline2",  ]
    print(f"here are your stats, {health, damage, defense,} here are your abilities/attacks for the time being {attacks}  " )
    print("Now that you have a class you should pick what difficulty you want! There are three and one secret one, you'll have find that out yourself!")
   


elif player == 2:
    print(" Defender has a neat passive where he spawns with a minion! This is sort of the summoner class. That utilizes his minions.")
    health = 50
    damage = 1
    defense = 3
    status = []
    attacks = [ "flimsy punch1", " Shield up!2 ", " Recovery 3" ] 
    print("passive: heals over time while in battle, and starts with a minion ")


elif player == 3: 
    print(" A Broken soul...One that has ventured many places, yet so lost in the world... Broken, a character that utilizes recharging ' shield ' and cannot heal. ")
    health = 1
    shard = 5
    damage = 10
    status = ["cold"]
    attacks = ["isolate1", "glass stab2", "Break3 ", "repair job4 " ]

    print(" another passive: any attack this character inflicts bleed onto enemies except for break me away. A permamnent debuff that can stack up to five ")
    

elif player == 4:
    print(" The mage utilizies mana and  mana recharge, although must be careful one wrong move can mess up your run! ")

    health = 18
    print(" damage depends on spell ")
    mana = 36
    shard = 0
    status = ["thinker",]
    attacks = [ "fireball", "ice shard", "arcane shield ", "focus "]
    print("passive regens mana overtime and is the only character that uses mana!")
    print(" if arcane shield is broke in one hit then you will stun the enemy for two turns! ")

if player > 4 or player < 1:
    print("...The lost... ")
    health = 1
    shard = 3
    damage = 12
    status = []
    attacks = ["katar stab", "weave", "repair job"] 
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
elif  difficulty != 1 or difficulty != 2 or difficulty != 3:
    print("A nightmare that swept the town... ")




    if difficulty == 1 or difficulty == 2 or difficulty == 3:
        print("Welcome to the training grounds! Where every traveller starts their journey! ")
        print("go attack that dummy!")


while True:
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        break
    if player != 1:
        break
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
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        break
    if player != 2:
        break
    if player == 2:
        print(f"{attacks}, this is your moveset, your attacks do {damage}, when not affected by something special like an item. Go ahead and let your minion do the work")
        print("look! Your minion has spawned it's an adorable bee, sadly they can only sting you can control your minions on what they do! ")
        print("do something! ")
        moveset = int(input("flismy punch1, shields up2, recovery3\n"))
        movesetBee = int(input("sting1, sting does 5 damage \n"))
    if moveset == 1 and movesetBee == 1:
        print("wow... Your punch was really weak it just made the dummy wobbke...")
        print("your bee has killed? the dummy! ")
        break
    elif moveset == 2 and movesetBee == 1:
        print("you raise your shield to in hopes to tank a hit from a dummy...? for your bee ")
        print("your bee stings the dummy! The dummy falls over... ")
        break
    elif moveset == 3 and movesetBee == 1:
        print("you attempt to heal you and your bee... You're already at full health, same with the bee ")
        print("your bee stins the dummy! It...Falls over. ")
        break
    if moveset > 3 or moveset < 1 and movesetBee == 1:
        print("You don't have anything  equipped in that slot! ")
        print("your bee stings the dummy... It falls over. ")
        break
    elif moveset == 1 or moveset == 2 or moveset == 3 or moveset > 3 or moveset < 1 and movesetBee != 1:
        print("you know this character is really weak...? Can't even knock over a dummy... ")


while True:
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        break
    if player != 3:
        break
    print(shard, "shard ")
    if player == 3:
        print(f"{attacks}, this is your moveset, your attacks do {damage}, ")
        print("this class is weird, glass stab cannot be used without being hurt or not using break, repair job heals yourself repairs your shield ")
    moveset = int(input(" isolate1, glass stab2, break3, repair job4 \n"))
    if shard == 5 and moveset == 2:
        print("not broken enough... ")
    elif shard < 1 and moveset == 3:
        print("Stop... ")
    elif moveset == 3:
        print("You take a piece of your self and weld it in your hand ")
        shard -= 1
    elif shard <= 4 and moveset == 2:
        print("you lung at the dummy, it breaks ")
        break 
    elif moveset == 4 and shard == 5:
        print("no more...")
    elif moveset == 4:
        print(" an attempt to fix something that's already broken")
        shard += 1 
    elif moveset == 1:
        print(" you put arm ahead of yourself in attempt to block them... ")
        print("when attacked does damage back ")

while True:
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        break
    if player != 4:
     break
    print("mana:",mana,)
    print("shard:",shard,)

    if player == 4:
    
         print(f"{attacks}, this is your moveset, your attacks do, you utilize mana! ")
    moveset = int(input("fireball1, ice shard2, arcane shield3 , focus 4\n"))

    if moveset == 1:
        print("you cast a fire ball and the dummy explodes... 10 damage! ")
        mana -= 7
        break
    if moveset == 2:
        print("you cast an ice shard and it peirces the dummy it falls over... ")
        mana -= 10
        break
    if moveset == 3 and shard > 0:
        print("you already have a shield!")
    elif moveset == 3:
        print("you cast a shield upon yourself give yourself 2 shard")
        shard += 2
    elif moveset == 3 and shard > 0:
        print("you already have a shield!")
    if moveset == 4 and mana == 56:
        print("too much mana! ")
    elif moveset == 4:
        print("you can use this as many times as you want, mana cannot exceed 56 ")
        mana += 10

while True: 
    if difficulty != 1 or difficulty != 2 or difficulty != 3:
        break
    print("shard:",shard)
    if player != 1 and player != 2 and player != 3 and player != 4:
        print("A lost soul... ")
        print(f"{attacks} this is your moveset, this class takes triple damage compared to others. ")
    moveset = int(input("katar stab 1, weave2, repair job 3 \n"))
    if moveset == 1:
        print("you swiftly stab the dummy, it falls over")
        break
    if moveset == 2:
        print("I thought to myself, what is there too dodge? ")
    if moveset == 3 and shard == 3:
        print("there's nothing left to fix")
    elif moveset == 3:
        print("show me mercy... ")
        shard += 1


if difficulty == 1 or difficulty == 2 or difficulty == 3:
    print("those are the basics to combat! Congratulatons you can leave the training grounds! ")
    print("Although... i will say... There are things out there now, weird creatures that went through out town... Sadly.")
    print("maybe you can help!")












if difficulty < 1 or difficulty > 3 and player == 3 or player < 1 or player > 4:
        print("you know why you are here...")
        print("that thing haunts me... To this day, the recollection of my past... ")
elif difficulty < 1 or difficulty > 3 and player == 1 or player == 2 or player == 4:
        print(" You don't belong here... ")
        print("there will sadly be no content for these other classes in nightmare mode...")

health1 = 50
shardC = 1
status1 = []
damage1 = 9999
while True:
    if player == 3 and difficulty == 1 or difficulty == 2 or difficulty == 3:
        break
    if player == 3 and difficulty < 1 or difficulty > 3:
     print("the creature that still haunts me...")
    print("HP", health)
    print("shard", shard)
    print("status:",status)
    print("the thing...HP:",health1)
    print("nightmare...shard:", shardC)
    punch = 1
    lunge = 2
    recollection = 3
    attacks1 = ["1", "2", "3"]
    moveset = int(input("isolate1, glass stab2, break3, repair job4\n" ))
    if health < 1: 
        print("you were never enough...")
        break
    elif health1 < 1:
        print("Maybe you stand a chance in the world you are broken in... ")
        print("that is all there is at the moment for nightmare mode on this class!")
        break
    if ran.choice(attacks1) == "1" and shard == 0:
        print("you feel hopeless...You give up...You sit there, wide open")
        health -= damage1
    if ran.choice(attacks1) == "1" and shardC > 0 and moveset == 1:
        print("you hear there voices...You feel that hit... It hurt you... that 'thing'.. seemed unhurt...")
        shard -= 1 
        shardC -= 1 
    elif ran.choice(attacks1) == "1" and shardC == 0 and moveset == 1:
        print("you feel at peace in a way, the violent punch seems to not hurt...")
        shard -= 1
        health1 -= damage

    
    elif ran.choice(attacks1) == "2" and moveset == 1 and shard == 0:
        print("it was too late, you couldn't react in time... ")
        health -= damage1
    if ran.choice(attacks1) == "2" and moveset == 1 and shardC >= 1:
        print("That hurt... You have been knocked back... Get up... ")
        shard -= 2 
        print("it laughs as you get up... ")

    elif ran.choice(attacks1) == "2" and moveset == 1 and shardC ==0 and shard == 0:
        print("you feel it, you dodge it, you subconciously repair yourself while you have the chance...")
        shard += 1
        damage = 0
        print("the creature seemed bothered at the sight of that ")

    elif ran.choice(attacks1) == "2" and moveset == 1 and shardC ==0:
         print(" you know it's coming, you move out the way and ram into it...")
         health1 -= 12
         shard -=1 
         print("that creature gets back up, groaning, he has a frown now... ")

    if ran.choice(attacks1) == "3" and moveset == 1 and shard == 0:
        print("the flashbacks were too much...You laid there in dispair...Consumed by darkness...")
        break
    elif ran.choice(attacks1) == "3" and moveset == 1:
        print("you feel a little tingle. you feel like it's safe to put your arm down")
        shardC +=1
        health1 += 5
    elif ran.choice(attacks1) == "3" and moveset == 1 and shardC == 0:
        print("you know what it's doing you fight it back, and repair yourself at the same time ")
        shard += 1


    
    
        
    




  
  

