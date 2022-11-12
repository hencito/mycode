#!/usr/bin/env/ python3

def main():

    # delaring whichfarm
    whichfarm =""
    non_animals = ["carrots", "celery"]
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    farms_2 = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

    # debug code
    # print(farms_2)

    #Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
    
    while whichfarm  not in("southwest farm","northeast farm","east farm","west farm"):
        whichfarm= input("Please select a farm (Southwest Farm, Northeast Farm, East Farm, West Farm)\n>>").lower()


    #write a for loop that returns all the animals from the Farm!


    for farm in farms_2:
        if farm["name"].lower() == whichfarm:
            for item in farm["agriculture"]:
                if item not in non_animals:
                    print(item)

if __name__ == "__main__":
    main()
