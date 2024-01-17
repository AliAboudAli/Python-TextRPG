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