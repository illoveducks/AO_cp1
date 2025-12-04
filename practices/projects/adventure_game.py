# AO 1st Adventure game! 

import random 

import time

Marks_stats = { "damage": 5,
               "health": 20,
               "defense": 0, }

Status = { "wolf": "alive",
            "royal guard": 'alive',
            "panda": ' alive',
            "desert golem": 'alive?',
            "program": 'unbroken'}

weapons = {
    "stick": 3,
    "copper sword": 5,
    "the great bamboo sword": 7

}

armor = {'sandstone': 2,
         'iron': 4,
         'the royal shield': 5}


Marks_location = "home"

print("I woke up, I wonder, I wonder what's going on in town today. I need to get ready")

time.sleep(1)

print("I made breakfast, something is wrong, I feel it, I looked outside, to see a world ' shattered ', why?")

time.sleep(1)

print("After finishing breakfast, I got up, should we head outside?")

while True:
    
    outside = input("yes, no\n").strip()

    str(outside)
    if outside != 'yes' or outside != 'no':
        print("what...?")


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
            break
while True:
    go = input("where should I go? \n left leads me to the forest, \n right leads me to the desert, \n forward leads me to the new town, \n or back home... ( type back by the way ) ").strip()

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
    while True:
        print("there are sticks everywhere...")
        print("why did we go here again...? What's your goal...? ")
        go = ("pick up a stick, forward, left, right, ")





# Explaining movement
# You can pick directions to make Mark go, forward, left, or right, each will lead to a different place

# Typically Forward will lead you towards the gate ( final area ),  or a boss

# Right will usually make you start heading towards a new biome or location, and same with left this is excluding the desert
