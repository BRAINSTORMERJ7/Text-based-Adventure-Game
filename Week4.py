import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroad.")
    time.sleep(1)
    print("A mysterious path lies to your left, and a dark forest is to your right.")
    time.sleep(1)
    print("Which path will you choose?")

def make_choice():
    print("\n1. Take the mysterious path to the left.")
    print("2. Enter the dark forest to the right.")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def mysterious_path():
    print("\nYou follow the mysterious path and encounter a magical creature.")
    time.sleep(1)
    print("It offers you a choice between two potions:")
    time.sleep(1)
    print("1. A glowing blue potion.")
    print("2. A shimmering red potion.")
    choice = input("Which potion will you choose (1 or 2): ")
    if choice == '1':
        print("\nThe blue potion grants you the power of teleportation! You move ahead.")
    elif choice == '2':
        print("\nThe red potion transforms you into a giant eagle! You soar through the skies.")
    else:
        print("\nInvalid choice! The magical creature disappears, and you find yourself back at the crossroad.")

def dark_forest():
    print("\nYou enter the dark forest and come across a rickety bridge.")
    time.sleep(1)
    print("A troll guards the bridge and demands a toll.")
    time.sleep(1)
    print("1. Pay the toll and cross the bridge.")
    print("2. Try to sneak past the troll.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("\nThe troll is pleased and lets you cross safely.")
    elif choice == '2':
        print("\nYour attempt to sneak past fails, and the troll chases you away.")
    else:
        print("\nInvalid choice! The troll gets angry, and you find yourself back at the crossroad.")

def main():
    introduction()
    while True:
        choice = make_choice()
        if choice == '1':
            mysterious_path()
            break
        elif choice == '2':
            dark_forest()
            break
        else:
            print("Invalid input! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
