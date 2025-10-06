import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You only have 10 attempts!")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            attempts += 1
            print("Too high! Try again.")
        elif guess < number_to_guess:1
        print("Too low! Try again.")  
        attempts += 1
        
        continue
start_game()

# run-time error, the variable, " guess " wasn't labeled as a int or float which cause it to break while running

# logic error, you have an unlimited attempts in this game, fixed it by added so that it added an attempt everytime you put an input

#   run-time error, if there is an input that is not said, like if the input is not an integer it breaks, I fixed that ny adding an if statement

# There isn't really a need for the print statement at the bottom, as sometimes it doesn't print, it's a logic error