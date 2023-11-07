import random

class Character:
    def __init__(self, name, health, power, defense, mana):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.mana = mana

    def attack(self, enemy):
        if self.mana >= 10:
            self.mana -= 10
            attack_power = random.randint(int(self.power * 0.7), int(self.power))
            enemy_damage = max(attack_power - enemy.defense, 0)
            enemy.health -= enemy_damage
            return attack_power, enemy_damage
        else:
            print("Not enough mana for an attack! Resting to regain mana...")
            self.rest()
            return 0, 0

    def increase_defense(self):
        if self.mana >= 10:
            self.mana -= 10
            self.defense += 5
            return True
        else:
            print("Not enough mana to increase defense!")
            return False

    def critical_hit(self, enemy):
        if self.mana >= 20:
            self.mana -= 20
            if random.random() <= 0.42:
                critical_power = self.power * 2
                enemy_damage = max(critical_power - enemy.defense, 0)
                enemy.health -= enemy_damage
                return critical_power, enemy_damage
            else:
                print(f"{self.name} attempted a critical hit but missed!")
                self.rest()  # Not enough mana, rest to regain mana.
                return 0, 0
        else:
            print("Not enough mana for a critical hit! Resting to regain mana...")
            self.rest()
            return 0, 0

    def rest(self):
        self.mana = min(self.mana + 30, 50)
        print(f"{self.name} rested and regained mana.")

def print_battle_options():
    print("Battle Options:")
    print("1. Attack")
    print("2. Try Critical Attack")
    print("3. Defend")
    print("4. Rest")

def print_character_status(player, enemy):
    print("*****************************")
    print(f"{player.name}: Health {player.health}, Mana {player.mana}")
    print(f"{enemy.name}: Health {enemy.health}, Mana {enemy.mana}")
    print("*****************************")

def main():
    print("Welcome to the Mystic Odyssey: Chronicles of Serathia!")
    player = Character("Heralin", 100, 25, 12, 50)
    enemy = Character("Morgara", 85, 20, 10, 100)
    story_part = 0

    while player.health > 0 and story_part < 10:
        input("Press Enter to continue...")
        print("*****************************")
        print_story(story_part)
        print("*****************************")
        story_part += 1
        count = 0
        if story_part == 8 and enemy.health <= 0 and count == 0:
            enemy.health = 120
            enemy.power = 21
            count += 1
            continue

        if story_part in [4, 7, 9]:
            while player.health > 0 and enemy.health > 0:
                print_character_status(player, enemy)
                print_battle_options()
                choice = input("Enter your choice: \n")

                if choice == "1":
                    attack_power, enemy_damage = player.attack(enemy)
                    print(f"{player.name} attacked the enemy with {attack_power} power, dealt {enemy_damage} damage.")
                elif choice == "2":
                    critical_power, enemy_damage = player.critical_hit(enemy)
                    if critical_power > 0:
                        print(f"{player.name} performed a critical hit, dealt {enemy_damage} damage to the enemy.")
                    else:
                        print(f"{player.name} attempted a critical hit but missed!")
                elif choice == "3":
                    if player.increase_defense():
                        print(f"{player.name} increased defense for the next round.")
                    else:
                        print("Not enough mana to defend!")
                elif choice == "4":
                    player.rest()
                else:
                    print("Invalid choice. Please choose a valid option.")
                    continue

                if enemy.health > 0:
                    enemy_power, player_damage = enemy.attack(player)
                    print(f"{enemy.name} attacked {player.name} with {enemy_power} power, dealt {player_damage} damage.")

    print_game_result(player.health)

def print_story(story_part):
    story = [
        "In the mystical realm of Serathia, the land is threatened by the dark sorceress Morgara.",
        "Heralin, a courageous and skilled female hero, embarks on a perilous journey to stop Morgara.",
        "Guided by ancient prophecies, Heralin seeks the counsel of wise sages and hones her skills.",
        "Armed with a powerful weapon, Heralin confronts Morgara in a fierce battle.",
        "Morgara, cunning and formidable, creates a blinding light to escape, leaving Heralin determined to pursue.",
        "Morgara grows stronger, summoning ancient creatures and forging dark alliances.",
        "Heralin, undeterred, faces every obstacle and pursues Morgara relentlessly.",
        "The day of destiny arrives. Heralin stands at the gates of Morgara's fortress, ready for the final confrontation.",
        "In the epic battle that ensues, Heralin fights valiantly, striking down Morgara and ending her reign of terror.",
        "Serathia, once shrouded in darkness, now basks in the glow of renewed magic. Heralin emerges as a symbol of hope and unity."
    ]
    print(story[story_part])

def print_game_result(player_health):
    if player_health <= 0:
        print("Player has died, you lost the game!")
    else:
        print("Congratulations! You survived the challenges and became the hero of Serathia, defeating Morgara!")

if __name__ == "__main__":
    main()



