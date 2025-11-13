import turtle as t  # importing turtle
import random 

#Save the file as maze_generator.py
# Include your 1st line comment with initials, class period, and assignment name
#Import the turtle library at the beginning
#Set up the screen with appropriate dimensions and a background color
#Use nested loops to iterate through a grid system for maze creation
#Implement conditionals to determine wall placement
#Ensure that the maze has at least one valid path from start to finish
#Use functions to organize code, e.g., one for setup, one for drawing walls, and one for generating the maze layout
#Make sure the maze generation logic is correctly implemented
#Test the program to ensure it consistently generates valid, solvable mazes
#Clearly mark the start and end points of the maze
#Commit and push your code to Github

# setting up my screen how tall and wide it is.
screen = t.Screen()
screen.setup(1100, 1100)

# assign rows and columns
row_count = 6
column_count = 6

# a list for empty walls
horizontal_walls = [[0, 1, 1, 1, 1, 1], 
                    [0, 0, 0, 0, 0, 0], 
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0]]

# a list for empty walls
vertical_walls = [[1, 0, 0, 1, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1], 
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1], 
                  [1, 0, 0, 0, 0, 0, 1]]




#print the maze
t.speed(15)
t.teleport(-450,-450)
t.left(90)
t.forward(900)
t.teleport(-450, 500)
t.right(90)
t.forward(900)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(900)
t.teleport(-450, -450)
t.right(180)
t.forward(90)
t.penup()
t.forward(270)
t.pendown()
t.forward(90)
t.penup()
t.forward(270)
t.pendown()
t.forward(180)
t.teleport(-450, -300)


# Build walls, 
# then build vertical walls, 
# how to randomize them, no clue

    


t.done()
