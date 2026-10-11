# IT 140 Module Six Milestone
# Student Name: Jania King

# Define the dictionary linking rooms to one another
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

def show_instructions():
    """Displays the game instructions and commands to the player."""
    print("Welcome to the Dragon Text Game Prototype!")
    print("Move commands: go South, go North, go East, go West")
    print("Type 'exit' to quit the game.\n")

def main():
    # 1. Establish the starting room
    current_room = 'Great Hall'
    
    # Show instructions once at the start of the game
    show_instructions()
    
    # 2. Create the gameplay loop
    while current_room != 'exit':
        # 3. Display the current room status
        print(f"You are in the {current_room}.")
        
        # 4. Prompt for and get command from the player
        player_input = input("Enter your move: ").strip().lower()
        print("-" * 30) # Visual separator for readability
        
        # 6. Handle exit command
        if player_input == 'exit':
            current_room = 'exit'
            continue
            
        # Parse command (expecting formats like "go north" or just "north")
        # Splitting helps handle inputs like 'go south' or just 'south' gracefully
        command_parts = player_input.split()
        
        if len(command_parts) == 2 and command_parts[0] == 'go':
            direction = command_parts[1]
        elif len(command_parts) == 1:
            direction = command_parts[0]
        else:
            # 7. Handle invalid command syntax
            print("Invalid command syntax! Use 'go [direction]' or 'exit'.\n")
            continue
            
        # 5. Handle a valid movement command using the dictionary
        if direction in rooms[current_room]:
            # Move between rooms process
            current_room = rooms[current_room][direction]
            print(f"You moved {direction}.\n")
        else:
            # Handle invalid directional movement (no room in that direction)
            print(f"You cannot go {direction} from here!\n")
            
    # 6. Handle loop termination / game exit message
    print("Thank you for playing! Game over.")

if __name__ == "__main__":
    main()
