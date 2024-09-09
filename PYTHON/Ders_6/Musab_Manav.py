RED = "\033[91m"
RESET = "\033[0m" #COLOR

# Meyve ve sebzeler ile stokları
meyve_stok = {
    "MUZ": 5000,
    "ELMA": 5000,
    "ERİK": 5000,
    "KARPUZ": 5000,
    "KAVUN": 5000
}
sebze_stok = {
    "DOMATES": 5000,
    "HIYAR(GSLİLER)": 5000,
    "KIVIRCIK": 5000,
    "HAVUÇ": 5000,
    "LİMON": 5000
}

# Kullanıcının seçtiği ürünler ve kiloları
manavList = []

print("Diken Hal'e HOŞ GELDİNİZ")
while True:  # Ana döngü
    manavListSecim = input("Meyve için M, sebze için S'yi seçebilirsiniz:").upper()

    if manavListSecim != "M" and manavListSecim != "S":
        print(f"{RED}Lütfen sadece M ya da S harfini kullanınız!!!{RESET}")
        continue

    if manavListSecim == "M":
        print("Meyve stokları:", meyve_stok)
    elif manavListSecim == "S":
        print("Sebze stokları:", sebze_stok)

    while True:  # Ürün seçimi döngüsü
        meyveSecim = input("İstediğiniz MEYVEYİ/SEBZEYİ seçiniz:").upper()

        if meyveSecim not in meyve_stok and meyveSecim not in sebze_stok:
            print(f"{RED}Lütfen Sadece Listedeki Ürünleri Giriniz {RESET}")
            continue
        break

    while True:  # Kilo alma döngüsü
        if manavListSecim == "M":
            current_stock = meyve_stok[meyveSecim]
        else:
            current_stock = sebze_stok[meyveSecim]

        print(f"{meyveSecim} için kalan stok: {current_stock} kg")

        try:
            meyveKilo = int(input("Kaç kilo istersiniz:"))
        except ValueError:
            print(f"{RED}Lütfen sadece RAKAM giriniz!{RESET}")
            continue

        if meyveKilo < 1 or meyveKilo > current_stock:
            print(f"{RED}Lütfen düzgün kilo giriniz!!!{RESET}")
            continue

        # Stokları güncelleme ve seçilen ürünleri listeye ekleme
        if manavListSecim == "M":
            meyve_stok[meyveSecim] -= meyveKilo
            manavList.append((meyveSecim, meyveKilo))
        else:
            sebze_stok[meyveSecim] -= meyveKilo
            manavList.append((meyveSecim, meyveKilo))

        print(f"{meyveKilo} kg {meyveSecim} aldınız. Kalan stok: {current_stock - meyveKilo} kg")

        if (manavListSecim == "M" and meyve_stok[meyveSecim] == 0) or (manavListSecim == "S" and sebze_stok[meyveSecim] == 0):
            print(f"{meyveSecim} stoğu bitti!")
            break

        arzu = input("Başka bir arzunuz varsa E'ye basınız, çıkmak için herhangi bir tuşa basabilirsiniz:").upper()
        if arzu == "E":
            break
        else:
            print("İyi günler :)")
            break

    # İkinci aşama
    print("BeşKardeşler Markete HOŞ GELDİNİZ")
    print(f"Seçtiğiniz ürünler ve kilolar: {manavList}")
    break  # Bu break, ana döngüyü bitirir ve programı sonlandırır.