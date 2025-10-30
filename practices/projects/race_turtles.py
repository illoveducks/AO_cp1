# AO 1st hi!
import random as r
import turtle as t

quickness = [1,2,3,4,5,6,7,8,9,10]


screen = t.Screen()
screen.setup(2000, 500)

#finish line is at 190
finish_line = 190
#turtle is assined
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()

turtles = [t1,t2,t3,t4,t5]
#what each turtle color is
t1.color("blue")
t2.color("red")
t3.color("purple")
t4.color("orange")
t5.color("pink")
t6.color("gray")

#turtles are turtles
t1.shape("turtle")
t2.shape("turtle")

t3.shape("turtle")
t4.shape("turtle")



t6.shape("turtle")

steps = [7,8,9,10,11,12,13,14,15,16]

t1.teleport(-100,20)
t2.teleport(-100,40)
t3.teleport(-100,-20)
t4.teleport(-100,-40)
t5.teleport(-100 )
t6.teleport(900, 250)

t6.right(90)
t6.forward(490)
t6.left(180)
race = True # showing what's true
while race:
    if t.xcor() >= finish_line:
        race = False
        print(f"the won")
        break

# makes a choice of steps for all the turtles.
    t1.speed(r.choice(quickness))

   


    t1.forward(r.choice(steps))


    t2.speed(r.choice(quickness))

    t2.forward(r.choice(steps))

    t3.speed(r.choice(quickness))

    t3.forward(r.choice(steps))


    t4.speed(r.choice(quickness))

    t4.forward(r.choice(steps))


    t5.speed(r.choice(quickness))

    t5.forward(r.choice(steps))\
    
    continue
    


