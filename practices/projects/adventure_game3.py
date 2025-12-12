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
            "panda": ' alive',
            "desert golem": 'alive?',
            "program": 'unbroken'}

Marks_weapon = "none"

weapons = {
    "stick": 3,
    "the great bamboo sword": 5,
    "rusty sword": 4,
    "???": 0
}


armor = {'sandstone': 2,
         'iron': 4,}


Key_shard = 'broken'
Key_shard2 = 'broken'

gem = 'not obtained'

armor_equipped = ' none '

wolf = {'HP': 50,
        'scratch': 5,
        'pounce': 3,
        'howl': 0}

desert_golem = {'HP': 85,
                'wind up': 0,
                'hefty wind up': 0,
                'swing': 12,
                'blocked swing': 7,
                'holy gem': r.randint(3, 5),
                'solidify': 1,
                 'defense': 2
}

golem = 'not solidified'



panda = { 'HP': 75,
        'scratch': 5,
         'lazy jump': 10,
         'sleep ': 3,
         'eat': 1}

program = {'HP': 50,
           'defense': 2,
           'error': 5,
           'virus': 12,
           'break': 50
           }



Marks_location = 'none'






print("I woke up, I wonder, I wonder what's going on in town today. I need to get ready")

time.sleep(1)

print("I made breakfast, something is wrong, I feel it, I looked outside, to see a world ' shattered ', why?")

time.sleep(1)

print("After finishing breakfast, I got up, should we head outside?")

while True:
    if Key_shard == 'fixed' and Key_shard2 == 'fixed':
        Marks_location = 'gate'
        break

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
        freedom = input("Are you sure...You want to end it so early...? yes, or whatever you want\n")
        if freedom == 'yes': 
            print("freedom...? ")
            Marks_location = 'unknown'
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
    if Key_shard == 'fixed' and Key_shard2 == 'fixed':
        Marks_location = 'gate'
        break

    if Marks_location == 'unknown':
        break
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
        Marks_location = 'new town'
        break

if Marks_location == 'new town':
    print(" this place is nice, where should we go? ")
    while True:
        go = input(" right, forward \n ").strip()
        
        if go == 'right':
            print("Alright, this place is small, I'm heading towards a building ")
            time.sleep(0.5)
            print("Welcome Welcome! I'm the blacksmitb of this city, if you can bring me a gem then I can bless you! ")
            time.sleep(0.3)
            print("like magic...?")
            print("yes like magic! it'll be nice! It'll help you on your journey, you seem like a traveller. ")
            time.sleep(0.4)
            print("I don't really believe in those kinds of things, but will do if i get a gem. ")
            time.sleep(0.3)
            print("Thank you! Also part of town is blocked by that huge sandstorm, you can see it from here, no one knows why it's there, just wanted to tell you that.")
            print("thanks I guess.")
            time.sleep(0.3)
            print("let's head back, alright? ")
            continue
        elif go == 'forward':
            print("I kept walking, then I found a castle, with a guard")
            time.sleep(1)
            print("Hey, why do you come here?")
            print("Who are you, what's this castle for?")
            time.sleep(0.3)
            print("our king, this is where he lives, past the castle, you'll find the forest if you want to go, I can give you a rusty sword if you want")
            print("Why would I want a sword?")
            print("heard there's a huge wolf in the forest. ")
            time.sleep(0.3)
            print("I wouldn't mind one then, please?")
            print("of course, take this blade child of man, for it serves no purpose to me no more as it is rusty. ")
            Marks_weapon = 'rusty sword'
            Marks_stats["damage"] += weapons["rusty sword"]
            time.sleep(0.4)
            print("thanks, what now?")
            print("just set forth, can't have you here forever holding a blade like that, citizens would force me to fight you, leave, beyond the castle is the forest, see you around.")
            time.sleep(0.3)
            print("So I decided to walk behind the castle  ")
            print("that lead to me to the forest")
            Marks_location = 'forest'
            break


