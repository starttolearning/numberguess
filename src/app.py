# import libraries here
import random

# global variables
game_on = None
secret = None
guesses = None

# game level difficulty easy


def level_difficulty_easy():
    global game_on, secret, guesses
    secret = random.randrange(0, 100)
    guesses = 0

    while game_on:
        user_guess = int(input("Please guess a number between 0 and 100: "))
        if user_guess > secret:
            print("Your guess is too high, try again.")
            guesses += 1
        elif user_guess < secret:
            print("Your guess is too low, try again.")
            guesses += 1
        elif user_guess == secret:
            print("You got the right guess, cheer up!\n\n")
            print("And you have tried {} times.\n\n".format(guesses))
            start_again()
        else:
            print("Your input is not between 0 and 100, Please check your input!\n")

# game level difficulty hard


def level_difficulty_hard():
    global game_on, secret, guesses
    secret = random.randrange(0, 100)
    guesses = 5  # set the total try times

    while game_on and guesses != 0:
        user_guess = int(input("Please guess a number between 0 and 100: "))
        if user_guess > secret:
            print("Your guess is too high, try again.")
            guesses -= 1
        elif user_guess < secret:
            print("Your guess is too low, try again.")
            guesses -= 1
        elif user_guess == secret:
            print("You got the right guess, cheer up!\n\n")
            print("And you have tried {} times.\n\n".format(guesses))
            start_again()
        else:
            print("Your input is not between 0 and 100, Please check your input!\n")

        if guesses == 0:
            print("You have used all your chances, FAILED!")
            stop_game()

# start game


def start_game():
    global game_on, secret
    game_on = True
    level = which_level_you_want_to_play_with()
    if level == "easy":
        level_difficulty_easy()
    elif level == "hard":
        level_difficulty_hard()
    else:
        stop_game()

# stop game


def stop_game():
    global guesses, secret, game_on
    guesses, secret, game_on = None
    print("Thank you for play this little funny game.")
    return None

# some call backs


def start_again():
    global game_on, secret
    choice = input("Do you want to play again? \nType yes or no.")
    if choice == "yes":
        game_on = True
        secret = random.randrange(0, 100)
    else:
        stop_game()


def which_level_you_want_to_play_with():
    header = '''
    ==============================================
    + You are now playing WHO IS THE GUESS KING  +
    + This game have the following levels:       +
    +   1. easy, you have infinite time to guess +
    +   2. hard, you only have 5 times to get    +
    +      the right answer.                     +
    + To Start Playing Game Follow Our Instructions
    ===============================================
    '''
    print(header)
    return input("Tell us which level you want to play with.\neasy, hard, quit.")



# play game here


if __name__ == "__main__":
    start_game()
