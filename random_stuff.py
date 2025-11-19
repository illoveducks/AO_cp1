# HIII!

numbers = [56, 55, 68, 64, 1000, 100, 300, 42, 32, 5, 6, 8, 9]





def divide(num):
    return num/3


new_nums = map(lambda num: num/3 , numbers)
print(new_nums)
for num in new_nums:
    print(" divided: ",num)