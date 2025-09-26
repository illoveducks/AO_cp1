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
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        else:
            print("that's not a number!")
        continue
    print("Game Over. Thanks for playing!")

start_game()



# run-time error, the variable, " guess " wasn't labeled as a int or float which cause it to break while running

# logic error, you have an unlimited attempts in this game

#      