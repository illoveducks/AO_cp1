# AO 1st Adventure game! 

import random as r

import time




attempts = 0


Marks_stats = { "min Hp": 20, # How much you heal after the end of a fight. 
                "damage": 5,
               "health": 20,
               "defense": 0,
                "max HP": 23 }

Status = { "wolf": "alive",
            "royal guard": 'alive',
            "panda": ' alive',
            "desert golem": 'alive?',
            "program": 'unbroken'}

Marks_weapon = "none"

weapons = {
    "stick": 3,
    "copper sword": 7,
    "the great bamboo sword": 5

}

armor = {'sandstone': 2,
         'iron': 4,
         'the royal shield': 5}


Key_shard = 'broken'
Key_shard2 = 'shattered'


wolf = {'HP': 50,
        'scratch': 5,
        'pounce': 3,
        'howl': 0}

desert_golem = {'HP': 100,
                'wind up': 0,
                'hefty wind up': 0,
                'swing': 11,
                'holy gem': 4,
                'solidify': 1,
                 'defense': 2}

panda = { 'HP': 75,
        'scratch': 5,
         'lazy jump': 10,
         'sleep ': 3,
         'eat': 1,
         'defense': 1}

Royal_guard = {'HP': 60,
               'defense': 6,
               'swing': 6,
                'aggravate': 2 }






Marks_location = "home"

print("I woke up, I wonder, I wonder what's going on in town today. I need to get ready")

time.sleep(1)

print("I made breakfast, something is wrong, I feel it, I looked outside, to see a world ' shattered ', why?")

time.sleep(1)

print("After finishing breakfast, I got up, should we head outside?")

while True:
    
    outside = input("yes, no\n").strip()

    str(outside)

    if outside == 'yes':
        Marks_location = "outside"
        print("okay, I'll go, ")
        time.sleep(0.5)
        print("I opened the door, I was right, the town, it feels empty, at least my neighbor is here.")
        time.sleep(0.7)
        print("Hey Mark! How's it going! There are new bridges in our town! That's where most of our town is, gone! i'm heading to the new town, the two bridges over there, the one on the left leads to the forest I'd recommend going there! The on the right leads to the desert... and the one over here leads to the new town! See you later Mark! ")
        print("okay, thanks for telling me, hey, I got a question, do you ever feel like a puppet on strings?")
        time.sleep(1)
        print("no...weird question, oh well, see you around!")
        time.sleep(1)
        break
    elif outside != 'yes' and outside != 'no':
        print("what...?")
    
    elif outside == 'no':
        freedom = input("Are you sure...You want to end it so early...?\n")
        if freedom == 'yes': 
            print("freedom...? ")
            break
        else:
            print("haha you're so funny... let's go outside")
            Marks_location = "outside"
            time.sleep(0.5)
            print("I opened the door, I was right, the town, it feels empty, at least my neighbor is here.")
            time.sleep(0.7)
            print("Hey Mark! How's it going! There are new bridges in our town! That's where most of our town is, gone! i'm heading to the new town, the two bridges over there, the one on the left leads to the forest I'd recommend going there! The on the right leads to the desert... and the one over here leads to the new town! See you later Mark! ")
            print("okay, thanks for telling me, hey, I got a question, do you ever feel like a puppet on strings?")
            time.sleep(1)
            print("no...weird question, oh well, see you around!")
            time.sleep(1)
            break
while True:
    if attempts != 0:
        break
    go = input("where should I go? \n left leads me to the forest, \n right leads me to the desert, \n forward leads me to the new town, \n or back home... ( type back to head home )\n ").strip()
    
    str(go)

    if go == 'left':
        print("I walked towards the bridge, oh so slowly, I got there at last, crossed it and I finally entered the grand forest")
        Marks_location = 'forest'
        break
    elif go == 'right':
        print(" I walked towards the bridge, slowly, I finally got there, to cross it, to be met with the sandy and dry climate. ")
        Marks_location = 'desert'
        break
    elif go == 'forward': 
        Marks_location = 'new town'
        print("I may as well head where my friend went. to the new town! ")
        break

