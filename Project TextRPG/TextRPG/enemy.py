class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = 100
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

# Define different enemy types
enemy_types = [
    Enemy("GarbageMonster", 100, 8, 3),
    Enemy("Shadow Assassin", 80, 12, 5),
    Enemy("Fire Witch", 120, 10, 8),
    Enemy("Ice Golem", 150, 15, 10),
    Enemy("Ancient Dragon", 200, 20, 15),
    Enemy("Giant Spider", 180, 18, 20)
]