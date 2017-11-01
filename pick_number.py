import random

print "Howdy!"
name = raw_input("What's your name?: ")
print "Welcome to my awesome game program, %s!" % (name)
print "Would you like to play? (Y or N)"


def game_state():
    """Determines user status for whether or not to run the game."""

    while True:

        status = raw_input('>>> ').upper()

        if status == "Y":
            return "Y"
            break

        elif status == "N":
            return "N"
            break

        else:
            print "That's not an option, please choose Y or N."


game_status = game_state()


def run_game(game_status):
    """Runs pick-a-number game depending on user status."""

    if game_status == "Y":

        number = random.randint(1, 100)

        print "I am thinking of a number between 1 and 100, what is your guess?"
        guess = raw_input(">>> ")

        if guess.isdigit() is True:
            guess = int(guess)

        else:

