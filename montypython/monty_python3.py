#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

def main():

    round = 0
    answer = " "

    while round < 3 and answer != "Brian":
        round += 1     # increase the round counter by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').lower()
        if answer == "brian": # logic to check if user gave correct answer
            print("Correct!")
            break
        elif answer=="shrubbery":
            print("You gave the super secret answer!")
            break
        elif round == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")


if __name__ == "__main__":
    main()

