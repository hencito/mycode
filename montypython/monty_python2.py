#!/usr/bin/env python3

def main():
    # We're going to use a counter to control our while loop in this lab, so let's start our counter (which we'll call round, equal to 0).
    round = 0

    # Make a simple while loop that will loop forever (or until we execute a break).
    while True:
        round = round +1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ") 
        if answer =="Brian":
            print("Correct!")
            break
        elif round == 3:
            print("Sorry, the name was Brian.")
            break
        else:
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()
