stokmeyve = {
    "Elma": 60,
    "Armut": 60,
    "Muz": 60,
    "Portakal": 60,
    "Üzüm": 60
}

stoksebze = {
    "Havuç": 60,
    "Patates": 60,
    "Domates": 60,
    "Salatalık": 60,
    "Biber": 60
}

while True:
    print("Müşteriye ne sunmak istersiniz?")
    print("1. Meyve")
    print("2. Sebze")
    secim = input("Lütfen seçim yapın (1 veya 2): ")

    if secim == "1":
        print("Meyve seçenekleri:")
        i = 0
        for meyve in stokmeyve:
            print(f"{i}. {meyve} - Mevcut stok: {stokmeyve[meyve]} kilo")
            i += 1

        secim = int(input("Hangi meyveyi istersiniz (0-4): "))

        meyve_listesi = list(stokmeyve.keys())

        if 0 <= secim < len(meyve_listesi):
            secilenmeyve = meyve_listesi[secim]
            print(f"{secilenmeyve} seçtiniz.")

            print(f"Mevcut stokta {stokmeyve[secilenmeyve]} kilo {secilenmeyve} var.")

            while True:
                miktar = int(input(f"{secilenmeyve} için kaç kilo istersiniz: "))

                if miktar > stokmeyve[secilenmeyve]:
                    print(f"Maalesef stokta sadece {stokmeyve[secilenmeyve]} kilo {secilenmeyve} var.")
                else:
                    break

            stokmeyve[secilenmeyve] -= miktar
            print(f"{secilenmeyve} : {miktar} kilo")
            print("Emin toptancıyı tercih ettiğiniz için teşekkürler!")

        else:
            print("Geçersiz seçim.")

    elif secim == "2":
        print("Sebze seçenekleri:")
        i = 0
        for sebze in stoksebze:
            print(f"{i}. {sebze} - Mevcut stok: {stoksebze[sebze]} kilo")
            i += 1

        secim = int(input("Hangi sebzeyi istersiniz (0-4): "))

        sebze_listesi = list(stoksebze.keys())

        if 0 <= secim < len(sebze_listesi):
            secilensebze = sebze_listesi[secim]
            print(f"{secilensebze} seçtiniz.")

            print(f"Mevcut stokta {stoksebze[secilensebze]} kilo {secilensebze} var.")

            while True:
                miktar = int(input(f"{secilensebze} için kaç kilo istersiniz: "))

                if miktar > stoksebze[secilensebze]:
                    print(f"Maalesef stokta sadece {stoksebze[secilensebze]} kilo {secilensebze} var.")
                else:
                    break

            stoksebze[secilensebze] -= miktar
            print(f"{secilensebze} : {miktar} kilo")
            print("Emin toptancıyı tercih ettiğiniz için teşekkürler!")

        else:
            print("Geçersiz seçim.")

    else:
        print("Geçersiz seçim.")

    devam = input("Başka bir şey almak ister misiniz? (evet/hayır): ")

    if devam == "hayır":
        print("Alışverişinizi tamamladınız.")
        break
    elif devam != "evet":
        print("Geçersiz cevap. Lütfen 'evet' veya 'hayır' girin.")
