import random

class Heralin:
    """Heralin, hikayenin kahramani. Saglik, savunma ve mana gibi ozelliklere sahip."""
    def _init_(self, name, health, defense, mana):
        # Karakterin isim, saglik, mana ve savunma degerlerini baslatalim.
        self.name = name
        self.health = health
        self.mana = mana
        self.defense = defense

    def attack(self, other):
        """Heralin'in saldiri metodu, mana tuketiyor ve rakibe zarar veriyor."""
        if self.mana >= 10:
            # Eger yeterli mana varsa, saldiri gucu hesaplanir ve dayak atar.
            attack_power = random.randint(50, 55)
            damage = attack_power - other.defense
            other.health -= damage
            self.mana -= 10
            print(f"{self.name}, {other.name}'a {attack_power} gucle saldirdi ve {damage} zarar verdi.")
        else:
            # Yeterli mana yoksa dinlenme metodunu cagiririz.
            print("Yeterli mana yok, mana kazanmak icin dinleniyor")
            self.rest()
        other.attack(self)

    def try_critical_attack(self, other):
        """Heralin'in elestirel saldiri denemesi, buyuk zarar verme sansi sunar."""
        if self.mana >= 20:
            # Eger yeterli mana varsa ve sans basariliysa, buyuk zarar verir.
            if random.random() < 0.42:
                attack_power = 40
                damage = attack_power
                other.health -= damage
                self.mana -= 20
                print(f"{self.name}, {other.name}'a {attack_power} gucle saldirdi ve {damage} zarar verdi.")
            else:
                # Elestirel saldiri basarisiz olursa.
                print("Heralin elestirel vurus denedi ama isabetsiz!")
                self.mana -= 20
        else:
            # Yeterli mana yoksa dinlenme metodunu cagiririz.
            print("Yeterli mana yok, mana kazanmak icin dinleniyor")
            self.rest()

    def rest(self):
        """Heralin'in mana yenilemek icin dinlenme metodu."""
        self.mana = min(self.mana + 30, 50)
        print(f"{self.name} dinlenerek 30 mana kazandi")

    def defend(self):
        """Heralin'in savunma arttirma metodu."""
        self.defense += 17
        self.mana -= 10
        print(f"{self.name} bir sonraki tur icin savunmasini arttirdi.")

class Morgara:
    """Morgara, hikayenin karsi karakteri. Saglik, guc ve savunma gibi ozelliklere sahiptir."""
    def _init_(self, name, health, power, defense, mana, rested):
        # Karakterin isim, saglik, guc, savunma, mana ve dinlenme durumu degerlerini baslatir.
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.mana = mana
        self.rested = rested

    def attack(self, other):
        """Morgara'nin saldiri metodu, rakibe zarar verir."""
        attack_power = random.randint(14, 20)
        damage = max(attack_power - other.defense, 0)
        other.health -= damage
        print(f"{self.name}, {other.name}'a {attack_power} gucle saldirdi ve {damage} zarar verdi.")

    def rest(self):
        """Morgara'nin saglik yenilemek icin dinlenme metodu baslar."""
        self.health = 120
        self.rested = True

def story():
    """Hikayeyi duraklatmak ve kullanicidan devam etmek icin giris yapmasini istemek icin kullanilan bir fonksiyon olusturalim."""
    print("----------------")
    input("Devam etmek icin Enter'a basin...")

def main(hero, enemy):
    """Oyun dongusunu calistiran ana fonksiyon."""
    print("Mistik Serathia Kronikleri'ne hos geldiniz!")
    story()

    # Oyun girisi ve hikaye ayarlari
    print("Serathia'nin mistik diyarinda, karanlik buyucu Morgara tarafindan tehdit ediliyor.")
    story()

    print("Heralin, cesur ve yetenekli bir kadin kahraman, Morgara'yi durdurmak icin tehlikeli bir yolculuga cikiyor.")
    story()

    # Savas dongusu
    while hero.health > 0 and enemy.health > 0:
        print(f"{hero.name}: Saglik {hero.health}, Mana {hero.mana}")
        print(f"{enemy.name}: Saglik {enemy.health}")
        print("Savas Secenekleri:")
        print("1. Saldır")
        print("2. Elestirel Saldırı Dene")
        print("3. Savun")
        print("4. Dinlen")
        choice = input("Seciminizi girin: ")

        # Savas secenekleri
        if choice == "1":
            hero.attack(enemy)
        elif choice == "2":
            hero.try_critical_attack(enemy)
        elif choice == "3":
            hero.defend()
        elif choice == "4":
            hero.rest()
        else:
            print("Gecersiz secim. Lutfen gecerli bir secenek secin.")
            continue

    # Oyun sonucu
    if hero.health > 0 and enemy.health <= 0:
        if not enemy.rested:
            enemy.rest()
            print("Morgara, kurnaz ve guclu, kacmak icin parlak bir isik yaratarak Heralin'i takip etmeye kararli birakir.")
            main(hero, enemy)
        else:
            print("Serathia, bir zamanlar karanlikta kalirken, yeniden sihirle aydinlanir. Heralin, umut ve birligin bir sembolu olarak ortaya cikar.")
            print("Tebrikler! Serathia'nin kahramani oldunuz ve Morgara'yi yendiniz!")
    else:
        print("Oyuncu oldu, oyunu kaybettiniz.")

# Karakter orneklerini olustur ve oyunu baslat
if __name__ == "_main_":
    hero = Heralin("Heralin", 100, 12, 50)
    enemy = Morgara("Morgara", 85, 20, 10, 10000, False)
    main(hero, enemy)