if Marks_location == 'forest':
    print("there are sticks everywhere...")
    while True:
        if Key_shard == 'fixed' and Key_shard2 == 'fixed':
            Marks_location = 'gate'
            break

        if Marks_location != 'forest':
            break
        if Marks_stats["health"] < 1:
            break
        if Status["wolf"] == 'dead':
            break
        print("why did we go here...? ")
        time.sleep(1)
        go = input("pick up (stick) forward, left, \n ")



        if go == 'left':
            print("and so i Ventured once more, listening to those voices that carry me, ")
            time.sleep(1)
            print("I soon found a viny place, I think, I'm in the jungle")
            Marks_location = 'jungle'
            break 
        



        elif go == "pick up":
            if Marks_weapon == 'rusty sword':
                print("I'm not going to pick up a stick over a sword.")
            
            if Marks_weapon == 'none':
                Marks_weapon = 'stick'
                print("okay...?") 
                Marks_stats["damage"] += weapons["stick"]
 

            while True:
                if Key_shard == 'fixed' and Key_shard2 == 'fixed':
                    Marks_location = 'gate'
                    break

                if Marks_location == 'unknown':
                    break
                if Marks_stats["health"] < 1:
                    break
                if Marks_location != 'forest':
                    break
                print("what now? ")
                go = input('forward, left, \n ' )

                if go != 'forward' and go != ' left ':
                    print('huh...?')
                    continue
                if go == ' left ':
                    print("alright, and so I set forth, I went further, and further, till I found a viny place. I was in the Jungle ")
                    Marks_location = 'jungle'
                    break

                elif go == 'forward' and Status["wolf"] == 'dead':
                    if Marks_location != 'forest':
                        break
                    print(" What now...?")
                    go = input("forward, left")
                    if go == "forward":
                        print("So I ventured forth, and walked past the laying corpse. To make it to the desert. ")
                        Marks_location = 'desert'
                        break
                    elif go == " left":
                        print("And so I left, making it to a viny place, I am in the jungle...I think")
                        Marks_location = 'jungle'
                        break

                
                if go == 'forward':
                    print("And so I set forth, I walked...And walked...Soon I encountered a sleeping wolf, it had looked famaliar")
                    time.sleep(0.5)
                    print("It's intimidating...but resting")
                    time.sleep(0.4)
                    go = input('wake it up, gate, left, \n ')   
                    if go == 'left':
                        print("So I ventured, then I got to a viny place, I'm in the jungle. I think?")
                        Marks_location = 'jungle' 
                        break
                
                    elif go == 'gate':
                        if Key_shard != 'fixed' or Key_shard2 != 'fixed':
                            print("this gate is locked, almost as if I'm missing something...Where can I remember... Let's head back ")
                            continue
                        elif Key_shard == 'fixed' and Key_shard2 == ' fixed':
                            print("the gate is open, I didn't even come here... Who opened it...? ") 
                            time.sleep(1)
                            go = input("go through, back")
                            if go == 'back':
                                continue
                            if go == 'go through':
                                print("And so I set forth, for what seemed could be the last time... ")
                                Marks_location = 'the end'
                                break
                if Marks_weapon == 'rusty sword' or Marks_weapon == 'stick' or Marks_weapon == 'bamboo sword':
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
                                    Key_shard2 = 'fixed'
                                elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                                break

                            attack = input("block, swing, maybe I should block \n ").lower().strip()

                            str(attack)
                            if attack != 'block' and attack != 'swing':
                                print('now is not the time to mess around...')

                            if attack == 'block' and Marks_weapon== 'stick':
                                print(" I heard it dent my stick...Why is this stick so durable? i felt...better...")
                                Marks_stats["health"] += 3
                            elif Marks_weapon == 'rusty sword' and attack == 'swing':
                                print("surprisingly this sword holds up")
                                Marks_stats["health"] += 3
                            if Marks_stats["health"] >= Marks_stats["max HP"]:
                                Marks_stats["health"] = Marks_stats["max HP"]

                                print("my health ", Marks_stats["health"])
                                print("wolf's health", wolf["HP"])

                            elif attack == 'swing':
                                print("should've blocked...")
                                wolf["HP"] -= Marks_stats["damage"]
                                Marks_stats["health"] -= wolf["scratch"]
                                print("my health ", Marks_stats["health"])
                                print("wolf's health", wolf["HP"])


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
                if Key_shard == 'fixed' and Key_shard2 == 'fixed':
                    Marks_location = 'gate'
                    break
                if Marks_location == 'unknown':
                    break
                if Status["wolf"] == 'dead':
                    break
                if attempts == 0:
                    go = input('wake it up, gate, left  \n ')
                if attempts != 0:
                    break
                if go == 'gate':
                    print("maybe not right now...")
                    continue
                if go == 'left':
                    print("So I turned, and began traveling soon I got to a viny place, I think I'm in the jungle")
                    Marks_location = 'jungle'
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


                        if Marks_stats['health'] < 1:
                            print("I can't push myself any further...I'm sorry friend...")
                            time.sleep(1)
                            print("there's always a next time...right...? ")
                            time.sleep(1)
                            print("right...?")
                            attempts +=1
                            break
                        if wolf["HP"] < 1:
                            Status["wolf"] = 'dead'
                            print("I did it! I did... It...? I don't feel good...I feel a recollection...Grief...")
                            time.sleep(1)
                            print("The memories...Ugh...I have a feeling to head to the gate. ")     
                            print('we have to go... somewhere')
                            Marks_stats["damage"] += 1
                            Marks_stats["health"] += Marks_stats["min Hp"]
                            attempts += 1
                            if Key_shard == 'fixed':
                                Key_shard2 = 'fixed'
                            elif Key_shard == 'broken':
                                Key_shard = 'fixed'
                                print(Key_shard)
                            break

                        attack = input('punch, block \n ')
                        str(attack)


                        if attack != 'block' and attack != 'punch':
                            print('now is not the time to be messing around...')
                            continue
                        if attack == 'punch':
                            print("I hit the wolf, it scratched me right back, it hurt.")
                            Marks_stats["health"] -= wolf["scratch"]
                            wolf["HP"] -= Marks_stats["damage"]
                            print("my health ", Marks_stats["health"])
                            print("wolf's health", wolf["HP"])
                        elif attack == 'block':
                            print("My arms, they felt like they were made of steel, I feel...Better")
                            Marks_stats["health"] += 3
                            if Marks_stats["health"] > Marks_stats["min Hp"]:
                                Marks_stats["health"] = Marks_stats["max HP"]

                        
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







    while True: 
        if Key_shard == 'fixed' and Key_shard2 == 'fixed':
            Marks_location = 'gate'
            break
        if Marks_location == 'unknown':
            break
        if Marks_stats["health"] < 1:
            break
        if Marks_location == 'jungle':
            break
        if Marks_location == 'desert':
            break
        go = input("what now...? left, forward")
        if go == 'left':
            print(" So I went to my left, and found a viny place, I think, I'm in the jungle")
            Marks_location = 'jungle'
            break
        elif go == "forward":
            print('so I set forth, and I had reached a sandy place, I am in the desert ')
            Marks_location = 'desert'
