# Full Name: Damien Taylor

# IT 140 Project Two: Text-Based Adventure Game

def show_instructions():
"""Display the game objective and available commands."""
print("Abandoned Castle Adventure")
print("Collect all 6 items before entering the Final Chamber.")
print("Move commands: go north, go south, go east, go west")
print("Item command: get item name")
print("Type 'quit' to stop playing.")

def show_status(current_room, inventory, rooms):
"""Display the player's current game status."""
print("\n------------------------------")
print("You are in the", current_room)
print("Inventory:", inventory)


if "item" in rooms[current_room]:
    print("You see a", rooms[current_room]["item"])

print("------------------------------")


def main():
"""Run the main gameplay loop."""
rooms = {
"Entrance Hall": {
"north": "Library",
"east": "Armory",
"west": "Storage Room"
},
"Library": {
"south": "Entrance Hall",
"east": "Study",
"north": "Alchemy Room",
"item": "Ancient Map"
},
"Armory": {
"west": "Entrance Hall",
"south": "Dungeon",
"item": "Silver Sword"
},
"Storage Room": {
"east": "Entrance Hall",
"item": "Flashlight"
},
"Study": {
"west": "Library",
"item": "Rusty Key"
},
"Alchemy Room": {
"south": "Library",
"east": "Final Chamber",
"item": "Health Potion"
},
"Dungeon": {
"north": "Armory",
"east": "Final Chamber",
"item": "Golden Amulet"
},
"Final Chamber": {
"west": "Alchemy Room",
"south": "Dungeon",
"item": "The Shadow King"
}
}


current_room = "Entrance Hall"
inventory = []
total_items = 6

show_instructions()

while True:
    show_status(current_room, inventory, rooms)

    if current_room == "Final Chamber":
        if len(inventory) == total_items:
            print("Congratulations! You collected all six items and defeated The Shadow King!")
        else:
            print("The Shadow King has found you before you collected every item. GAME OVER!")
        print("Thanks for playing!")
        break

    command = input("Enter your move: ").strip().lower()

    if command == "quit":
        print("Thanks for playing!")
        break

    command_parts = command.split(maxsplit=1)

    if len(command_parts) != 2:
        print("Invalid command. Use 'go north' or 'get Ancient Map'.")
        continue

    action = command_parts[0]
    value = command_parts[1].strip()

    if action == "go":
        if value in rooms[current_room]:
            current_room = rooms[current_room][value]
        else:
            print("You can't go that way. Choose a valid direction.")

    elif action == "get":
        room_item = rooms[current_room].get("item")

        if room_item and room_item.lower() == value.lower():
            inventory.append(room_item)
            del rooms[current_room]["item"]
            print(room_item, "collected!")
        else:
            print("That item is not available in this room.")

    else:
        print("Invalid command. Use 'go direction' or 'get item name'.")


if **name** == "**main**":
main()
