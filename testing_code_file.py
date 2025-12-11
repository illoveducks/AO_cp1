# test

import random as r

weapon_damage = {"stick":3,
                 "copper sword":8,
                 "wolf's claw": 7}
damage = 5

hi = { 'lazy': r.randint(1, 10) }

print(hi['lazy'])

damage += weapon_damage["stick"]

print(damage)

while True:
    possibility = ["hi", "hello","11"]

    print(r.choice(possibility))