######### TOPTANCI ###########
frt = ["Elma", "Armut", "Erik", "İncir", "Karpuz"]
veg = ["Domates", "Biber", "Patlıcan", "Salatalık", "Brokoli"]
#########  MANAV   ###########
gg_frt = []
gg_veg = []
# not in  - .lower - .capitalize - if not - enumerate
while True:
    frt_veg = input("Hoşgeldiniz, Meyve mi almak istersiniz, Sebze mi? (Meyve-Sebze): ").lower()

    if frt_veg not in ["meyve", "sebze"]:
        print("İstenilen formata uygun giriş yapınız: Sebze - Meyve")
        continue

    elif frt_veg == "meyve":
        print(f"Halde bulunan meyveler: {frt}")
        frt_chose = input("Hangi meyveyi almak istiyorsunuz? ").capitalize()

        if frt_chose not in frt:
            print("Elimde olmayan bir meyveyi isteyemezsiniz")
            continue

        frt_kg = int(input(f"{frt_chose}'dan kaç kilo almak istiyorsunuz? "))
        gg_frt.append((frt_chose, frt_kg))
        print(f"{frt_kg} kilo {frt_chose} aldınız.")

    elif frt_veg == "sebze":
        print(f"Halde bulunan sebzeler: {veg}")
        veg_chose = input("Hangi sebzeyi almak istiyorsunuz? ").capitalize()

        if veg_chose not in veg:
            print("Elimde olmayan bir sebzeyi isteyemezsiniz")
            continue

        veg_kg = int(input(f"{veg_chose}'dan kaç kilo almak istiyorsunuz? "))
        gg_veg.append((veg_chose, veg_kg))
        print(f"{veg_kg} kilo {veg_chose} aldınız.")

    Continue = input("Başka bir arzunuz var mı? (Evet - Hayır): ").lower()
    if Continue == "hayır":
        print("İyi günler, --> Manav kısmına geçiyorum")
        break

####  MANAV  ####

while True:
    frt_veg = input("Meyve mi almak istersiniz, Sebze mi? (Meyve-Sebze): ").lower()

    if frt_veg not in ["meyve", "sebze"]:
        print("İstenilen formata uygun giriş yapınız: Meyve - Sebze")
        continue

    if frt_veg == "meyve":
        if not gg_frt:
            print("Manavda meyve kalmamıştır!")
            continue

        print(f"Manavda bulunan meyveler: {gg_frt}")
        frt_chose = input("Hangi meyveyi almak istiyorsunuz? ").capitalize()
        for index, (fruit, kg) in enumerate(gg_frt): #["Elma",10,"Armut",20]
            if fruit == frt_chose:
                break
        else:
            print("Seçilen meyve manavda yok.")
            continue

        frt_kg = int(input(f"{frt_chose}'dan kaç kilo almak istiyorsunuz? "))

        if frt_kg > gg_frt[index][1]:
            print(f"Yeterli stok yok. Mevcut stok: {gg_frt[index][1]} kilo.")
        else:
            kalan_kg = gg_frt[index][1] - frt_kg
            if kalan_kg > 0:
                gg_frt[index] = (gg_frt[index][0], kalan_kg)
            else:
                gg_frt.pop(index)
            print(f"{frt_kg} kilo {frt_chose} aldınız.")

    elif frt_veg == "sebze":
        if not gg_veg:
            print("Manavda sebze kalmamıştır!")
            continue

        print(f"Manavda bulunan sebzeler: {gg_veg}")
        veg_chose = input("Hangi sebzeyi almak istiyorsunuz? ").capitalize()

        for index, (veg, kg) in enumerate(gg_veg):
            if veg == veg_chose:
                break
        else:
            print("Seçilen sebze manavda yok.")
            continue

        veg_kg = int(input(f"{veg_chose}'dan kaç kilo almak istiyorsunuz? "))

        if veg_kg > gg_veg[index][1]:
            print(f"Yeterli stok yok. Mevcut stok: {gg_veg[index][1]} kilo.")
        else:
            kalan_kg = gg_veg[index][1] - veg_kg
            if kalan_kg > 0:
                gg_veg[index] = (gg_veg[index][0], kalan_kg)
            else:
                gg_veg.pop(index)
            print(f"{veg_kg} kilo {veg_chose} aldınız.")

    devam = input("Başka bir arzunuz var mı? (Evet - Hayır): ").lower()
    if devam == "hayır":
        print("Afiyet olsun!")
        break