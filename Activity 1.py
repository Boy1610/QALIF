import random 

def main():
    """Start a colour guessing game."""
    print("Guess the colour!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
    ]

    x = random.choice(rainbow)
    # Uncomment to reveal the correct answer for testing
    # print(x)
    
    guess = None 

    while x != guess:
        guess = input("What colour am I thinking of? ").strip().lower()

        if x == guess:
            print("You guessed {}. Congratulations, you got it right!".format(guess))
        else:
            print("You guessed {}. Unfortunately, it's wrong. Try again!".format(guess))

main()
