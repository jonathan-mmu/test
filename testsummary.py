def main_menu():
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("       🐈  🐾MAIN MENU🐾  🐈")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Start New Game")
        print("2. Load Saved Game")
        print("---------------------------------------")
        
        choice = input("Please choose an option: ")

        if choice == "1":
            NewGame()
            break
        elif choice == "2":
            LoadGame()
            break
        else:
            print("Invalid choice. Please enter a number either 1 or 2.")
    
# SAVE GAME FUNC
def save_game_txt(PlayerName, game_state, filename = "databases/PlayersData.txt"):
    with open(filename, 'a') as file:  
        file.write(f"Player: {PlayerName}\n")
        for key, value in game_state.items():
            file.write(f"{key}: {value}\n")
        # Blank line to separate data
        file.write("\n")

# LOAD GAME FUNC
def load_game_txt(PlayerName, password, filename = "databases/PlayersData.txt"):
    game_state = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        player_found = False
        for line in lines:

            if line.startswith("Player:"):

                # (": ")[1] = player's name
                CurrentPlayer = line.split(": ")[1].strip()
                if CurrentPlayer == PlayerName:
                    # True = data found // False = ignore
                    player_found = True
                else:
                    player_found = False

            elif player_found:
                # Empty line to indicate the end of a player data
                if line.strip() == "":
                    break  
                key, value = line.strip().split(': ')
                game_state[key] = value

    if game_state.get('password') == password:
        return game_state
    else:
        print("Incorrect name or password.")
        return None

def NewGame():
    print("Starting a new game...")
    PlayerName = input("Enter Your Name: ")
    password = input("Create a new password: ")
    game_state = {
        'password': password,
    }
    save_game_txt(PlayerName, game_state)
    print("Game saved successfully.")
    print(f"Hello, {PlayerName}!")

import sys

def LoadGame():
    attempts = 5
    while attempts > 0:         
        print("Loading saved game...")
        PlayerName = input("Enter your name: ")
        password = input("Enter your password: ")

        # Correct input
        game_state = load_game_txt(PlayerName, password)
        if game_state:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"  😸 Hello again, {PlayerName}! 😸")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1. View previous summary")
            print("2. Play a new game")
            print("---------------------------------------")

            valid = False
            ValidAttempts = 3

            while not valid and ValidAttempts > 0:
                choice2 = input("Please choose an option: ")
                choice2 = int(choice2)
                if choice2 in [1, 2]:
                    valid = True
                else:
                    print("Invalid choice. Please enter a number either 1 or 2.")
                    ValidAttempts -= 1

            if valid:
                if choice2 == 1:
                    summary()
                    sys.exit()
                    return None
                elif choice2 == 2:
                    break
            else:
                print("Invalid choice. Please enter a number either 1 or 2.")              

        # Incorrect input
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                print("Maximum attempts reached.")
                print("Exiting game... Goodbye!")
                sys.exit()

def summary():
    print("Summary of your previous game...")
    return

# Initialize attributes, stats, and inventory
attributes = {"Name": None, "Gender": None, "Age": None, "Color": None, "Size": None, "Personality": None}
stats = {
    "Health": {"Current": 50, "Max": 100}, 
    "Energy": {"Current": 50, "Max": 100}, 
    "Hunger": {"Current": 50, "Max": 100}, 
    "Mood": None, 
    "Affection": {"Current": 50, "Max": 100}
}
inventory = {"Catnip": False, "Treats": False, "Yarnball": False, "Mouse Toy": False}
attribute_values = {
    "Age": ["1", "20"],
    "Gender": ["Male", "Female"],
    "Color": ["White", "Black", "Orange"],
    "Size": ["Fat", "Skinny"],
    "Personality": ["Playful", "Curious", "Lazy"]
}

# Main function to orchestrate the game
def main():
    introduction()
    get_attributes()
    set_lim()
    gameplay()
    display_attributes()
    display_stats()
    press_enter_to_continue()
    the_end()
    ending()
    return

# plot introduction
def introduction():
    print("Welcome to Purrfect Life, a Cat Simulator")
    #add a plot

    return

# Function to collect cat attributes
def get_attributes():
    global attributes

    attributes["Name"] = input("Name: ")
    attributes["Age"] = check_attributes("Age")
    attributes["Gender"] = check_attributes("Gender")
    attributes["Color"] = check_attributes("Color")
    attributes["Size"] = check_attributes("Size")
    attributes["Personality"] = check_attributes("Personality")

    return

# Validate attribute input
def check_attributes(attribute):
    global attribute_values
    values = attribute_values[attribute]

    while True:
        # Check the value for age or other attributes
        if attribute == "Age":
            temp = str(input(f"Select your cat's {attribute} ({'-'.join(values)}): "))
            try:
                value = int(temp)
            except:
                print(f"ERROR: Please enter an integer! ({'-'.join(values)})")
                continue
            else:
                if int(values[0]) <= value <= int(values[1]):
                    return value
            print(f"ERROR: Please enter a valid {attribute.lower()}! ({'-'.join(values)})")

        else:
            temp = str(input(f"Select your cat's {attribute} ({', '.join(values)}): "))
            for value in values:
                if temp.lower() == value.lower():
                    return value
            print(f"ERROR: Please enter a valid {attribute.lower()}! ({', '.join(values)})")

