from classes import *

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue") # Custom Class #1
    print("4. Custom Class #2 (Implement this)") # Custom Class #2 -- still needs to be implemented

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Rogue(name) # Custom Class #1
    elif class_choice == '4':
        pass # Custom Class #2 -- still needs to be implemented
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal() # This method is in the Character class and still needs to be implemented.
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        # This is the wizard's turn. Check if he's alive, if he is, regenerate and attack the player back.
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        # Check if the player is still alive. If not, state he has been defeated and end the loop.
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    # Check if the wizard is still alive, if not, declare victory for the player.
    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


# This is our main function. This is where we create a player object, a wizard object, and commence the battle between them.
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

# This where the program begins.
if __name__ == "__main__":
    main()