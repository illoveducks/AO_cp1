# Ao 1st squared numbers

# List of numbers which are floats now
numbers = [3.0, 7.0, 12.0, 25.0, 30.0, 45.0, 50.0, 65.0, 70.0, 85.0, 90.0, 105.0, 110.0, 125.0, 130.0, 145.0, 150.0, 165.0, 170.0, 185.0, 190.0, 205.0, 210.0, 225.0, 230.0, 245.0, 250.0, 265.0, 270.0, 285.0]


# Print numbers up here maybe to naje ut easuer 

# Where I will set up my map, setting the squared

# setting my squared
def square(num):
    # return
    return num**2

# Setting up two maps
squared_nums = list(map(lambda num: num**2, numbers ))

# lambda used to help with certain equations
numbers = list(map(lambda num: num+0, numbers))




# make it one loop to be able to combine them
#for num in squared_nums: 
   # print("squared: ", num)


#for num2 in numbers:
#    print("original", num)


# bit of a work around but here's my table, I combined them.
for i in squared_nums:
        # Does square root to reverse operation to get me the original
        original = i **0.5
        # puts it all together!
        print("original", original, "squared:", i)

# Had to convert them to floats so that it worked

       


    