# Set the maximum limits and initialise stats based on age, size, personality
def set_lim():
    global attributes
    global stats

    if (attributes["Age"] >= 15) | (attributes["Age"] <=2):
        stats["Health"]["Current"] -= 20
        stats["Health"]["Max"] -= 20

    if attributes["Size"] == "Fat":
        stats["Health"]["Max"] -= 10
        stats["Hunger"]["Max"] += 10
    else:
        stats["Hunger"]["Current"] += 20
        stats["Hunger"]["Max"] -= 10

    if attributes["Personality"] == "Playful":
        stats["Energy"]["Current"] += 20
        stats["Energy"]["Max"] += 20
    elif attributes["Personality"] == "Lazy":
        stats["Energy"]["Current"] -= 20
        stats["Energy"]["Max"] -= 20

    return

# gameplay
def gameplay():
    # Read game data 
    with open("databases/game_data.txt", "r") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 5):
            statement = eval(lines[i])
            stats_adjustments = eval(lines[(i + 1)])
            inventory_adjustments = eval(lines[(i + 2)])
            results = eval(lines[(i + 3)])
            print(statement)
            while True:
                action = get_action(1, len(results))
                # exit if user wants to quit
                if action == 0:
                    return

                update_stats(stats_adjustments[(action - 1)])
                success = update_inventory(inventory_adjustments[(action - 1)])
                if success: 
                    print(results[(action - 1)])
                else:
                    print("\nYou do NOT have the required items to carry out this action! Please select another action.")
                    continue

                press_enter_to_continue()
                display_stats()

                # check whether cat alive or not
                gameover = check_condition()
                press_enter_to_continue()
                if gameover:
                    print("\nYou died.... \n---GAMEOVER---")
                    return
                
                break
                
    return

def get_action(min, max):
    while True:
        action = input(f"Action ({min}-{max}, or 'q' to quit): ").strip().lower()

        # Check if player wants to quit
        if action == 'q':
            print("\nYou chose to quit the game. Here are your final stats:")
            return 0
        elif action.isdigit():
            action = int(action)
            if min <= action <= max:
                return action
            else:
                print(f"❌ ERROR: Please enter a valid action between {min} and {max}.")
        else:
            print("❌ ERROR: Please enter a number or 'q' to quit.")

# Update the cat's stats
def update_stats(stats_adjustment):
    global stats

    for stat in stats:
        if stat != "Mood":
            stats[stat]["Current"] = check_lim(stats[stat]["Current"] + stats_adjustment[stat], 0, stats[stat]["Max"])

    # dynamic mood
    if stats["Hunger"]["Current"] > 50:
        stats["Mood"] = "Hungry 😾"
    elif stats["Energy"]["Current"] < 40:
        stats["Mood"] = "Tired 😴"
    elif stats["Health"]["Current"] < 30:
        stats["Mood"] = "Sick 🤢"
    elif stats["Affection"]["Current"] > 70 and stats["Energy"]["Current"] > 50:
        stats["Mood"] = "Happy 😺"
    else:
        stats["Mood"] = "Neutral 😺"

# Ensure stats stay within bounds
def check_lim(value, min, max):
    if value <= min:
        return min
    elif value >= max:
        return max
    else:
        return value

def update_inventory(inventory_adjustment):
    global inventory

    # Return if no item adjustment to be made
    if inventory_adjustment == None:
        return True

    # Check whether user have the required items
    for item in inventory_adjustment:
        if (not inventory_adjustment[item]) & (not inventory[item]):
            return False

    # Update the inventory
    for item in inventory_adjustment:
        inventory[item] = inventory_adjustment[item]

    return True 

def check_condition():
    global stats
    
    # Return gameover if cat health = 0 (Cat dies)
    if stats["Health"]["Current"] == 0:
        return True

    if stats["Energy"]["Current"] <= 20:
        stats["Health"]["Current"] = check_lim(stats["Health"]["Current"] - 5, 0, stats["Health"]["Max"])
        press_enter_to_continue()
        print("\n❗❗ Energy is low! Your health is depleting! ❗❗")

    if stats["Hunger"]["Current"] >= (stats["Hunger"]["Max"] - 20):
        stats["Health"]["Current"] = check_lim(stats["Health"]["Current"] - 5, 0, stats["Health"]["Max"])
        press_enter_to_continue()
        print("\n❗❗ You are hungry! Your health is depleting! ❗❗")

    # Check health after update
    if stats["Health"]["Current"] == 0:
        press_enter_to_continue()
        display_stats()
        return True

    return False

#display attributes
def display_attributes():
    global attributes
    print("\n📋 **Cat Attributes:**")
    for key, value in attributes.items():
        print(f"  🔹 {key}: {value}")
    return

# display current stats/inventory
def display_stats():
    global stats, inventory
    print("\n🐾 **Summary of Your Cat** 🐾")
    # Display stats
    print("\n📊 **Current Stats:**")
    print(f"  ❤️ Health: {stats['Health']['Current']}/{stats['Health']['Max']}")
    print(f"  ⚡ Energy: {stats['Energy']['Current']}/{stats['Energy']['Max']}")
    print(f"  🍗 Hunger: {stats['Hunger']['Current']}/{stats['Hunger']['Max']}")
    print(f"  😺 Mood: **{stats['Mood']}**")
    print(f"  💕 Affection: {stats['Affection']['Current']}/{stats['Affection']['Max']}")

    # Display inventory (show only acquired items)
    print("\n🎒 **Inventory:**")
    owned_items = [item for item, has_item in inventory.items() if has_item]

    if owned_items:
        for item in owned_items:
            print(f"  ✅ {item}")
    else:
        print("  ❌ No items collected.\n")
    
    return

def press_enter_to_continue():
    input("\n🔹 Press Enter to continue...")
    return

def the_end():
    input("\n ⭐The End... press enter to see results!")
    return

# Display the ending message
def ending():
    print("\n **Thank you for playing Purrfect Life!** ✨\n")
    return

# Run the program
main_menu()
main()
