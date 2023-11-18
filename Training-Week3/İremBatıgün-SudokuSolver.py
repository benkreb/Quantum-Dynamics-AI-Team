import random

class Heralin:
    def __init__(self, name, health, defense, mana):
        self.name = name
        self.health = health
        self.mana = mana
        self.defense = defense
# When Heralin attacks her attributes change such as mana, power, health
    def attack(self, other):
        if self.mana >= 10:
            current_power = random.randint(50,55)
            damage=current_power-other.defense
            other.health -= damage
            self.mana -= 10
            print(f"{self.name} attacked {other.name} with {current_power} power, dealing {damage} damage.")
        else:
            print("Not enough mana, resting to gain mana")
            self.rest()
        other.attack(self)
      
  # Critical attack requires 20 mana. It has a 42% chance of dealing 40 damage
    def try_critical_attack(self, other):
      if self.mana >= 20:
        
        if random.random() < 0.42:
            current_power = 40          
            damage=current_power
            other.health -= damage
            self.mana-=20
            print(f"{self.name} attacked {other.name} with {current_power} power, dealing {damage} damage.")
        else:
          print("Heralin attempted a critical hit but missed!")
          self.mana-=20
      else:
        print("Not enough mana, resting to gain mana")
        self.rest()
    # Heralin can rest to gain mana
    def rest(self):
        if self.mana + 30 <= 50:
            self.mana += 30
        else:
            self.mana = 50
        print(f"{self.name} rests and gains 30 mana")
    # Heralin can increase her defense 
    def defend(self):
        self.defense += 17
        self.mana -= 10
        print(f"{self.name} Heralin increased defense for the next round.")


class Morgara:                      
    def __init__(self, name, health, power ,defense,mana,rested):
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.mana = mana
        self.rested = rested
    # When Morgara attacks her attributes change such as mana, power, health
    def attack(self, other):
        current_power = random.randint(14,20)
        damage = current_power - other.defense
        if damage < 0:
          damage = 0
        other.health -= damage
        print(f"{self.name} attacked {other.name} with {current_power} power, dealing {damage} damage.")

    #When Morgara rest, her health increases to 120
    def rest(self):
        self.health=120
        self.rested = True
      
def story():      
  print("----------------")
  input("Press Enter to continue...")

def main(Heralin,Morgara):
    print("Welcome to the Mystic Odyssey: Chronicles of Serathia!")
    story()

    print("In the mystical realm of Serathia, the land is threatened by the dark sorceress Morgara.")
    story()
   

    
    print("Heralin, a courageous and skilled female hero, embarks on a perilous journey to stop Morgara.")
    story()

    print("Guided by ancient prophecies, Heralin seeks the counsel of wise sages and hones her skills.")
    story()

    print("Armed with a powerful weapon, Heralin confronts Morgara in a fierce battle.")
    story()
  
  # while loop to keep the game going until Morgara is defeated
    while hero.health > 0 and enemy.health > 0:
        print(f"{hero.name}: Health {hero.health}, Mana {hero.mana}")
        print(f"{enemy.name}: Health {enemy.health}")
        print("Battle Options:")
        print("1. Attack")
        print("2. Try Critical Attack")
        print("3. Defend")
        print("4. Rest")
        choice = input("Enter your choice: ")

        if choice == "1":
            hero.attack(enemy)
        elif choice == "2":
            hero.try_critical_attack(enemy)
            enemy.attack(hero)
        elif choice == "3":
            hero.defend()
            enemy.attack(hero)
        elif choice == "4":
            hero.rest()
            enemy.attack(hero)
        else:
            print("Invalid choice. Please choose a valid option.")
            continue
# if Morgara is defeated, let  her rest and play one more time
    if hero.health > 0 and enemy.health <= 0:      
      if  enemy.rested == False:
        enemy.rest()
        print("Morgara, cunning and formidable, creates a blinding light to escape, leaving Heralin determined to pursue.")
        story()
        print("Morgara grows stronger, summoning ancient creatures and forging dark alliances.")
        story()
        print("Heralin, undeterred, faces every obstacle and pursues Morgara relentlessly.")
        story()
        print("The day of destiny arrives. Heralin stands at the gates of Morgara's fortress, ready for the final confrontation.")
        story()
        print("In the epic battle that ensues, Heralin fights valiantly, striking down Morgara and ending her reign of terror.")       
        print("----------------\n--------------")
        main(Heralin,Morgara)
        

      else:
        story()
        print("Serathia, once shrouded in darkness, now basks in the glow of renewed magic. Heralin emerges as a symbol of hope and unity.")
        print("----------------")
        print("Congratulations! You became the hero of Serathia and defeated Morgara!")
      
    else:
        print("Player has died, you lost the game.")
      
 #creating objects and calling the main function         
if __name__ == "__main__":
    hero = Heralin("Heralin", 100, 12, 50)
    enemy = Morgara("Morgara", 85, 20,10, 10000,False)

    main(Heralin,Morgara)
