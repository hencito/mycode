#!/usr/bin/env python3
"""This is related to 31.Challenge: Lists,
input, Concatenation"""

#Imporing the random module
import random


def main():
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)

    num=int( input("Please enter a number between 0 and 18: "))

    student_name = tlgstudents[num]

    print(f"{student_name} always use {wordbank[2]} {wordbank[1]} to indent.")

    """Running out of time in class,  so using the solution for the bonus material"""
    # for Bonus 2. Student name printed out below is related to input from user.
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]


    print(f"Your unfortunate victim is {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()
