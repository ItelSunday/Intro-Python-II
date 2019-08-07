from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has alreapytthdy been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Windra", room["outside"])
# print(f"{player.name} is in",room['player.current_room'])

error_message = None

# print(player.name)
#value of input to test IF statement

# Write a loop that:
#declaring to current room
while True:
    current_room = player.current_room 
    print(player.current_room)
    
    cmd = input("Choose the direction you want to go to, 'n' for North, 's' for South, 'e' for East, 'w' for West,'q' for Quit -> ")
    
    #test valid direction or not a valid direction: making sure is not null
    #redeclares valid room
    if cmd == 'n': 
        if current_room.n_to is not None: 
            player.current_room = current_room.n_to 
            continue
        else:
            print("you can't go to this direction")
    elif cmd == 's':
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            continue
        else:
            print("you can't go to this direction")
            continue
    elif cmd == 'e':
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
            continue
        else:
            print("you can't go to this direction")
            continue
    elif cmd == 'w':
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("you can't go to this direction")
            continue
    elif cmd == 'q':
        print("Good bye! Enjoy your freedom")
        break
    else:
        print("Invalid command. Use direction: n, s, e, w, q")
    
            
    
            
        
        
        
    
# * Prints the current room name
print("Player.current_room.name")

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


