#!/usr/bin/python3


def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
    
    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


    # From the challenge list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:
    # My eyes! The goggles do nothing!
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")


    # From the trial list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:
    # My eyes! The goggles do nothing!
    a=trial[2]["goggles"]
    b=trial[2]["eyes"]
    c=trial[3]

    print(f"My {a}! The {b} do {c}!")


    # From the nightmare list, pull the strings eyes, goggles, and nothing and create a print function that returns this output
    # My eyes! The goggles do nothing!   
    a=nightmare[0]["user"]["name"]["first"]
    b=nightmare[0]["kumquat"]
    c=nightmare[0]["d"]


    print(f"My {a}! The {b} do {c}!")



if __name__ == "__main__":
    main()
