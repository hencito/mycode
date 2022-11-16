#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      use [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # create a list of keys
    keylist = list(rooms[currentRoom].keys())
    # print the player's current location
    
    print('===========================')
    # check if the player is in the Basement
    if currentRoom == 'Basement':
        
        print('You sense that there is a Secret Passage at the north-east end of this room.')
        print('You are in the ' + currentRoom)
        
        # inform the player of their movement options
        print('---------------------------')
        print('Your movement options are:')
        for option in keylist:
            if option not in ['item', 'special-item']:
                print(option)
              
    else:
        
        print('You are in the ' + currentRoom)
        
        print('---------------------------')
        print('Your movement options are:')
        # inform the player of their movement options
        for option in keylist:
            if option not in ['item', 'special-item']:
                print(option)
        
    # print what the player is carrying            
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('Inventory:', inventory)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # check if there's an item in the room, if so print it
    
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    if "special-item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['special-item'])
    print('===========================')

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'sword'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'south' : 'Basement',
                  'enemy' : 'monster'
                },

            'Dining Room' : {
                'west' : 'Hall',
                'south' : 'Garden',
                'item' : 'potion'
            },

            'Garden' :{
                'north' : 'Dining Room'
            },

            'Basement' :{
                'north' : 'Kitchen',
                'north-east' : 'Secrete Passage',
                'item' : 'key',
                'special-item' : 'skelleton key'
            },

            'Secrete Passage' :{
                'north-east':'Dining Room',
                'sout-west' : 'Basement'
            }

         }

# start the player in the Hall
currentRoom = 'Hall'

# this will track what 'use' action will the player take. 
playerAction = ''


# this tracks the status or passages and trap doors
passageStatus= 'locked'


showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')
        print('\n')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # block movement to the Secret Passage if the passage is locked
            if move[1] == 'north-east' and passageStatus == 'locked':
                print('You can\'t go that way, the passage is locked.')
            else:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
                
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!\n')

        

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item or a special item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!\n')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # 3 if the special-item in the room matches the special-item the player wishes to get
        elif "special-item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['special-item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!\n')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['special-item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!\n')


        
    
## If a player has a sword and enters a room with a monster
    if 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
           
        if 'enemy' in rooms[currentRoom] and 'sword' in inventory and 'monster' in rooms[currentRoom]['enemy']:
            
            
            print('--------------------------------------------------------')
            print('There is a monster in the room...and you have a sword...')
            playerAction = input('Would you like to fight it? (y/n)').lower()
            print('\n')

            if playerAction == "y":
                print('Please input your action')
                move = ''
                while move == '':  
                    move = input('>')
                move = move.lower().split(" ", 1)
                print('\n')
            
            else:
                print('A monster attacks!!!')
                print('The monster has got you... GAME OVER!')
                break
        # this will end the game if the player enters the room without an item: sword
        if playerAction == '':
                print('A monster attacks!!!')
                print('The monster has got you... GAME OVER!')
                break
            
       
   
    # give the player the ability to take an action
    if move[0] == 'use':
        # take a swing
        if move[1] == 'sword':
            if 'sword' in inventory  and 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
                print('*******************************************************************')
                print('With lightning speed you swing your sword and defeat the monster!!!')
                print('*******************************************************************')
                print('\n')
                del rooms[currentRoom]['enemy']
                playerAction = ''
        else:
            # tell them they cant do that
            print('Can\'t do that. You do not have a'  + move[1] + '!')

  
    
    # define how to open the Secret Passage
    if currentRoom == 'Basement' and 'skelleton key' in inventory:
        print('--------------------------------------------------------')
        playerAction = input('Would you like to use the skelleton key? (y/n)').lower()
        print('\n')

        if playerAction == 'y':

            print('***************************************************************')
            print ('You open the Secret Passage. Go in and see where it takes you!')
            print('***************************************************************')
            passageStatus ='open'
            inventory.remove('skelleton key')
      

    # if 'enemy' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['enemy']:
    #     print('A monster has got you... GAME OVER!')
    #     break

        ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('--------------------------------------------------------------------------')
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        print('--------------------------------------------------------------------------')
        break
    
    # provide the player with a message if they enter the garden without the key
    if currentRoom == 'Garden' and 'key' not in inventory and 'potion' in inventory:
        print('---------------------------------------------------------')
        print('At the other end of the Garden, there seems to be a Gate.')
        print('A "key" is needed to open it.')
        print('Go back and search for the key!')
        print('---------------------------------------------------------\n')

    # provide the player with a message if they enter the garden without the potion
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' not in inventory:
        print('----------------------------------------------------------------------------------')
        print('The plants in the garden are releasing spores to the air.')
        print('You have encontered this before; if you stay any longer then you will fall asleep.')
        print('You will need a potion to combat the sleep effect.')
        print('Go back and search for a potion!')
        print('----------------------------------------------------------------------------------\n')

    if currentRoom == 'Garden' and 'key' not in inventory and 'potion' not in inventory:
        print('---------------------------------------------------------------------------')
        print('The Garden does not seem very safe. You may need a few items to traverse it.')
        print('Go back and search!')
        print('---------------------------------------------------------------------------\n')




