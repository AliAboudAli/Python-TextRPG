import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100

#Player#
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effect = []

        Player = player()

    #Title Screen RPG#
    def title_screen_selections():
        option = input("> ")
        if option_lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
            while option.lower() not in ("play", "help", "quit"):
                prin("Please input a valid command")
                option = input ( "> " )
                if option_lower ( ) == ("play") :
                    start_game ( )
                elif option.lower ( ) == ("help") :
                    help_menu ( )
                elif option.lower ( ) == ("quit") :
                    sys.exit ( )

def title_screen ():
    os.system("clear")
    print("--------------------------------")
    print("| Welcome to the Text RPG Game |")
    print("--------------------------------")
    print("|            -Start-           |")
    print("|            -Help-            |")
    print("|            -Quit-            |")
    print("--------------------------------")
    title_screen_selections()

def help_menu():
    print("--------------------------------")
    print("| Welcome to the Text RPG Game |")
    print("--------------------------------")
    print("|                      |")
    print("|                        |")
    print("|                      |")
    print("--------------------------------")
    title_screen_selections()

if __name__ == "__main__":
    title_screen()