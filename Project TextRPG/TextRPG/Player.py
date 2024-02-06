class Player:
    def __init__(self, zonemap):
        self.name = ''
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.magic_points = 20
        self.special_skill_cooldown = 0
        self.location = 'a1'
        self.game_over = False
        self.level = 1
        self.experience = 0
        self.max_health = 100
        self.max_magic_points = 20
        self.gold = 100  # Starting gold
        self.inventory = []
        self.luck = 0  # Luck stat
        self.lure = 0  # Lure stat
        self.zonemap = zonemap


    def level_up(self):
        self.level += 1
        self.attack += 5
        self.defense += 3
        self.max_health += 20
        self.max_magic_points += 10
        self.health = self.max_health
        self.magic_points = self.max_magic_points
        print(f"Congratulations! You've reached level {self.level}.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"You gained {amount} experience points.")
        if self.experience >= self.level * 100:  # Level up condition
            self.level_up()

    def show_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item.name}: {item.description}")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Magic Points: {self.magic_points}/{self.max_magic_points}")
        print(f"Gold: {self.gold}")
        print(f"Luck: {self.luck}")
        print(f"Lure: {self.lure}")

    def use_special_ability(self, target):
        raise NotImplementedError("Subclasses must implement use_special_ability method")

    def special_attack(self, target):
        raise NotImplementedError("Subclasses must implement special_attack method")


class Wizard(Player):
    def __init__(self, zonemap):  # Add zonemap argument
        super().__init__(zonemap)  # Pass zonemap to superclass constructor
        self.name = 'Wizard'  # Set the name of the Wizard player
        self.special_attack_name = 'Fireball'
        self.special_attack_damage = 30  # Base damage of Fireball
        self.special_attack_cooldown = 15  # Cooldown in seconds



class Orc(Player):
    def __init__(self, zonemap):  # Add zonemap argument
        super().__init__(zonemap)  # Pass zonemap to superclass constructor
        self.name = 'Orc'  # Set the name of the Orc player
        self.special_attack_name = 'Rage'
        self.special_attack_damage = 20  # Base damage of Rage
        self.special_attack_cooldown = 15  # Cooldown in seconds


class Human(Player):
    def __init__(self, zonemap):  # Add zonemap argument
        super().__init__(zonemap)  # Pass zonemap to superclass constructor
        self.name = 'Human'  # Set the name of the Human player
        self.special_attack_name = 'Technical Power'
        self.special_attack_damage = 25  # Base damage of Technical Power
        self.special_attack_cooldown = 15  # Cooldown in seconds

