# AO 1st hi!
import random as r
import turtle as t

quickness = [1,2,3,4,5,6,7,8,9,10]


screen = t.Screen()
screen.setup(2000, 500)




t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()

t2.color("red")
t2.shape("turtle")
t3.color("purple")
t3.shape("turtle")
t4.color("orange")
t4.shape("turtle")
t5.color("pink")
t5.shape("turtle")
t6.color("gray")
t6.shape("turtle")

t.goto(0,0)
t2.goto(0,0)
t.pendown()
t2.pendown()


t6.teleport(2150, 60)



t.shape("turtle")

t.fillcolor("blue")

t.speed(r.choice(quickness))

t.teleport(0, 20)


t.forward(1000)

t2.color("red")

t2.shape("turtle")

t2.speed(r.choice(quickness))

t2.teleport(0, 40)

t2.forward(1000)

t3.speed(r.choice(quickness))


t3.forward(1000)

t4.teleport(0,-20)

t4.speed(r.choice(quickness))

t4.forward(1000)


t5.teleport(0,-40)

t5.speed(r.choice(quickness))

t5.forward(1000)



t.done()


