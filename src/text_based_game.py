# IT 140 Module Seven Project Two
# Student Name: Jania King

def show_instructions():
    """Displays the game instructions and commands to the player."""
    print("=========================================================")
    print(" Dragon Text Adventure Game ")
    print("=========================================================")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Item command: get 'item_name'")
    print("Type 'exit' to quit the game.")
    print("=========================================================\n")


def main():
    # 1. Map setup: A dictionary linking rooms to one another and placing items in specific rooms.
    # Note: The 'Dining Room' contains the Dragon (villain) and no collectible item.
    rooms = {
        'Great Hall': {'south': 'Bedroom', 'north': 'Dungeon', 'east': 'Kitchen', 'west': 'Library'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar', 'item': 'Armor'},
        'Cellar': {'west': 'Bedroom', 'item': 'Helmet'},
        'Dungeon': {'south': 'Great Hall', 'east': 'Gallery', 'item': 'Sword'},
        'Gallery': {'west': 'Dungeon', 'item': 'Shield'},
        'Kitchen': {'west': 'Great Hall', 'north': 'Dining Room', 'item': 'Potion'},
        'Library': {'east': 'Great Hall', 'item': 'Book'},
        'Dining Room': {'south': 'Kitchen', 'item': 'Dragon'} # Villain Room
    }

    # Initialize gameplay variables
    current_room = 'Great Hall'
    inventory = []
    win_condition_items = 6

    # Show instructions once at the start of the game
    show_instructions()

    # 2. Main Gameplay Loop
    while True:
        # Display player's current status
        print(f"You are in the {current_room}")
        print(f"Inventory: {inventory}")
        
        # Check if current room has a collectible item that hasn't been picked up yet
        if 'item' in rooms[current_room] and rooms[current_room]['item'] != 'Dragon':
            print(f"You see a {rooms[current_room]['item']}")
        print("-" * 30)

        # 3. Check Villain / Win / Lose conditions immediately upon entering a room
        if current_room == 'Dining Room':
            if len(inventory) == win_condition_items:
                print("\nCongratulations! You have collected all items and defeated the dragon!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                print("\nNOM NOM... GAME OVER!")
                print("You faced the dragon without all your gear and were eaten!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break # End the game loop

        # 4. Prompt for and accept player input
        player_input = input("Enter your move: ").strip().lower()

        # Handle explicit exit command
        if player_input == 'exit':
            print("Thank you for playing! Game over.")
            break

        # Parse commands (expecting formats like "go north" or "get sword")
        command_parts = player_input.split()

        # Input validation for command length
        if len(command_parts) < 2:
            print("Invalid command syntax! Use 'go [direction]' or 'get [item]'.\n")
            continue

        action = command_parts[0]
        # Handle multi-word items gracefully (e.g., if an item name has spaces)
        target = " ".join(command_parts[1:]).title() 

        # 5. Handle Movement Command
        if action == 'go':
            direction = command_parts[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You moved {direction}.\n")
            else:
                print(f"You cannot go {direction} from here!\n")

        # 6. Handle Gathering Items Command
        elif action == 'get':
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == target.lower():
                item_to_get = rooms[current_room]['item']
                inventory.append(item_to_get)
                print(f"Success! You have added the {item_to_get} to your inventory.\n")
                # Remove the item from the room so it cannot be collected again
                del rooms[current_room]['item']
            else:
                print(f"Can't get {target}! That item is not in this room.\n")

        # Handle unrecognized action verbs
        else:
            print("Invalid action! Start your command with 'go' or 'get'.\n")


if __name__ == "__main__":
    main()

