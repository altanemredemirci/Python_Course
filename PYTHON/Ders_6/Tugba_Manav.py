meyve_listesi = ["elma","armut","muz","portakal","çilek"]
sebze_listesi = ["patates","soğan","havuç","lahana","marul"]

# meyvelerin kilo stoklarını eşleştir ?
meyve_stok = [100,100,100,100,100]
sebze_stok= [100,100,100,100,100]
güncel_meyve_stok = []
güncel_sebze_stok = []
manav_alınacak_meyveler = []
manav_alınacak_sebzeler = []
müsteri_alınacak_meyveler = []
müsteri_alınacak_sebzeler = []
müsteri_meyve_alısverisi = []
müsteri_sebze_alısverisi = []
def liste_yazdir(liste):
    for eleman in liste:
        print((eleman))

def hal_ile_etkilesim():
    while True:
        print("TOPTANCI-MANAV")
        tercih = input("meyve mi sebze mi (m/s):")
        if tercih == "m":
            print("\nmeyve_listesi")
            liste_yazdir(meyve_listesi)
            secilen_meyve = input("hangi meyveyi seçmek istersiniz?: ")

            if secilen_meyve in meyve_listesi:
                miktar = float(input("Kaç kilo almak istersiniz?: "))  # seçilen meyvenin indeksi tanımlanır. tanımlanan indeksin meyve stoktaki karşılığından alınan miktar çıkarılır
                index = meyve_listesi.index(secilen_meyve)

                # stoktaki durumu kontrol et
                if miktar <= meyve_stok[index]:
                    manav_alınacak_meyveler.append(secilen_meyve)

                    güncel_meyve_stok.append(miktar)

                else:
                    print(secilen_meyve, "istenilen miktarda bulunmamaktadır.")
            else:
                print("Geçersiz seçim")

        elif tercih == "s":
            print("\n(sebze_listesi")
            liste_yazdir(sebze_listesi)
            secilen_sebze = input("hangi sebzeyi seçmek istersiniz?: ")

            if secilen_sebze in sebze_listesi:
                index = sebze_listesi.index(secilen_sebze)
                miktar = float(input("kaç kilo almak istersiniz?: "))
                # stoktaki durumu kontrol et
                if miktar <= sebze_stok[index]:
                    manav_alınacak_sebzeler.append(secilen_sebze)

                    güncel_sebze_stok.append(miktar)

                else:
                    print(secilen_sebze, "istenilen miktarda bulunmamaktadır")
                    continue

            else:
                print("Geçersiz seçim")
                continue

        else:
            print("geçersiz seçenek. Lütfen m ya da s yazın:")
        #  başka bir arzu olup olmadığı sorulur
        devam = input("başka bir arzunuz var mı?: (e/h")

        if devam == "h":
            print("iyi günler")
            break

        elif devam == "e":
            continue
        else:
            print("geçersiz cevap. evet ya da hayır yazınız.")
            continue

def müsteri_ile_etkilesim():

    while True:
        print("MÜŞTERİ-MANAV")
        tercih = input("meyve mi sebze mi (m/s):")
        if tercih == "m":
            print("\nmeyve_listesi")
            liste_yazdir(manav_alınacak_meyveler)
            müsteri_meyve_secimi = input("hangi meyveyi seçmek istesiniz?: ")
            if müsteri_meyve_secimi in manav_alınacak_meyveler:
                index2 = manav_alınacak_meyveler.index(müsteri_meyve_secimi)
                miktar2 = float(input("Kaç kilo almak istersiniz?: "))

                # stoktaki durumu kontrol et
                # ***elma 2 kere girildiğinde toplam miktar yazdırılmalı?**
                if miktar2 <= güncel_meyve_stok[index2]:
                    güncel_meyve_stok[index2] -= miktar2
                    müsteri_alınacak_meyveler.append(müsteri_meyve_secimi)
                    müsteri_meyve_alısverisi.append(miktar2)
                    print(müsteri_meyve_secimi, miktar2, "kilo satın alındı")

                else:
                    print(müsteri_meyve_secimi, "istenilen miktarda bulunmamaktadır.")
            else:
                print("Geçersiz seçim")
                continue

        elif tercih == "s":
            print("\nsebze_listesi")
            liste_yazdir(manav_alınacak_sebzeler)
            müsteri_sebze_secimi = input("hangi sebzeyi seçmek istesiniz?: ")

            if müsteri_sebze_secimi in manav_alınacak_sebzeler:
                index = manav_alınacak_sebzeler.index(müsteri_sebze_secimi)
                miktar = float(input("Kaç kilo almak istersiniz?: "))
                # stoktaki durumu kontrol et

                if miktar <= güncel_sebze_stok[index]:
                    güncel_sebze_stok[index] -= miktar
                    müsteri_alınacak_sebzeler.append(müsteri_sebze_secimi)
                    müsteri_sebze_alısverisi.append(miktar)
                    print(müsteri_sebze_secimi, miktar, "kilo satın alındı")

                else:
                    print(müsteri_sebze_secimi, "istenilen miktarda bulunmamaktadır.")
            else:
                print("geçersiz seçim.İstediğiniz sebze bulunmamaktadır")

        else:
         print("geçersiz seçim. Lütfen meyve ya da sebze seçiniz")

        devam = input("başka bir arzunuz var mı?: (e/h) ")

        if devam == "h":
            print("afiyet olsun")
            break

        elif devam == "e":
            continue

        else:
            print("geçersiz cevap. e ya da h yazınız.")
            continue


def müsteri():
    print("ALINAN MEYVE VE SEBZELER")
    print("müsterinin aldığı meyve listesi:", müsteri_alınacak_meyveler)
    print("alınan meyvelerin miktarları:", müsteri_meyve_alısverisi)
    print("müsterinin aldığı sebze listesi:", müsteri_alınacak_sebzeler)
    print("alınan sebzelerin miktarları:", güncel_sebze_stok)



hal_ile_etkilesim()
müsteri_ile_etkilesim()
müsteri()