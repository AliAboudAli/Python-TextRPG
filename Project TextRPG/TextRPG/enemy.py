class Enemy:
    def __init__(self, name, health, attack, defense, stats, specialattack):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.stats = stats
        self.specialstats = specialattack


Enemy1 = Enemy("GarbageMonster", 100, 8, 3, 10, 10)