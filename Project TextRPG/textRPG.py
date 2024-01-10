import sys
import os
import time
import random

screen_width = 100

class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effect = []
        self.location = 'a1'
        self.game_over = False

class enemy:
    def __init__(self, hp,attack, defense, health):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.health = health



myPlayer = Player()
AEnemy = enemy(10, 10, 10, 10) #
#deze is een aanroeping van een function die moet je intialiseren bij elk def(methode) probeer ook classes als dat kan anders googlen

# Title Screen RPG
def title_screen_selections():
    option = input('> ')
    if option.lower() == 'play':
        start_game()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        sys.exit()
    else:
        while option not in ('play', 'help', 'quit'):
            print('Please input a valid command')
            option = input('> ')
            if option == 'play':
                start_game()
            elif option == 'help':
                help_menu()
            elif option == 'quit':
                sys.exit()


def title_screen():
    os.system('clear')
    print('|------------------------------|')
    print('| Welcome to the Text RPG Game |')
    print('|------------------------------|')
    print('|            -Start-           |')
    print('|            -Help-            |')
    print('|            -Quit-            |')
    print('|------------------------------|')
    title_screen_selections()
title_screen() #voorbeeld

def help_menu():
    print('|-------------------------------------------------|')
    print('| Welcome to the Text RPG Game                    |')
    print('|-------------------------------------------------|')
    print('| -Use up, down, left, right to move              |')
    print('| -Type your command to do something              |')
    print('| ^Look^ is the command to inspect something      |')
    print('|-------------------------------------------------|')
    title_screen_selections()
help_menu()

def start_game():
    maingame_loop()
start_game()

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.lower() + '#"')
    print('#' + zonemap[myPlayer.location][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(myPlayer.location))))
print_location()


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


def player_move(my_action):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'east']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'west']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print('You are already tired of this zone!')
    else:
        print('Ah, a new location to be explored')


def maingame_loop():
    while not myPlayer.game_over:
        prompt()


def setup_game():
    os.system('clear')
    question1 = 'Are you ready to start the game?'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)  # Fixed the syntax error here
    title_screen()


# Constants
ZONENAME = 'ZONENAME'
DESCRIPTION = 'DESCRIPTION'
EXAMINATION = 'EXAMINATION'
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
SOLVED = 'SOLVED'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}

