#!/usr/bin/env python3

"""Write a script that will output ALL 99 LINES of the song 99 Bottles of Beer on the Wall!
   If you're unfamiliar with the song, here's what the output would look like:

    99 bottles of beer on the wall!
    99 bottles of beer on the wall! 99 bottles of beer! You take one down, pass it around!
    98 bottles of beer on the wall!
    98 bottles of beer on the wall! 98 bottles of beer! You take one down, pass it around!
    97 bottles of beer on the wall!
    97 bottles of beer on the wall! 97 bottles of beer! You take one down, pass it around!
    [...and so on...] """

def main():
    
    i=0    

    howmany=int(input("How many bottles of beer do you want to count down?"))

    for bottle in range(howmany):
        i += 1
        countdown = 100 - i
        
        if countdown >= 0: 
            print(f"{countdown} bottles of beer on the wall!")
            print(f"{countdown} bottles of beer on the wall! {countdown} bottles of beer! You take one down, pass it around!")
        
        else:
            print("No more bottles left on the wall!")
            break

if __name__ == "__main__":
    main()
