class Location:
    def __init__(self, name, description, shop=None):
        self.name = name
        self.description = description
        self.shop = shop


def player_move(player, zonemap, location_key):
    print('Available locations:')
    for location_key in player.zonemap.keys():
        print(player.zonemap[location_key]['ZONENAME'])

    ask = "Where would you like to move to?\n"
    dest = input(ask).lower()

    if dest in ['up', 'north']:
        direction = player.UP
    elif dest in ['left', 'west']:
        direction = player.LEFT
    elif dest in ['right', 'east']:
        direction = player.RIGHT
    elif dest in ['down', 'south']:
        direction = player.DOWN
    else:
        print("Invalid direction. Please choose a valid direction (up, down, left, right).")
        return

    destination = player.zonemap[player.location][direction]
    movement_handler(player, destination)


def movement_handler(player, destination):
    if destination:
        print("\n" + "You have moved to " + destination + ".")
        player.location = destination
        print_location(player)
        if player.zonemap[player.location]['shop']:
            visit_shop(player)
    else:
        print("You cannot move in that direction.")


def visit_shop(player):
    current_location = player.zonemap[player.location]
    shop_inventory = current_location['shop']
    print("Welcome to the shop!")
    print("Here is what's available:")
    for item in shop_inventory:
        print(f"{item}: {shop_inventory[item]['price']} gold")
    print("What would you like to buy? (Type 'exit' to leave)")
    while True:
        choice = input("Enter the name of the item: ").lower()
        if choice == 'exit':
            print("Thanks for visiting!")
            break
        if choice in shop_inventory:
            if player.gold >= shop_inventory[choice]['price']:
                player.gold -= shop_inventory[choice]['price']
                player.inventory.append(choice)
                print(f"You bought {choice} for {shop_inventory[choice]['price']} gold.")
            else:
                print("You don't have enough gold to buy that!")
        else:
            print("That item is not available in this shop!")


def print_location(player):
    print('\n' + ('#' * (4 + len(player.location))))
    print('#' + player.location.lower() + '#')
    print('#' + player.zonemap[player.location]['DESCRIPTION'] + '#')
    print('\n' + ('#' * (4 + len(player.location))))


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
                 'd1': False, 'd2': False, 'd3': False, 'd4': False }
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
        'shop': {'sword': {'price': 50}, 'potion': {'price': 10}}
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
        'shop': {'sword': {'price': 50}, 'potion': {'price': 10}}
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

    }
}