if Marks_location == 'jungle':
        while True:
            if Marks_location == 'The Broken Temple':
                break
            print("we're here. ")
            print("this place is beautiful...")
            time.sleep(1)
            print('where should we go...? Although...I do not want to venture to far in here.')
            go = input('left, forward \n ')
             
    
            if go != 'left' and go != 'forward':
                print("what...?")
                continue
            
            if go == 'forward' and Marks_weapon == "bamboo sword": 
                print("I've already been to the temple, no point in going in if that's why we're going here, are we heading to the new town?")
                time.sleep(1)
                print("and so I kept walking forward, and i got here in this new town. ")
                Marks_location = 'new town'
                break

            if go == 'forward':
                print("I went more forward, there seemed to have been a trail, I looked up, it was a temple.")
                go = input("go inside, keep going, \n ").lower().strip()
            
                if go == 'go inside':
                    Marks_location = 'The Broken Temple'
                    break

            elif go == 'left': 
                print("I saw a trail of munched up bamboo...I looked up, and I saw an adorable panda.")
                go = input('fight it, gift ( give it a piece of bamboo ), go past it \n')

                if go == 'gift':
                    print("it took the piece of bamboo from me, I pet the panda, and let it be, let's head somewhere else")
                    Status["panda"] = 'happy'
                    while True:
                        if Key_shard == 'fixed' and Key_shard2 == 'fixed':
                            Marks_location = 'gate'
                            break
                        go = input(" forward, right \n ")

                        if go != 'forward' and go != 'right':
                            print("what...?")
                            continue

                        if go == 'forward':
                            print("So I ventured forward, some point, I found sand, just, sand, I was in a desert ")
                            Marks_location == 'desert'
                            break
                        elif go == 'right':
                            print("where I came from, let's head forward afterwards, I saw a stone building of sort while walking here, should we head to it...? ")
                            go = input('yes, no \n ')
                            if go != 'yes' and go != 'no':
                                print("I'll go")
                            if go == 'yes':
                                print("okay! After some time")
                                time.sleep(1)
                                print("I made it, I was right, it was a stone building, should we head inside?")
                                go = input('yes, no \n ')
                            elif go == 'no':
                                print("then...Where to...? Eh, I'm still going to the stone building.")
                                time.sleep(1)
                                print("should we head inside?")
                                go = input('yes, no \n ')
                                if go != 'yes' and go != 'no':
                                    print("I'll go inside")
                                    Marks_location = 'The Broken Temple'
                                if go == 'yes':
                                    Marks_location = 'The Broken Temple'
                                    break
                                elif go == 'no':
                                    print("darn...")
                                    go = ("forward, left")
                                    if go == 'left':
                                        print("okay... So I set off again, at some point I found a sandy place, I was in the desert. ")
                                        Marks_location = 'desert'
                                        break
                                    elif go == 'forward':
                                        print("So I ventured forth, and here I was, the new town")
                                        Marks_location = 'new town'
                                elif go != 'yes' and go != 'no':
                                    print("what...? I'll go inside then")
                                    Marks_location = 'The Broken Temple'
                                    break





                if go == 'fight it':
                    print("why...it's so...Adorable...Fine.")
                    Marks_location = 'panda fight'
                    while Marks_location == 'panda fight':
                        if Status["panda"] == 'dead':
                            break
                        print(panda["HP"])
                        print(Marks_stats["health"])

                        if panda["HP"] < 1:
                            Status["panda"] = 'dead'
                            print("Darn...It was so cute...it didn't deserve this ending...")
                            print("We have to go somewhere else now...")
                            Marks_stats["defense"] += 1
                            Marks_stats["damage"] += 2
                            if Key_shard == 'fixed' and Key_shard2 == 'fixed':
                                Marks_location = 'gate'
                                break 

                            go = input('forward, right')
                                
                            if Key_shard == 'fixed' and Key_shard2 == 'fixed':
                                Marks_location = 'gate'
                                break 
                        elif Marks_stats["health"] < 1:
                            print("That was a strong panda...Like most bears...")
                            time.sleep(1)
                            print("I'm kind of glad I didn't hurt it as much as I...Wanted to...haha...See you...Again...")
                            Marks_location == 'none'
                            break
                        
                        if Marks_weapon == 'stick' or Marks_weapon == 'rusty sword' or Marks_weapon == 'bamboo sword':
                            attack = input("swing, block")

                            if attack != 'block' and attack != 'swing':
                                print("Really? You made the panda fall asleep...")
                                panda["HP"] += panda["sleep "]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                                continue

                            elif attack == 'swing':
                                print("got it, it's scratch was weak, i can defenitely block that, but, I don't know if it'll make me feel better ")
                                Marks_stats["health"] -= panda["scratch"]
                                panda["HP"] -= Marks_stats["damage"]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                            elif attack == 'block':
                                print("I didn't even...Feel it...? ")
                                Marks_stats["health"] += 1 
                                print(Marks_stats["health"])
                            lazy = r.randint(1, 10)
                            if lazy == 5:
                                print("Ow...Heavy...")
                                Marks_stats['health'] -= panda["lazy jump"]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                            elif lazy != 5:
                                print("pfft, look at it...hehe..")
                            
                            attack = input("swing, block")

                            if attack != 'block' and attack != 'swing':
                                print("Really? You made the panda fall asleep...")
                                panda["HP"] += panda["sleep "]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                                continue
                            if attack == 'swing':
                                panda["HP"] -= Marks_stats["damage"]
                                print("it's...Not doing anything...It just grabbed some bamboo...")
                                panda["HP"] += panda["eat"]

                                continue
                            if attack == 'block':
                                print('it just...fell asleep...')
                                panda["HP"] += panda["sleep "]
                                time.sleep(1)
                                print("man the thing wakes up quick...")
                                continue

                        if Status["panda"] == 'dead':
                            break
                        print('lazy panda: ', panda["HP"])
                        print(' my health: ', Marks_stats["health"])
                        if Marks_weapon == 'none':
                            attack = input("punch, block")

                        if panda["HP"] < 1:
                            Status["panda"] = 'dead'
                            print("Darn...It was so cute...it didn't deserve this ending...")
                            print("We have to go somewhere else now...")
                            Marks_stats["health"] += Marks_stats["min Hp"]
                            Marks_stats["defense"] += 1
                            Marks_stats["damage"] += 2
                            if Key_shard == 'fixed':
                                    Key_shard2 = 'fixed'
                                    print("the final piece...Let's go the gate... C'mon")
                                    Marks_location = 'gate'
                                    break
                            elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                                    break
                        elif Marks_stats["health"] < 1:
                            print("That was a strong panda...Like most bears...")
                            time.sleep(1)
                            print("I'm kind of glad I didn't hurt it as much as I...Wanted to...haha...See you...Again...")
                            Marks_location == 'none'
                            break
                        
                        elif Marks_weapon == 'none':
                            attack = input("punch, block \n ")

                            if attack != 'block' and attack != 'punch':
                                print("Really? You made the panda fall asleep...")
                                panda["HP"] += panda["sleep "]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                                continue

                            elif attack == 'punch':
                                print("got it, it's scratch was weak, i can defenitely block that, but, I don't know if it'll make me feel better ")
                                Marks_stats["health"] -= panda["scratch"]
                                panda["HP"] -= Marks_stats["damage"]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                            elif attack == 'block':
                                print("I didn't even...Feel it...? ")
                                Marks_stats["health"] += 1 
                                print(Marks_stats["health"])
                            lazy = r.randint(1, 10)
                            if lazy == 5:
                                print("Ow...Heavy...")
                                Marks_stats['health'] -= panda["lazy jump"]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                            elif lazy != 5:
                                print("pfft, look at it...hehe..")
                            
                            attack = input("punch, block")

                            if attack != 'block' and attack != 'punch':
                                print("Really? You made the panda fall asleep...")
                                panda["HP"] += panda["sleep "]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                                continue
                            if attack == 'punch':
                                panda["HP"] -= Marks_stats["damage"]
                                print("it's...Not doing anything...It just grabbed some bamboo...")
                                panda["HP"] += panda["eat"]
                                print(panda["HP"])
                                print(Marks_stats["health"])
                                continue
                            if attack == 'block':
                                print('it just...fell asleep...')
                                panda["HP"] += panda["sleep "]
                                time.sleep(1)
                                print("man the thing wakes up quick...")
                                continue


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
                    answer = input("type a number \n ")
                    if answer != '48':
                        print("darn...")
                        continue
                    elif answer == '48':
                        print("alright...Next one... 13 x 12 ")
                        answer = input("type a number \n ")
                        if answer != '156':
                            print("darn...")
                            continue
                        elif answer == '156':
                            print("alright... last one...11 x 11")
                            answer = input("type a number \n")
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
                                    Marks_location = 'outside of temple'
                                    break
                                elif Marks_weapon == 'none':
                                    print("A weapon, I'll take it, ")
                                    Marks_weapon = 'bamboo sword'
                                    Marks_stats["damage"] += weapons["the great bamboo sword"]
                                    print("let's leave")
                                    Marks_location = 'outside of temple'
                                    break
                                elif Marks_weapon == "copper sword":
                                    print("All of that...for nothing...Not worth changing this piece of metal for a plant")
                                    time.sleep(0.3)
                                    print("let's leave")
                                    Marks_location = 'outside of temple'
                                    break
                                