zonemap = {
    'a1': {
        ZONENAME: "Engimal Town Entrance",
        DESCRIPTION: 'Entrance Engimal Town',
        EXAMINATION: 'Many houses are fested here but no one is here',
        SOLVED: False,
        UP: (' '),
        DOWN: ('b1'),
        LEFT: (' '),
        RIGHT: ('a2'),

        },
        'a2': {
            ZONENAME: "Engimal Market ",
            DESCRIPTION: 'This market is very big and is one off the biggest market in town',
            EXAMINATION: 'You walked in the market while people are selling and you see a sword at the blacksmith, so you decided to buy it but unfortunately it',
            SOLVED: False,
            UP: (' '),
            DOWN: ('b2'),
            LEFT: ('a1'),
            RIGHT: ('a3'),
        },
        'a3': {
            ZONENAME: "Engimal Town Hall",
            DESCRIPTION: 'it is a big town hall where all the planning is happening ',
            EXAMINATION: "while there is no one here you seeked for the entrance",
            SOLVED: False,
            UP: (''),
            DOWN: ('b3'),
            LEFT: ('a2'),
            RIGHT: ('a4'),
        },
        'a4': {
            ZONENAME: "Engimal Town Exit",
            DESCRIPTION: 'This is a long town hall while many statues of animals are with glowing eyes',
            EXAMINATION: 'While you walked in the hall you find a chest but you did not have the key, you walked forward continue towards the exit',
            SOLVED: False,
            UP: (' '),
            DOWN: ('b4'),
            LEFT: ('a3'),
            RIGHT: (' '),
        },
        'b1': {
            ZONENAME: "entrance forest hills",
            DESCRIPTION: 'You left Engimal Town on its way to your home',
            EXAMINATION: 'You see a deer running away from you so you decide to keepe on going',
            SOLVED: False,
            UP: ('a1'),
            DOWN: ('c1'),
            LEFT: (''),
            RIGHT: ('b2'),
        },
        'b2': {  ###Home direction set
            ZONENAME: "Home",
            DESCRIPTION: 'Here is where you live!',
            EXAMINATION: 'Your home seems to be empty',
            SOLVED: False,
            UP: ('a2'),
            DOWN: ('c2'),
            LEFT: ('b1'),
            RIGHT: ('b3'),
        },
        'b3': {
            ZONENAME: "Frogs forest",
            DESCRIPTION: 'big forest in the hearts of many species of frogs',
            EXAMINATION: 'You hear a lot of noises in the forest and you see a big toad coming towards you',
            SOLVED: False,
            UP: ('a3'),
            DOWN: ('c3'),
            LEFT: ('b2'),
            RIGHT: ('b4'),
        },
        'b4': {
            ZONENAME: 'Frogs Temple',
            DESCRIPTION: 'In the temple there a lots of traps',
            EXAMINATION: 'To go further you need to solve a puzzle to open the door',
            SOLVED: False,
            UP: ('a4'),
            DOWN: ('c4'),
            LEFT: ('b3'),
            RIGHT: (''),
        },
        'c1': {
            ZONENAME: "Mystic Forest",
            DESCRIPTION: 'A dense, mystical forest with towering trees.',
            EXAMINATION: 'You feel a strange energy in the air as you delve deeper into the forest.',
            SOLVED: False,
            UP: ('b1'),
            DOWN: ('d1'),
            LEFT: (' '),
            RIGHT: ('c2'),
        },

        'c2': {
            ZONENAME: "Ancient Ruins",
            DESCRIPTION: 'The ruins of an ancient civilization stand in silence.',
            EXAMINATION: 'You notice ancient inscriptions on the walls, hinting at a forgotten history.',
            SOLVED: False,
            UP: ('b2'),
            DOWN: ('d2'),
            LEFT: ('c1'),
            RIGHT: ('c3'),
        },

        'c3': {
            ZONENAME: "Cursed Swamp",
            DESCRIPTION: 'A gloomy swamp with eerie sounds in the distance.',
            EXAMINATION: 'The murky waters hide secrets, and you hear whispers in the wind.',
            SOLVED: False,
            UP: ('b3'),
            DOWN: ('d3'),
            LEFT: ('c2'),
            RIGHT: ('c4'),
        },

        'c4': {
            ZONENAME: "Haunted Mansion",
            DESCRIPTION: 'A foreboding mansion with shattered windows and creaking doors.',
            EXAMINATION: 'Darkness surrounds you as you step inside, and ghostly apparitions appear.',
            SOLVED: False,
            UP: ('b4'),
            DOWN: ('d4'),
            LEFT: ('c3'),
            RIGHT: (' '),
        },

        'd1': {
            ZONENAME: "Mystic Mountain",
            DESCRIPTION: 'A majestic mountain with breathtaking vistas.',
            EXAMINATION: 'You can see the entire world from this point, and a sense of wonder overcomes you.',
            SOLVED: False,
            UP: ('c1'),
            DOWN: (' '),
            LEFT: (' '),
            RIGHT: ('d2'),
        },

        'd2': {
            ZONENAME: "Crystal Caves",
            DESCRIPTION: 'Glistening caves filled with radiant crystals.',
            EXAMINATION: 'The crystals illuminate your path, but something stirs in the darkness.',
            SOLVED: False,
            UP: ('c2'),
            DOWN: (' '),
            LEFT: ('d1'),
            RIGHT: ('d3'),
        },

        'd3': {
            ZONENAME: "Fire Volcano",
            DESCRIPTION: 'An active volcano spewing molten lava andzxc ash into the sky.',
            EXAMINATION: 'The heat is unbearable, and the ground trembles beneath your feet.',
            SOLVED: False,
            UP: ('c3'),
            DOWN: (' '),
            LEFT: ('d2'),
            RIGHT: ('d4'),
        },

        'd4': {
            ZONENAME: "Dark Abyss",
            DESCRIPTION: 'A bottomless abyss with an unsettling void.',
            EXAMINATION: 'The darkness is impenetrable, and you hear whispers from the abyss.',
            SOLVED: False,
            UP: ('c4'),
            DOWN: (' '),
            LEFT: ('d3'),
            RIGHT: (' '),
        }
    }


def print_location():
    print('\n' + ('#' * (4 + len(Player.location))))
    print('#' + myPlayer.location.lower() + '#"')
    print('#' + zonemap[Player.position][DESCRIPTION] + '#')
    print('\n' + ('#' * (4 + len(Player.location))))


def prompt():
    print("\n" + "================================")
    print("What would you do?")
    action = input("> ")
    acceptable__actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable__actions:
        print("Unkown error has been dectected by the action reviewer please try again!\n")
        action = input("> ")
        if action.lower() == 'quit':
            sys.exit()
        if action.lower() == ['move', 'go', 'travel', 'walk']:
            player_move(action.lower())
        if action.lower() == ['Examine', 'inspect', 'interact', 'look']:
            player_examine(action.lower())


def player_move(myaction):
    ask = "Where would like to move to?\n"
    dest = input(ask)
    if dest in ['up' 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'east']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'west']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("/n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print('You are already tired for this zone!')
    else:
        print('Ah, a new location to be explored')




def setup_game():
    os.system('clear')
    question1 = 'Are you ready to start the game?'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0,10)
def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print(f"{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")

        #player attacks turn
        player_attack = random.randint(1, player.attack)
        enemy_defense = random.randint(1, enemy.defense)
        damage_to_enemy = max(0, player_attack - enemy_defense)
        enemy.health -= damage_to_enemy
        print(f"{player.name} attacks the {enemy.name} for {damage_to_enemy} damage")

        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break
        #Enemy attacks turn
        enemy_attack = random.randint(1, enemy.attack)
        player_defense = random.randint(1, player.defense)
        damage_to_player = max(0, enemy_attack - player_defense)
        player.health -= damage_to_player
        print(f"{enemy.name} attacks the {player.name} for {damage_to_player} damage")
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    player1 = player("Human", 100, 10, 5)
    enemy1 = enemy("GarbageMonster", 100, 8, 3)

    setup_game()
    battle(player1, enemy1)
def maingameloop():
    while myPlayer.gameover is False:
        prompt()
    def start_game():
        return

