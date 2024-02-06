from Player import Player
from weapon import weapon

class store:
    def __init__(self):
        self.inventory = {
            'Sword': weapon('Sword', 'A basic sword', 20, 50),
            'Axe': weapon('Axe', 'A heavy axe', 25, 70),
            'Bow': weapon('Bow', 'A ranged weapon', 18, 60),
            'Staff': weapon('Staff', 'A magical staff', 22, 80),
        }

    def buy(self, item_name, player):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if player.gold >= item.price:
                player.gold -= item.price
                player.inventory.append(item)
                print(f"You bought a {item.name} for {item.price} gold.")
            else:
                print("You don't have enough gold to buy that item.")
        else:
            print("That item is not available in the store.")
