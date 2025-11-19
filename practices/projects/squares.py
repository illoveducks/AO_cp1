# Ao 1st squared numbers

# List of numbers
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]


# Print numbers up here maybe to naje ut easuer 

# Where I will set up my map, setting the squared

# setting my squared
def square(num):
    # return
    return num**2

# Setting up two maps
squared_nums = list(map(lambda num: num**2, numbers ))
print(squared_nums)

numbers = list(map(lambda num: num+0, numbers))

# make it one loop to be able to combine them
for num in squared_nums:
    print("squared: ", num)

for num in numbers:
    print("original", num)



 