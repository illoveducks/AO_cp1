import turtle as t 

def draw_branch(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            draw_branch(length / 3)
            t.backward(length)
            t.right(60)
    
t.shape("turtle")
t.speed("5")
t.color("light blue")
t.penup()
