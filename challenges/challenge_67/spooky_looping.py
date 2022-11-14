#!/usr/bin/env python3


# Instantiate a counter
count = 0

# Read in the content of the Dracula novel as a file
with open("dracula.txt","r") as foo:
    with open("vampytimex.txt","w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                count+=1
                print(line)
                fang.write(line)
print(count)
