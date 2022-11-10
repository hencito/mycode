#!/usr/bin/env python3

#import libraries
#import emoji

# end of import libraries
# Write your own program using if, elif, and else! You can pick from one of the following ideas, or come up with your own!

""""Requirements:
        Return unique answers based on the input provided... multiple results should be possible.
        AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
        Use at least one while loop.
        Make all code "your own."
        ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative."""


def main():
        
        guess_round = 0
        answer = ""
        choice = "0"
        movies = {1:"The Hitchicker's Guide to the Galaxy", 2:"Little Rascals", 3:"Star Wars (all of them)"}
        play_again = "ask"

        #setup the game
        print("\n")
        print ("WELCOME TO COMPLETE THAT LINE!!!\n")
        print("The game where you complete the line of a movie quote")
        print("Good Luck! And may the odds be ever in your favor")
        
        while play_again not in ("n","no"):
                print("The Movies for todays game are: \n")
                print(movies)


                while choice not in("1","2","3"):
                        print("\n")
                        choice = input("Please choose a movie (1-3):\n>>")

                
                


                if choice == "1":
                        print("\n")
                        print("Complete the following line:")
                        print("So long and thanks for all the ____.\n")
                        while guess_round <=3:
                                guess_round  += 1
                                answer = input("Please type in your guess:\n>").lower()
                                if answer == "fish":
                                        print("\n")
                                        print("Correct!"+ "\N{party popper}")
                                        print("Your prize is a... Fish"+ "\N{fish}"+"!!!")
                                        print("... sorry we have a low budget"+"\N{upside-down face}")
                                        break
                                elif guess_round==3:
                                        print("\n")
                                        print("Sorry, the answer is 'fish'"+"\N{fish}"+".")
                                        print("I guess the odds were not in your favor..."+"\N{worried face}")
                                        print("Better luck next time! (next game date is unknown... you know, low budget and all"+"\N{upside-down face}")
                                        break
                                else:
                                        print("\n")
                                        print("Wrong guess"+"\N{neutral face}"+", try again")
                                        print("\n")
                                        

                if choice == "2":
                        print("\n")
                        print("Complete the following line:")
                        print("Spanky: How’s the toothache, bub?\nAlfalfa: Uh, the dentist pulled my wisdom teeth.\nSpanky: So that explains why you’re acting so ______.\n")
                        while guess_round <=3:
                                guess_round  += 1
                                answer = input("Please type in your guess:\n>").lower()
                                if answer == "stupid":
                                        print("\n")
                                        print("Correct!"+"\N{party popper}")
                                        print("Your prize is a... Dictionary"+"\N{closed book}"+"...from the dollar store!!!")
                                        print("... sorry we have a low budget"+"\N{upside-down face}")
                                        break
                                elif guess_round==3:
                                        print("\n")
                                        print("Sorry, the answer is 'stupid'"+"\N{thinking face}"+".")
                                        print("I guess the odds were not in your favor..."+"\N{worried face}")
                                        print("Better luck next time! (next game date is unknown... you know, low budget and all)"+"\N{upside-down face}")
                                        break
                                else:
                                        print("\n")
                                        print("Wrong guess"+"\N{neutral face}"+", try again")
                                        print("\n")
                                

                if choice == "3":
                        print("\n")
                        print("Complete the following line:")
                        print("Anakin: I don't like '____' . It's coarse and rough and irritating and it gets everywhere. Not like here. Here everything is soft and smooth.\n")
                        while guess_round <=3:
                                guess_round  += 1
                                answer = input("Please type in your guess:\n>").lower()
                                if answer == "sand":
                                        print("\n")
                                        print("Correct!"+ "\N{party popper}")
                                        print("Your prize is a... fancy bottle of Sand"+"\N{hourglass}"+"!!!")
                                        print("... sorry we have a low budget"+"\N{upside-down face}")
                                        break
                                elif guess_round==3:
                                        print("\n")
                                        print("Sorry, the answer is 'sand'."+"\N{hourglass}")
                                        print("I guess the odds were not in your favor..."+"\N{worried face}")
                                        print("Better luck next time! (next game date is unknown... you know, low budget and all)"+"\N{upside-down face}")
                                        break
                                else:
                                        print("\n")
                                        print("Wrong guess"+"\N{neutral face}"+", try again")
                                        print("\n")
                
                
                
                #Reset the game for a new playthrough 
                choice = "0"
                guess_round = 0
                print("\n")
                play_again=input("Would you like to Play Again?(y/n)\n>>").lower()

if __name__=="__main__":
        main()
                

                

