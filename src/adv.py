from room import Room

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
chamber! Sadly, it has already been completely emptied by
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
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



from player import Player

current_room = 'outside'
game_over = False
player = Player(room[current_room])
cardinals = ['n', 's', 'w', 'e'] # remove this if not needed in memory, used in elif under while not game_over

while not game_over:
    print(player.current_room)
    command = input("Choose wisely:\nEnter the first letter of a cardinal direction, or 'q' to quit: ").lower()
    if command == 'q':
        game_over = not game_over
        print("\nYou have asked to quit the game")
        break
    elif any([direction == command for direction in cardinals]):
        dir_key = f'{command}_to'
        for key in room[current_room].__dict__:
            if key == dir_key:
                print(f'key: {key}\ncurrent_room: {room[current_room]}\ndir_key: {dir_key}')
                print(f'building out: {room}')
    else:
        print(f"\n{command} isn't a recognized command. Enter the first letter of a cardinal direction or 'q'")

if game_over:
    print("Game Over")