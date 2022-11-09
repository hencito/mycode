#!/usr/bin/python3

def main():

# Save a user's input to the variable char_name
    char_name=input("Which character do you want to know about? (Starlord, Mystique, Hulk)").capitalize()

# Save a user's input to the variable char_stat
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")


# this is the dictionary for this exercise
    marvelchars= {
    "Starlord":
     {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
                 }


#Create a print function that combines that information into this output:
# <char_name>'s <char_stat> is: <value>


    print(f"{char_name}'s {char_stat} is: { marvelchars[char_name][char_stat].title()}")



# call our main function

if __name__ == "__main__":
    main()



        
