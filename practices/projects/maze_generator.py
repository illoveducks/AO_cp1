
import turtle as t # importing turtle
import random as r

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
rows = 9
columns = 9

# a list for empty walls 
ro = []
col = []

# a for thing
for i in range(rows + 1):
# making another list for rows
    row = []
    # another loop for columns
    for co in range(columns):
        ro.append(True)
    ro.append(row)


# another list but for columns
for c in range(columns + 1 ):
    colu = []
    for c








