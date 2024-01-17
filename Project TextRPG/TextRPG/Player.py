class Player:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.location = 'a1'
        self.game_over = False
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
        print('You are already tired for this zone!')
    else:
        print('Ah, a new location to be explored')