if Marks_location == 'forest':
    print("there are sticks everywhere...")
    while True:
        if Status["wolf"] == 'dead':
            break
        print("why did we go here...? What's your goal...? ")
        time.sleep(1)
        go = input("pick up (stick) forward, left, ")



        if go == 'left':
            print("and so i Ventured once more, listening to those voices that carry me, ")
            time.sleep(1)
            print("I soon found a viny place, I think, I'm in the jungle")
            Marks_location = 'jungle'
            break 

        elif go == "pick up":
            print("okay...?") 
            Marks_stats["damage"] += weapons["stick"]
            Marks_weapon = 'stick'

            while attempts == 0:
                if Status['wolf'] == 'dead':
                    break
                print("what now? ")
                go = input('forward, left, right, \n ' )

                if go != 'forward' and go != ' left ' and go != 'right':
                    print('huh...?')
                    continue

                if go == 'forward':
                    print("And so I set forth, I walked...And walked...Soon I encountered a sleeping wolf, it had looked famaliar")
                    time.sleep(0.5)
                    print("It's intimidating...but resting")
                    time.sleep(0.4)
                    go = input('wake it up, head to the gate, right, back \n ')   
                    
                    if go == 'wake it up':
                        print("i screamed at the wolf, it let out a howl as if it were calling something, there is no turning back, no longer...")
                        time.sleep(0.5)
                        while True:
                            if Status['wolf'] == 'dead':
                                print("Why are we here again...? To mourn over it...?")
                                break
                            print("looks...worried...?")

                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
        
                            print("it's going for an attack")

                            if Marks_stats['health'] < 1:
                                print("I can't push myself any further...I'm sorry friend...")
                                time.sleep(1)
                                print("there's always a next time...right...? ")
                                time.sleep(1)
                                print("right...?")
                                break
                            if wolf["HP"] < 1:
                                Status["wolf"] = 'dead'
                                print("I did it! I did... It...? I don't feel good...I feel a recollection...Grief...")
                                time.sleep(1)
                                print("The memories...Ugh...I have a feeling to head to the gate. ")
                                Marks_stats["damage"] += 1
                                if Key_shard == 'fixed':
                                    Key_shard2 = 'unshattered'
                                elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                                break

                            attack = input("block, swing, maybe I should block \n ").lower().strip()

                            str(attack)
                            if attack != 'block' and attack != 'swing':
                                print('now is not the time to mess around...')

                            if attack == 'block':
                                print(" I heard it dent my stick...Why is this stick so durable? i felt...better...")
                                Marks_stats["health"] += 3
                                print("my health ", Marks_stats["health"])
                                print("wolf's health", wolf["HP"])

                            elif attack != 'block':
                                Marks_stats["health"] -= wolf["scratch"]
                                print("my health ", Marks_stats["health"])
                                print("wolf's health", wolf["HP"])
                            if attack == 'swing':
                                print("I got it! uh oh...")
                                time.sleep(1)
                                print("ouch...")
                                Marks_stats["health"] -= wolf["pounce"] 
                                wolf["HP"] -= Marks_stats["damage"]
                                print("my health ", Marks_stats["health"])
                                print("wolf's health", wolf["HP"])
                            if Marks_weapon == 'stick':
                                attack = input("block, swing \n ").lower().strip()
                                if attack == 'block':
                                    print('uh oh...')
                                    time.sleep(0.5)
                                    print("the wolf had a great leap, and pounced on me, maybe I can't block that...")
                                    Marks_stats["health"] -= wolf['pounce']
                                    print("my health ", Marks_stats["health"])
                                    print("wolf's health", wolf["HP"])
                                    time.sleep(0.6)
                                    print("Didn't hurt...much...?")
                                    time.sleep(0.7)
                                    print('the creature let out a frantic howl, but nothing came...')
                                    continue


                                elif attack == 'swing':
                                    print("I landed a hit! But...It leaped at me right afterwards... ")
                                    wolf["HP"] -= Marks_stats["damage"]
                                    Marks_stats["health"] -= wolf["pounce"]
                                    time.sleep(0.7)
                                    print("it let out a frantic howl...But nothing came...")
                                    continue





        if go == 'forward':
            print("And so I set forth, I walked...And walked...Soon I encountered a sleeping wolf, it had looked famaliar")
            time.sleep(0.5)
            print("It's intimidating...but resting")
            while True:
                if Status["wolf"] == 'dead':
                    break
                if attempts == 0:
                    go = input('wake it up, head to the gate, right, back \n ')
                if attempts != 0:
                    break
                if go == 'wake it up':
                    print("I punched the sleeping creature, it woke up with a fierce howl, but it looked like it was calling to something")
                    time.sleep(0.5)
                    while True:
                        if Status["wolf"] == 'dead':
                            break

                        print("my health ", Marks_stats["health"])
                        print("wolf's health", wolf["HP"])
                        print("Maybe I should block")

                        attack = input('punch, block \n ')
                        str(attack)

                        if Marks_stats['health'] <= 1:
                            print("I can't push myself any further...I'm sorry friend...")
                            time.sleep(1)
                            print("there's always a next time...right...? ")
                            time.sleep(1)
                            print("right...?")
                            attempts +=1
                            break
                        if wolf["HP"] <= 1:
                            Status["wolf"] = 'dead'
                            print("I did it! I did... It...? I don't feel good...I feel a recollection...Grief...")
                            time.sleep(1)
                            print("The memories...Ugh...I have a feeling to head to the gate. ")     
                            print('we have to go... somewhere')
                            Marks_stats["damage"] += 1
                            Marks_stats["health"] += Marks_stats["min Hp"]
                            attempts += 1
                            if Key_shard == 'fixed':
                                Key_shard2 = 'unshattered'
                            elif Key_shard == 'broken':
                                Key_shard = 'fixed'
                            break
        


                        if attack != 'block' and attack != 'punch':
                            print('now is not the time to be messing around...')
                            attack = input("punch, block \n ")
                        if attack == 'punch':
                            print("I hit the wolf, it scratched me right back, it hurt.")
                            Marks_stats["health"] -= wolf["scratch"]
                            wolf["HP"] -= Marks_stats["damage"]
                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
                        elif attack == 'block':
                            print("My arms, they felt like they were made of steel, I feel...Better")
                        if Marks_stats["health"] >= Marks_stats["max HP"]:
                            Marks_stats["health"] = Marks_stats["max HP"]

                        elif Marks_stats["health"] < Marks_stats["max HP"]:
                            Marks_stats["health"] += 3

                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
                        
                        attack = input("what now? punch, block \n ")

                        if attack != 'block' and attack != 'punch':
                            print('now is not the time to be messing around...')
                            attack = input("punch, block \n ")
                            continue

                        if attack == 'punch':
                            print("I hit it but it immediately leaped towards me")
                            wolf["HP"] -= Marks_stats["damage"]
                            Marks_stats["health"] -= wolf["pounce"]
                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
                            time.sleep(1)
                            print('the wolf let out a frantic howl like if it were calling to something...But nothing came...')
                            continue
                        elif attack == 'block':
                            print('uh oh...')
                            Marks_stats["health"] -= wolf["pounce"]
                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
                            time.sleep(1)
                            print("As I got up, I looked at it... It howled, a fierce one.")
                            continue






