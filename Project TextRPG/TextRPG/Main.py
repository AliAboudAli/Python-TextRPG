from TextRPG.Player import Player as myPlayer
from TextRPG.Player import
import sys
import os
import time

def title_screen():
    os.system('cls')
    print('|------------------------------|')
    print('| Welcome to the Text RPG Game |')
    print('|------------------------------|')
    print('|            -Start-           |')
    print('|            -Help-            |')
    print('|            -Quit-            |')
    print('|------------------------------|')
    title_screen_selections()

def help_menu():
    print('|-------------------------------------------------|')
    print('| Welcome to the Text RPG Game                    |')
    print('|-------------------------------------------------|')
    print('| -Use up, down, left, right to move              |')
    print('| -Type your command to do something              |')
    print('| ^Look^ is the command to inspect something      |')
    print('|-------------------------------------------------|')
    title_screen_selections()

def title_screen_selections():
    option = input('> ')

    if option.lower() == 'start':
        start_game()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    else:
        while option not in ('start', 'help', 'quit'):
            print('Please input a valid command')
            option = input('> ')
            if option == 'start':
                start_game()
            elif option == 'help':
                help_menu()
            elif option == 'quit':
                sys.exit()

def start_game():
    print('start_game')
    maingame_loop()

def setup_game():
    os.system('clear')
    question1 = 'Are you ready to start the game?'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    title_screen()

def prompt():
    print("\n" + "================================")
    print("What would you do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown error has been detected by the action reviewer please try again!\n")
        action = input("> ")
        if action.lower() == 'quit':
            sys.exit()
        if action.lower() in ['move', 'go', 'travel', 'walk']:
            player_move(action.lower())
        if action.lower() in ['examine', 'inspect', 'interact', 'look']:
            player_examine(action.lower())

def maingame_loop():
    while not myPlayer.game_over:
        prompt()
def start_game():
    return

 title_screen()
#
# #to do list
# #################
# #define the enemies in the zonelist and attackable
# #NPC's
# #stats
# #Ascii en verhaal (AI)
# #special stats
