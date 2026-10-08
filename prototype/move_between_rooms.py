"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room.
current_room = 'Great Hall'

# Create the gameplay loop.
while current_room != 'exit':

    # Display the current room.
    print('You are currently in the', current_room)

    # Ask the player for a movement command or exit.
    command = input('Enter a direction or exit: ').lower()

    # Check for a valid movement command.
    if command in rooms[current_room]:
        current_room = rooms[current_room][command]

    # Check if the player wants to exit.
    elif command == 'exit':
        current_room = 'exit'

    # Handle invalid commands.
    else:
        print('Invalid direction. Please try again.')

# Display a message when the game ends.
print('Thanks for playing!')
