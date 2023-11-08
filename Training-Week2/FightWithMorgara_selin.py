import random

class Character:
    def __init__(self, name, health, power, defense, mana):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        self.mana = mana

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, power=25, defense=12, mana=50)

    def attack(self, enemy):
        damage = random.randint(self.power // 2, self.power)
        enemy.take_damage(damage)
        return damage

    def critical_attack(self, enemy):
        if self.mana >= 20:
            self.mana -= 20
            if random.random() < 0.42:
                damage = random.randint(self.power, self.power * 2)
                enemy.take_damage(damage)
                return damage
            else:
                return 0
        else:
            print("Not enough mana for a Critical Attack.")
            return 0

    def defend(self):
        self.defense += 5

    def rest(self):
        self.mana = min(50, self.mana + 10)

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=85, power=20, defense=10, mana=10000)

    def attack(self, player):
        damage = random.randint(self.power // 2, self.power)
        player.take_damage(damage)
        return damage

class Game:
    def __init__(self):
        self.player = Player("Heralin")
        self.enemy = Enemy("Morgara")
        self.story_phases = 10
        self.current_phase = 1

    def start(self):
        print("Welcome to Mystic Odyssey: Chronicles of Serathia!")
        input("Press Enter to begin your adventure...")

        while self.player.health > 0 and self.enemy.health > 0 and self.current_phase <= self.story_phases:
            print(f"\n--- Phase {self.current_phase} ---")
            input("Press Enter to continue...")
            self.battle()
            self.current_phase += 1

        if self.enemy.health <= 0:
            print("Congratulations! You have defeated Morgara and saved Serathia!")
        else:
            print("Game over. Morgara has defeated you.")

    def battle(self):
        print(f"{self.player.name}'s Stats: Health - {self.player.health}, Mana - {self.player.mana}")
        print(f"{self.enemy.name}'s Stats: Health - {self.enemy.health}, Mana - {self.enemy.mana}")

        action = input("Choose an action (attack/critical/defend/rest): ").lower()

        if action == "attack":
            damage = self.player.attack(self.enemy)
        elif action == "critical":
            damage = self.player.critical_attack(self.enemy)
        elif action == "defend":
            self.player.defend()
            damage = 0
        elif action == "rest":
            self.player.rest()
            damage = 0
        else:
            print("Invalid action. Choose from attack, critical, defend, or rest.")
            return

        enemy_damage = self.enemy.attack(self.player)

        print(f"You dealt {damage} damage to {self.enemy.name}.")
        print(f"{self.enemy.name} dealt {enemy_damage} damage to {self.player.name}.")

    def print_story(self, phase):
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
        print(story[phase - 1])

      

if __name__ == "__main__":
    game = Game()
    game.start()
