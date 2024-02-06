import sys
import os
import time
import random

from enemy import enemy_types
from weapon import weapon
from store import store
from Story import Story
from Player import Player, Orc, Human, Wizard
from Directions import player_move, zonemap


def main():
    player = choose_character()
    Story.intro()
    title_screen(player)
    setup_game(player)
    zonemap = {}  # Assuming zonemap is defined elsewhere
    location_key = None  # Assuming no specific location key is selected initially
    maingame_loop(player, zonemap, location_key)
    Story.outro()

def title_screen(player):
    os.system('cls')
    print('|------------------------------|')
    print('| Welcome to the Text RPG Game |')
    print('|------------------------------|')
    print('|            -Start-           |')
    print('|            -Help-            |')
    print('|            -Quit-            |')
    print('|------------------------------|')
    title_screen_selections(player)


def help_menu(player):
    os.system('cls')
    print('|-------------------------------------------------|')
    print('| Welcome to the Text RPG Game                    |')
    print('|-------------------------------------------------|')
    print('| -Use up, down, left, right to move              |')
    print('| -Type your command to do something              |')
    print('| ^Look^ is the command to inspect something      |')
    print('|-------------------------------------------------|')
    title_screen_selections(player)


def title_screen_selections(player):
    option = input('> ')

    if option.lower() == 'start':
        start_game(player)
    elif option.lower() == 'help':
        help_menu(player)
    elif option.lower() == 'quit':
        sys.exit()
    else:
        while option not in ('start', 'help', 'quit'):
            print('Please input a valid command')
            option = input('> ')
            if option == 'start':
                start_game(player)
            elif option == 'help':
                help_menu(player)
            elif option == 'quit':
                sys.exit()

def start_game(player):
    zonemap = {}  # Assuming zonemap is defined elsewhere
    choose_character()
    setup_game(player)
    prompt(player, zonemap, None)  # Pass zonemap and location_key as arguments
    maingame_loop(player, zonemap, None)



def choose_character():
    os.system('cls')  # Clear the screen
    print("Choose your character class:")
    print("1. Wizard")
    print("2. Orc")
    print("3. Human")

    choice = input("Enter the number of your choice: ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a number between 1 and 3.")
        choice = input("Enter the number of your choice: ")

    if choice == "1":
        player = Wizard(zonemap)
    elif choice == "2":
        player = Orc(zonemap)
    elif choice == "3":
        player = Human(zonemap)

    os.system('cls')  # Clear the screen again
    player.show_stats()  # Show current stats of the player
    return player


def setup_game(player):
    os.system('cls')
    print("Are you ready to start the game?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Let's begin!")
        zonemap, location_key = initialize_game()  # Initialize game and get starting location
        prompt(player, zonemap, location_key)  # Pass zonemap and location_key to prompt
    else:
        print("Invalid choice. Please choose 1 or 2.")
        setup_game(player)
    os.system('cls')




def prompt(player, zonemap, location_key):
    print("\n" + "================================")
    print("What would you like to do?")
    print("Available locations:")

    for idx, location_key in enumerate(zonemap.keys(), 1):
        print(f"{idx}. {zonemap[location_key].name}")  # Print location names

    choice = input("Enter the number of the location you want to go to: ")
    while not choice.isdigit() or not (1 <= int(choice) <= len(zonemap)):
        print("Invalid choice. Please enter a number corresponding to a location.")
        choice = input("Enter the number of the location you want to go to: ")

    location_key = list(zonemap.keys())[int(choice) - 1]

    # Flag to control the prompt loop
    action_taken = False

    while not action_taken:
        action = input("What action would you like to take? (examine/shop): ")
        if action.lower() == 'examine':
            player_examine(player, location_key)
            action_taken = True
        elif action.lower() == 'shop':
            if zonemap[location_key].shop:
                shop_menu(player, zonemap[location_key].shop)
                action_taken = True
            else:
                print("There is no shop in this location.")
        elif action.lower() == 'move':
            player_move(player, zonemap, location_key)
            action_taken = True
        else:
            print("Invalid action. Please choose examine, move, or shop.")



def maingame_loop(player, zonemap, location_key):
    while not player.game_over:
        prompt(player, zonemap, location_key)



def start_encounter(player):
    enemy = get_random_enemy()
    print(f"You encounter a {enemy.name}!")
    input("Press Enter to begin the battle...")
    battle(player, enemy)


def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print(f"{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")

        player_attack = random.randint(1, player.attack)
        enemy_defense = random.randint(1, enemy.defense)
        damage_to_enemy = max(0, player_attack - enemy_defense)
        enemy.health -= damage_to_enemy
        print(f"{player.name} attacks the {enemy.name} for {damage_to_enemy} damage")

        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        enemy_attack = random.randint(1, enemy.attack)
        player_defense = random.randint(1, player.defense)
        damage_to_player = max(0, enemy_attack - player_defense)
        player.health -= damage_to_player
        print(f"{enemy.name} attacks {player.name} for {damage_to_player} damage")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            player.game_over = True
            break

    if player.health <= 0:
        print('You have been defeated!')


def get_random_enemy():
    return random.choice(enemy_types)


if __name__ == "__main__":
    main()