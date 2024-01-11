import random

bakiye = 1000

def kart_ver():
    # Rastgele bir kart döndürsün
    return random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

def skor_hesapla(kartlar):
    # Kartların skorunu hesaplattım. As 11, resimli kartlar 10, diğerleri kendi değerleri kadar puan alıyor.
    skor = sum([11 if kart == "A" else 10 if kart in ["K", "Q", "J"] else int(kart) for kart in kartlar])
    # Eğer skor 21'den fazlaysa ve elde As varsa, skordan 10 çıkarılır. As 1 ya da 11 olarak sayılır. Az patlamadık illet yüzünden.
    if "A" in kartlar and skor > 21:
        skor -= 10
    return skor

def karsilastir(kullanici_skoru, bilgisayar_skoru):
    # Skorları karşılaştırır ve oyunun kim kazandığını belirtir..
    if kullanici_skoru == bilgisayar_skoru:
        return "Berabere!"
    elif kullanici_skoru > 21:
        return "21'i gectiniz. Kaybettiniz!"
    elif bilgisayar_skoru > 21:
        return "Rakip 21'i gecti. Kazandiniz!"
    elif kullanici_skoru > bilgisayar_skoru:
        return "Kazandiniz!"
    else:
        return "Kaybettiniz!"

def bakiye_goster():
    # Mevcut kasa değerini bize versin.
    print(f"Mevcut bakiyeniz: ${bakiye}")

def oyun_oyna():
    global bakiye
    bahis = int(input("Bahis miktarinizi girin: $"))

    if bahis > bakiye:
        print("Bahis miktari bakiyenizi asiyor.")
        print(f"Mevcut bakiyeniz: ${bakiye}")
        return

    kullanici_kartlari = [kart_ver(), kart_ver()]
    bilgisayar_kartlari = [kart_ver(), kart_ver()]
    oyun_sonu = False

    while not oyun_sonu:
        kullanici_skoru = skor_hesapla(kullanici_kartlari)
        bilgisayar_skoru = skor_hesapla(bilgisayar_kartlari)
        print(f"Kartlariniz: {kullanici_kartlari}, mevcut skor: {kullanici_skoru}")
        print(f"Rakibin ilk karti: {bilgisayar_kartlari[0]}")
        print("----------")

        if kullanici_skoru == 0 or bilgisayar_skoru == 0 or kullanici_skoru > 21:
            oyun_sonu = True
        else:
            devam_et = input("Baska kart cekmek icin 'e', durmak icin 'h' yazin: ").lower()
            if devam_et == 'e':
                kullanici_kartlari.append(kart_ver())
            else:
                oyun_sonu = True

    while bilgisayar_skoru != 0 and bilgisayar_skoru < 17:
        bilgisayar_kartlari.append(kart_ver())
        bilgisayar_skoru = skor_hesapla(bilgisayar_kartlari)

    print(f"Sizin final eliniz: {kullanici_kartlari}, final skor: {kullanici_skoru}")
    print(f"Rakibin final eli: {bilgisayar_kartlari}, final skor: {bilgisayar_skoru}")
    print("----------")
    sonuc = karsilastir(kullanici_skoru, bilgisayar_skoru)
    print(sonuc)
    print("----------")

    if "Kazandiniz" in sonuc:
        bakiye += bahis
        print(f"${bahis} kazandiniz! Mevcut bakiyeniz: ${bakiye}")
    elif "Kaybettiniz" in sonuc:
        bakiye -= bahis
        print(f"${bahis} kaybettiniz. Mevcut bakiyeniz: ${bakiye}")

while True:
    print("\nBlackjack'e Hos Geldiniz!")
    print("1. Oyunu Baslat")
    print("2. Bakiye Göster")
    print("3. Cikis Yap")
    print("----------")

    secim = input("Seçiminizi girin (1/2/3): ")

    if secim == "1":
        oyun_oyna()
    elif secim == "2":
        bakiye_goster()
    elif secim == "3":
        print("Oynadiginiz için tesekkürler! Hosca kalin!")
        break
    else:
        print("Gecersiz secim. Lutfen 1, 2 veya 3 girin.")

#oyun biterrr......ocak yıkmaya devam:)