if Marks_weapon == "none" or Marks_weapon == "stick" or Marks_weapon == "copper sword" or Marks_weapon == "bamboo":
    while True: 
        go = input("what now...? left, forward")
        if go == 'left':
            print(" So I went to my left, and found a viny place, I think, I'm in the jungle")
            Marks_location = ' jungle'
            break
        while Marks_location == 'jungle':
            print("we're here. ")
            print("this place is beautiful...")
            time.sleep(1)
            print('where should we go...? Although...I do not want to venture to far in here.')
            go = input('left, forward \n ')
    
            if go != 'left' or go != 'forward':
                print("what...?")
                continue
            
            if go == 'forward' and Marks_weapon == "bamboo sword": 
                print("I've already been to the temple, no point in going in, are we heading to the new town?")
                time.sleep(1)
                print("and so I kept walking here, in this new town. ")


            if go == 'forward':
                print("I went more forward, there seemed to have been a trail, I looked up, it was a temple.")
                go == input("go inside, keep going, \n ").lower().strip()

                if go == 'go inside':
                    Marks_location == 'The Broken Temple'
                    break

            elif go == 'left': 
                print("I saw a trail of munched up bamboo...I looked up, and I saw an adorable panda.")
                go == input('fight it, gift ( give it a piece of bamboo ), go past it \n')
                if go == 'fight it':
                    print("why...it's so...Adorable...Fine.")
                    while True:
                        print(panda["HP"])
                        print(Marks_stats["health"])

                        if panda["HP"] < 1:
                            print("Darn...It was so cute...it didn't deserver this ending...")
                            print("We have to go somewhere else now...")
                            Marks_stats["defense"] += 1
                            Marks_stats["damage"] += 2
                            go == ('forward, right')
                            break
                        elif Marks_stats["health"] < 1:
                            print("That was a strong panda...Like most bears...")
                            time.sleep(1)
                            print("I'm kind of glad I didn't hurt it as much as I...Wanted to...haha...See you...Again...")
                            Marks_location == 'none'
                        
                        if Marks_weapon == 'stick' or Marks_weapon == 'copper sword' or Marks_weapon == 'bamboo sword':
                            attack = input("swing, block")

                            if attack != 'block' or attack != 'swing':
                                print("Really? You made the panda fall asleep...")
                                panda["HP"] += panda["sleep "]
                                continue

                            if attack == 'swing':
                                print("got it, it's scratch was weak, i can defenitely block that, but, I don't know if it'll make me feel better ")
                                Marks_stats["health"] -= panda["scratch"]
                                panda["HP"] -= Marks_stats["damage"]
                            elif attack == b
                            

                                