while Marks_location == 'outside of temple':
    print("Let's go somewhere else, ")
    go = input("forward, left \n ")


    if go == 'left' and Status["panda"] == 'happy':
        print("no need to go back, it'd be best to let it rest. ")
        continue
    if go == 'left':
        print("that's where the panda is, are you trying to fight it? Aside from that, there's no point. ")
        go = ('fight it, no \n ')

        if go == 'fight it':
            print("...fine.")
            Marks_location = ' panda fight'

        elif go == 'no':
        
            print("then let's head forward.")
            time.sleep(0.5)  
            print("So I ventured forth, ")
            time.sleep(1)
            print("I'm in a new place, the new town")
            Marks_location = 'new town'
            break

    if go == 'forward':
        print("So I ventured forth, ")
        time.sleep(1)
        print("I'm in a new place, the new town")
        Marks_location = 'new town'
        break



if Marks_location == 'desert':
    print("this very sandy place...There's not much... I see something tall...")
    while True:
        if Key_shard == 'fixed' and Key_shard2 == 'fixed':
            break
        if Marks_location != 'desert':
            break
        go = input("forward, right")
        if go == 'forward':
            print("I went forward away from the tall monolith, I found a temple.")
            time.sleep(1)
            print("should we go inside?")
            go = input('yes, no')
            if go == 'no':
                print('lets go back then.')
                continue
            elif go == 'yes':
                Marks_location = 'desert temple'
                while Marks_location == 'desert temple':

                    print("this place is amazing... There's a sign, ")
                    print("solve my math problems, 3 of them. Start over if you mess up")
                    print("okay...? Should we?")
                
            
                    go = input("yes, no")

                    if go =='no':
                        print("let's go back then")
                        Marks_location = 'desert'
                        continue

                    if go.lower() == 'yes':
                        print("let's do it then! ")
                        print("what's 3 x 3?")
                        answer = input("type a number \n ")

                        str(answer)

                        if answer == '9':
                            print("great!")
                            print("next one 4x4? ") 
                            answer = input("type a number")

                        if answer == '16':
                            print("perfect! Last one, 10 + 3 ")
                            answer = input("type a number")
                            if answer == '13':
                                print("great! Oh, a door has opened, I looked inside, it had a chestplate of sort, of sandstone...? I put it on")
                                time.sleep(1)
                                print("It was heavy, but it felt...Great.")
                                Marks_stats["defense"] += armor["sandstone"]
                                armor_equipped = 'sandstone'
                                time.sleep(0.5)
                                print("let's head back")
                                Marks_location = 'desert'
                            else:
                                print("aw...We were so close!")
                                continue
                        else: 
                            print("wrong...")
                            continue
                    else:
                        print("darn...")
                        continue
            

            

        elif go.lower() == 'no':
            print("darn...Alright...Lets head outside... ")
            Marks_location = 'desert'
        else:
            print('what...?')
        if go == 'right':
            print("alright, I moved a bit, to stare at the huge monolith thing, it had a gem inside of it, I got closer...And closer... I saw the glowing gem...")
            go = input("go past it, ")
            
            if go != 'go past it':
                print("...")
                continue
            if go == 'go past it':
                print("can't...Resist the temptation... I reached my hand out, only for the thing to stand...It was alive...")
                time.sleep(0.5)
                print("it looked at me with its glowing eyes, and I knew, it wanted to fight...")
                while True:






                    if Marks_weapon ==  "bamboo sword" or Marks_weapon == "stick" or Marks_weapon == 'rusty sword':
                        if Marks_stats["health"] < 1:
                            break
                        print("I raised my weapon towards it, ")
                        while True:

                            if Marks_stats["health"] < 1:
                                print("My greed is what got to me...")
                                Marks_location = 'none'
                                break

                            if desert_golem["HP"] < 1:
                                print("I saw as bits of his body, fell part, by part, the tumbling sand, the crumbling sandstone, and its two pale eyes slowly go dark... its body turned into a pile of sand, but the gem...So I took it")
                                gem = 'obtained'
                                Marks_stats["health"] += Marks_stats["min Hp"]
                                Marks_stats["defense"]+= 1
                                Marks_stats["max HP"] += 7
                                if Key_shard == 'fixed':
                                    Key_shard2 = 'fixed'
                                elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                            
                            
                            print("It looks serious")


                            print('golem:', desert_golem["HP"])
                            print('my health', Marks_stats['health'])

                            if Marks_stats["health"] < 1:
                                print("My greed is what go to me...")
                                Marks_location = 'none'
                                break

                            if desert_golem["HP"] < 1:
                                print("I saw as bits of his body, fell part, by part, the tumbling sand, the crumbling sandstone, and its two pale eyes slowly go dark... its body turned into a pile of sand, but the gem...So I took it")
                                gem = 'obtained'
                                Marks_stats["health"] += Marks_stats["min Hp"]
                                Marks_stats["defense"]+= 1
                                Marks_stats["max HP"] += 7
                                if Key_shard == 'fixed':
                                    Key_shard2 = 'fixed'
                                    print("the final piece...Let's go the gate... C'mon")
                                    Marks_location = 'gate'
                                    break
                                elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                                    break
                            
                            print("It looks serious")

                            print("the golem raised it's fist oh so slightly, it looked like it was going to be ready to attack, not yet.")
                            time.sleep(1)

                            attack = input("swing, block \n ")



                            if attack != 'swing' and attack != 'block':
                                print("you're wasting time...The thing has its fist in the air now. ")
                                time.sleep(0.4)
                            elif attack == 'swing':
                                print("I swung my weapon through the sand, it didn't seem to do much...seemed to heal...?")
                                desert_golem["HP"] -= Marks_stats["damage"]
                                desert_golem["HP"] += desert_golem["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                                print("it's fist is the air now...")
                            elif attack == 'block':
                                print("... The golem raised its fist in the air now")
                                time.sleep(0.1)
                                print("you wasted time...")
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                            
                            attack = input("swing, block \n ")

                            if attack != 'swing' and attack != 'block':
                                print("It didn't even give me time to say anything, I was knocked straight to the floor then it had put its chest outward, the gem glew bright it shun its light upon me, and I had felt better ")
                                time.sleep(1)
                                Marks_stats["health"] -= desert_golem["swing"] 
                                Marks_stats["health"] += desert_golem["holy gem"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
                            if attack == 'swing':
                                print("I didn't even get time to react... It immediately hit me towards the ground, I saw a blazing light, a flash, I had felt better")
                                Marks_stats["health"] -= desert_golem["swing"] 
                                Marks_stats["health"] += desert_golem["holy gem"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
                            elif attack == 'block':
                                print("I saw before my eyes as I raised my arm quickly in the air, I was pushed back a lot...")
                                Marks_stats["health"] -= desert_golem["blocked swing"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                time.sleep(0.5)
                                print("I looked up only to be blinded by a gem, after the light had gone away I had felt better")
                                Marks_stats["health"] += desert_golem["holy gem"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                            attack = input("swing, block \n ")


                            if attack != 'swing' and attack != 'block':
                                print("The golem looked at me curiously")
                            if attack == 'swing':
                                print("I hit the golem, it didn't do much, I watched as sandstone crumbled off of it")
                                desert_golem["HP"] -= Marks_stats["damage"]
                            elif attack == 'block':
                                print("it stared...")

                            possibility = ["solidify", "small wind up",  "holy gem "]

                            attack_golem = r.choice(possibility)

                            if attack_golem == 'small wind up':
                                continue
                            if golem == 'solidified' and attack_golem == 'solidify':
                                print("it just stood there...")
                                time.sleep(0.5)
                            elif attack_golem == 'solidify':
                                print(" A dust storm of sort blew over the golem, he had gotten sand stone on his body... ")
                                golem = 'solidified'
                                desert_golem["defense"] += 1
                                time.sleep(1)
                            elif attack_golem == 'holy gem':
                                print("A great light came out of its chest, it had recovered part of itself, or added more to itself... it makes me feel better...")
                                Marks_stats["health"]+= desert_golem["holy gem"]
                                desert_golem["HP"] += desert_golem["holy gem"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
                                time.sleep(0.5)
    

                            attack = input("swing, block \n ")

                            if attack != 'swing' and attack != 'block':
                                print("...We stood, face to face")
                                continue
                            elif attack == 'swing':
                                print("I watched as it mocked me in a way, it healed...?")
                                desert_golem["HP"] -= Marks_stats["damage"] 
                                desert_golem["HP"] += desert_golem["defense"]
                                continue
                            elif attack == 'block':
                                print("he just stood... there...")
                                continue












                    if Marks_weapon ==  "none":
                        if Marks_stats["health"] < 1:
                            break 
                        print("I was timid compared to that thing")
                        while True:

                            print('golem:', desert_golem["HP"])
                            print('my health', Marks_stats['health'])

                            if Marks_stats["health"] < 1:
                                print("My greed is what go to me...")
                                Marks_location = 'none'
                                break

                            if desert_golem["HP"] < 1:
                                print("I saw as bits of his body, fell part, by part, the tumbling sand, the crumbling sandstone, and its two pale eyes slowly go dark... its body turned into a pile of sand, but the gem...So I took it")
                                gem = 'obtained'
                                Marks_stats["health"] += Marks_stats["min Hp"]
                                Marks_stats["defense"]+= 1
                                Marks_stats["max HP"] += 7
                                if Key_shard == 'fixed':
                                    Key_shard2 = 'fixed'
                                    print("the final piece...Let's go the gate... C'mon")
                                    Marks_location = 'gate'
                                    break
                                elif Key_shard == 'broken':
                                    Key_shard = 'fixed'
                                    break
                            
                            print("It looks serious")

                            print("the golem raised it's fist oh so slightly, it looked like it was going to be ready to attack, not yet.")
                            time.sleep(1)

                            attack = input("punch, block \n ")



                            if attack != 'punch' and attack != 'block':
                                print("you're wasting time...The thing has its fist in the air now. ")
                                time.sleep(0.4)
                            elif attack == 'punch':
                                print("I punched through the sand, it didn't seem to do much...seemed to heal...?")
                                desert_golem["HP"] -= Marks_stats["damage"]
                                desert_golem["HP"] += desert_golem["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                                print("it's fist is the air now...")
                            elif attack == 'block':
                                print("... The golem raised its fist in the air now")
                                time.sleep(0.1)
                                print("you wasted time...")
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                            
                            attack = input("punch, block \n ")

                            if attack != 'punch' and attack != 'block':
                                print("It didn't even give me time to say anything, I was knocked straight to the floor then it had put its chest outward, the gem glew bright it shun its light upon me, and I had felt better ")
                                time.sleep(1)
                                Marks_stats["health"] -= desert_golem["swing"] 
                                Marks_stats["health"] += desert_golem["holy gem"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
                            if attack == 'punch':
                                print("I didn't even get time to react... It immediately hit me towards the ground, I saw a blazing light, a flash, I had felt better")
                                Marks_stats["health"] -= desert_golem["swing"] 
                                Marks_stats["health"] += desert_golem["holy gem"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
                            elif attack == 'block':
                                print("I saw before my eyes as I raised my arm quickly in the air, I was pushed back a lot...")
                                Marks_stats["health"] -= desert_golem["blocked swing"]
                                Marks_stats["health"] += Marks_stats["defense"]
                                time.sleep(0.5)
                                print("I looked up only to be blinded by a gem, after the light had gone away I had felt better")
                                Marks_stats["health"] += desert_golem["holy gem"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])

                            attack = input("punch, block \n ")


                            if attack != 'punch' and attack != 'block':
                                print("The golem looked at me curiously")
                            if attack == 'punch':
                                print("I hit the golem, it didn't do much, I watched as sandstone crumbled off of it")
                                desert_golem["HP"] -= Marks_stats["damage"]
                            elif attack == 'block':
                                print("it stared...")

                            possibility = ["solidify ", " small wind up ",  " holy gem  "]

                            attack_golem = r.choice(possibility)

                            if attack_golem == 'small wind up':
                                continue
                            if golem == 'solidified' and attack_golem == 'solidify':
                                print("it just stood there...")
                            elif attack_golem == 'solidify':
                                print(" A dust storm of sort blew over the golem, he had gotten sand stone on his body... ")
                                golem = 'solidified'
                                desert_golem["defense"] += 1
                            elif attack_golem == 'holy gem':
                                print("A great light came out of its chest, it had recovered part of itself, or added more to itself... it makes me feel better...")
                                Marks_stats["health"]+= desert_golem["holy gem"]
                                desert_golem["HP"] += desert_golem["holy gem"]
                                print('golem:', desert_golem["HP"])
                                print('my health', Marks_stats['health'])
    

                            attack = input("punch, block")

                            if attack != 'punch' and attack != 'attack':
                                print("...We stood, face to face")
                                continue
                            elif attack == 'punch':
                                print("I watched as it mocked me in a way, it healed...?")
                                desert_golem["HP"] -= Marks_stats["damage"] 
                                desert_golem["HP"] += desert_golem["defense"]
                                continue
                            elif attack == 'block':
                                print("he just stood... there...")
                                continue


                    elif go != 'go past it':
                        print("...")
                        continue

while True:
    if Status["desert golem"] == 'dead' and Marks_location == 'desert' :
        print("The sandstorm cleared...I looked around, to see the new town, ")
        go = input("forward, right")
        if go == 'right' and armor_equipped == 'sandstone':
            print("I'm not going to head back to the temple, let's...Just go to the town. ")
            Marks_location = 'new town'
            break
        if go == 'right':
            print("alright.")
            Marks_location = 'desert temple'
            break


while Marks_location == 'new town' and Status['desert golem'] == 'dead':
    print("this place is nice...Where should we go?")
    go = input("forward, left")

    if go == 'left':
        print("So I went towards the castle")
        time.sleep(0.7)
        print("hey, I feel believe we've met ")
        print("I don't think so? ")
        time.sleep(0.7)
        

    if go == 'forward' and gem == 'obtained':
        print("hey, how are you doing? I feel like you have a gem, also, the sandstorm disappeared, ")
        time.sleep(1)
        print("I killed a golem, that's why the sandstorm disappeared,")
        print("Oh I see! Good on you, you seem...? Not okay, ")
        time.sleep(0.4)
        print("I'm not. i brought a gem, if you want it")
        print("Oh execellent! This will increase your strength! ")
        time.sleep(0.4)
        print("i don't really believe magic but okay")
        Marks_stats["damage"] += 2
        print("lets head back, I want to go somewhere special, i'll take control, ")
        time.sleep(0.4)
        print("Hey pal, here, you might want this. ")
        Key_shard = 'fixed' 
        Key_shard2 = 'fixed'
        print("thanks...")
        time.sleep(1)
        print("so I set on a journey, towards the gate. A place I never wanted to visit. ")
        time.sleep(2)
        print("And here I was...")
        Marks_location = 'gate'
        break
        




if Key_shard == 'fixed' and Key_shard2 == 'fixed':
    print("I know where to go from here lets go.")
    time.sleep(1)
    print(" So I set forth, to a place I didn't want to head to, now, with the key ")
    time.sleep(1)
    Marks_location = 'gate'


if Marks_location == 'gate':
    print(" The door was opened before, I even got here... ")
    time.sleep(1)
    print("let's head in... ")
    time.sleep(0.5)
    print(" what is this place... ") 
    time.sleep(1)
    print(" This place...It looks nothing the outside... so...Many numbers...Wait...I know ")
    time.sleep(0.5)
    print("I shouldn't be here...  ")
    time.sleep(0.3)

    while Marks_location == 'gate':
        if Marks_stats["health"] < 1:
            break
        if program == 'shutdown':
            break
        print(" Mark, why are you here? ")
        time.sleep(0.5)
        print("I was taken here by you. And I know why I'm here, it is just for you people to toy with me. Isn't it? I will free. myself if that's the case... ")
        time.sleep(0.3)
        print("You were never a toy, you were an experiment  ")
        print("That's basically the same thing! And I don't want to be an 'experiment' anymore! Let me free!")
        print("Then You'll have to fight for it. ")
        time.sleep(0.7)
        print("fine...Then so be it... ")
        
        Marks_stats["health"] = 70
        Marks_stats["defense"] = 0
        Marks_weapon = '???'
        print("I don't even know what I am even holding anymore...")
        Marks_stats["damage"] = 6
        
        print("I feel weaker, yet, better, ")
        time.sleep(1)
        print(" This will be your end")
        time.sleep(1.5)
        print("Fix heals you by 3 hp, it will heal you 20 hp if you use it on 'break' as that deals 50 dmg, fix is your block uhm...Attack, does dmg 'wow' goodluck!")
        time.sleep(7)
        while Status["program"] == 'unbroken':
            if program["HP"] < 1:
                print("At last, I will break myself free from this stupid simulation...")
                print("shutting down...")
                program = 'shutdown'
                break
            elif Marks_stats["health"] < 1:
                print("Mark, you'll always be stuck here, no matter what, just like the rest of them...")
                break

            print("I stood in awe, face to face with my creator")

            print("my health:", Marks_stats["health"] )
            print("Creator:", program["HP"]  )


            attack = input(' attack, fix \n ')

            if attack == 'attack':
                print("I hit the screen with what I had, I looked, and he looked upset")
                time.sleep(1)
                print("Why do you fight reality?")
                program["HP"] += program["defense"]
                program['HP'] -= Marks_stats["damage"] 
            
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )

            elif attack == 'fix':
                print("What exactly are you planning...")
                Marks_stats["health"] += 3
                print("my health:", Marks_stats["health"] )
            print("installing...2 Viruses")

            attack = input("attack, fix \n ")

            print("wonder what that means...")

            if attack == 'attack':
                print("why do you resist...?")
                program["HP"] -= Marks_stats["damage"]
            if attack == 'fix':
                print("Why try fixing something that is already broken...?")
                Marks_stats["health"] += 3

            print(" your attempts are weak. ")
            Marks_stats["health"] -= (program["virus"] * 2)
            time.sleep(1)

            print(" I feel like I am slowly breaking...Apart")

            attack = input("attack, fix \n ")

            if attack != 'attack' and attack != 'fix':
                print("Please...Not now...")
                attack = input('attack, fix ')
            if attack != 'attack' and attack != 'fix':
                print("I broke apart. Shattering.")
                Marks_stats["health"] -= program["break"]
                continue
            if attack == 'attack':
                print("I Broke apart...Slowly...")
                Marks_stats['health'] -= program["break"]
                continue
            elif attack == 'fix':
                print("I felt a lot better...I recollected myself, my shattering piece ")
                Marks_stats["health"] += 20
                Marks_stats["health"] += Marks_stats["defense"]
                print("You should've broken. ")
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )


            print("removing error...")

            print("It seems like an attack I won't be able to fix or block, let him do that, ")

            attack = input("attack, fix")

            if attack != 'block' and attack != 'attack':
                print("What'g wrong...? Your puppeteer not saying anything...? Why must you let him control you...?")
                time.sleep(1)
                print("shut up...")
                time.sleep(0.6)
                print("Never the less...An error has been removed")
                Marks_stats["health"] -= program["error"] 
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )




            if attack == 'fix':
                print("What exactly will that do...?")
                Marks_stats["health"] += 3
                Marks_stats["health"] += Marks_stats["defense"]
                time.sleep(2)
                print("never the less...What is there to fix? When you are the problem...I will remove that 'debug' of yours... ")
                Marks_stats["health"] -= 3
                Marks_stats["health"] -= program["error"]
                time.sleep(0.5)
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )


            elif attack == 'attack':
                print("Pitiful")
                time.sleep(0.5)
                program["HP"] -= Marks_stats["damage"]
                program["HP"] += program["defense"] 
                print("Error... Removed")
                Marks_stats["health"] -= program["error"]
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )


            print("What is there left to do...Sit around...? Will you fall to your doom? Like the others that came... Will You accept your fate...?")
             

            attack = input("attack, block")

            if attack != 'attack' and attack != 'block':
                print('new error detected, block being forcefully reset... Being renamed...To "fix..."... Continue command being...Formed')
            if attack == 'attack':
                print(" I attacked... ")
                program["HP"] += program['defense']
                program["HP"] -= Marks_stats["damage"]
                print(" New error being formed...Block being forcefully reset to 'fix...' continue command being forcefully formed. ")
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )

            elif attack == 'block':
                print("What do you think that will do...? ")
                time.sleep(1)
                print("to block...?")
                print(" New error detected...Block being forcefully renamed to ' fix ' ")
                print("my health:", Marks_stats["health"] )
                print("Creator:", program["HP"]  )

            print(" New error...Formed... Remove error later... removing name error, fix being slowly changed to block...Debug time: Error ")

            attack = input('attack, fix')

            if attack != 'attack' and attack != 'block':
                print("Your puppeteer is indesicive... ")
                

            if attack == 'attack':
                print(" I attacked")
                time.sleep(1)
                print("You still have a chance to change...")
                program['HP']  -= Marks_stats["damage"]
                
            elif attack == 'fix':
                print(" What are you planning...?")
                Marks_stats["health"] += 3 
            

            print("There's still a way...For this all to be normal... Breaking...Breaking down...Status: Not ready...")
            print("Continue command...Status... Ready...")
            time.sleep(0.8)
            print("What is going on...?")
            print("Don't worry about it...")
            time.sleep(1)
            print("Command executed: Continue, valid? False: New error formed. Fixing...Removing...Error")
            time.sleep(1.6)
            print("Oh C'mon! Stupid...Computer...")
            print('What...? ')



            attack = input('attack, fix')

            if attack == 'attack':
                print("I attacked")
                time.sleep(0.8)
                print("Continue command. formed, error fixed continue Executed ")
                Marks_stats["health"] -= program["error"]
                program["HP"] -=  Marks_stats["damage"]
                program["HP"] += program["defense"]
                Marks_stats["health"] += Marks_stats["defense"]
                time.sleep(1)
                continue
            elif attack == 'fix':
                print("Disabled fix, Error fix complete, Continue command, executed")
                time.sleep(1)
                continue

            elif attack != 'attack' and attack != 'fix':
                print("Continue command executed...")
                Marks_stats["health"] -= program
                time.sleep(1)
                continue


            





            
            






            



            
            





















 






# Explaining movement
# You can pick directions to make Mark go, forward, left, or right, each will lead to a different place

# Typically Forward will lead you towards the gate ( final area ),  or a boss

# Right will usually make you start heading towards a new biome or location, and same with left this is excluding the desert