while Marks_location == 'The Broken Temple':
    if Marks_location != 'The Broken Temple':
        break
    print("there's a sign here... It reads... Solve my four math problems and you'll be rewarded...One mess up, and you'll be brought back to the beginning...")
    time.sleep(1)
    print("Rules: typing random shenanigans also sends you back.")
    time.sleep(0.3)
    print("should we do it? ")
    maybe = input('yes, no')
    if maybe == 'yes':
        print("alright... First one on the wall...")
        time.sleep(0.6)
        while True:
                print("hmm...What's 6 x 6? ")
                answer = input(" type a number, type leave, if you wanna...leave \n ")
                
                str(answer)

                if answer != '36':
                    print("wrong...Aw...")
                    continue
                elif answer == '36':
                    print("alright next one...8 x 6")
                    answer == input("type a number \n ")
                    if answer != '48':
                        print("darn...")
                        continue
                    elif answer == '48':
                        print("alright...Next one... 13 x 12 ")
                        answer == input("type a number \n ")
                        if answer != '156':
                            print("darn...")
                            continue
                        elif answer == '156':
                            print("alright... last one...11 x 11")
                            answer == input("type a number \n")
                            if answer != '121':
                                print("darn...")
                                continue
                            elif answer == '121':
                                print("hey...We did it! ")
                                time.sleep(1)
                                print("there was a door that opened infront of me, there was a pedestal in that room, with a sword")
                                print("So I walked there and grabbed it, ")
                                if Marks_weapon == 'stick':
                                    print("time to throw this piece of junk... hehe...")
                                    Marks_stats["damage"] -= weapons["stick"]
                                    Marks_stats["damage"] += weapons["the great bamboo sword"]
                                    Marks_weapon = 'bamboo sword'
                                    print("let's leave")
                                    Marks_location == 'outside of temple'
                                    break
                                elif Marks_weapon == 'none':
                                    print("A weapon, I'll take it, ")
                                    Marks_weapon = 'bamboo sword'
                                    Marks_stats["damage"] += weapons["the great bamboo sword"]
                                    print("let's leave")
                                    Marks_location == 'outside of temple'
                                    break
                                elif Marks_weapon == "copper sword":
                                    print("All of that...for nothing...Not worth changing this piece of metal for a plant")
                                    time.sleep(0.3)
                                    print("let's leave")
                                    Marks_location == 'outside of temple'
                                    break
                                


while Marks_location == 'outside of temple':
    print("Let's go somewhere else, ")
    go = input("forward, left")








if Marks_location == 'none':
    print("awww... You died :( just go back and re run the terminal, by pressing the play button again good luck next attempt! ")
                
            

print(Marks_stats)






 






# Explaining movement
# You can pick directions to make Mark go, forward, left, or right, each will lead to a different place

# Typically Forward will lead you towards the gate ( final area ),  or a boss

# Right will usually make you start heading towards a new biome or location, and same with left this is excluding the desert
