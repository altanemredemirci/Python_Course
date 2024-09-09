"""
  /*
             HAL - Toptancı
            * Manav ürün almaya geliyor. Manava "Meyve mi Sebze mi? sorucaz" -> M
            * 5 adet meyve listelenecek -> ELMA
            * Meyve seçildikten sonra "Kaç Kilo?" ->10
            * Meyve satıldıktan sonra "Başka bir arzunuz var mı?"
            * Evet derse tekrar "Meyve mi Sebze mi?" satırına döndüreceğiz
            * Hayır. "iyi günler" diyerek manav kısmına geçeceğiz
            *
            *
             MANAV
            * "Meyve mi Sebze mi?" diye müşteriye soracağız.
            * Halden almış olduğumuz meyve veya sebzeleri listeleyeceğiz.
            * Müşteri ürün seçtikten sonra "Kaç Kilo?" sorusunu sorun
            * Girilen kilo bilgisini manavın halden aldığı kilo ile kıyaslayarak ürün satınız.
            * Elde olan ürün var olan kilosu kadar satılırsa, manavın ürünlerinden silin.
            * Ürün satıldıktan sonra "Başka bir arzunuz var mı?"
            * Evet derse tekrar "Meyve mi Sebze mi?" satırına döndüreceğiz
            * Hayır derse "Afiyet olsun" Müşteri kısmına geçiniz

            MÜŞTERİ
            * Alınan ürünleri ekrana yazdırınız.
             */


"""
halMeyve=["ELMA","ARMUT","MUZ"]
halSebze=["PATLICAN","SOGAN","BIBER"]
manavMeyve=list()
manavSebze=list()
manavMeyveKilo=list()
manavSebzeKilo=list()
musteriUrun=list()
musteriUrunKilo=list()

while True:
    print("***** HALE HOŞGELDİNİZ *****")
    halsecim=input("Meyve mi? Sebze mi?(M\S) Çıkış Q\nSeçiminiz:").upper() # lower(): küçük harfe çevirir.
    if halsecim=="M":
        while True:
            for i in range(len(halMeyve)):
                print(f"{i}-{halMeyve[i]}") # f: format. f ile " arasında python terimi kullanacağımı belirtiyorum"
            index=int(input("100-Çıkış\nİstediğiniz ürün numarası:"))
            if 0<=index<len(halMeyve):
                if halMeyve[index] not in manavMeyve:
                    manavMeyve.append(halMeyve[index])
                    kilo=int(input("Kaç kilo istersiniz?"))
                    manavMeyveKilo.append(kilo)
                else:
                    kilo = int(input("Kaç kilo istersiniz?"))
                    indexMeyve=manavMeyve.index(halMeyve[index])
                    manavMeyveKilo[indexMeyve]+=kilo

                donus=input("Başka arzunuz var mı?(E\H)").upper()
                if donus=="E":
                    continue
                else:
                    break

            elif index==100:
                break
            else:
                print("Hatalı Ürün Seçimi!!")
    elif halsecim=="S":
        while True:
            for i in range(len(halSebze)):
                print(f"{i}-{halSebze[i]}")  # f: format. f ile " arasında python terimi kullanacağımı belirtiyorum"
            index = int(input("100-Çıkış\nİstediğiniz ürün numarası:"))
            if 0 <= index < len(halSebze):
                if halSebze[index] not in manavSebze:
                    manavSebze.append(halSebze[index])
                    kilo = int(input("Kaç kilo istersiniz?"))
                    manavSebzeKilo.append(kilo)
                else:
                    kilo = int(input("Kaç kilo istersiniz?"))
                    indexSebze = manavSebze.index(halSebze[index])
                    manavSebzeKilo[indexSebze] += kilo

                donus = input("Başka arzunuz var mı?(E\H)").upper()
                if donus == "E":
                    continue
                else:
                    break

            elif index == 100:
                break
            else:
                print("Hatalı Ürün Seçimi!!")
    elif halsecim=="Q":
        print("Yine Bekleriz..")
        break

    else:
        print("Hatalı Seçim!!")

while True:
    print("***** MANAVA HOŞGELDİNİZ *****")
    manavSecim=input("Meyve mi? Sebze mi?(M\S) Çıkış Q\nSeçiminiz:").upper()

    if manavSecim=="M":

        if len(manavMeyve)==0:
            print("Meyveler Tükenmiştir.")
            continue
        while True:
            for i in range(len(manavMeyve)):
                print(f"{i}-{manavMeyve[i]}:{manavMeyveKilo[i]}")
            indexManav=int(input("100-Çıkış\nİstediğiniz ürün numarası:"))
            if 0<=indexManav<len(manavMeyve):
                kilo = int(input("Kaç kilo istersiniz?"))
                if kilo<=manavMeyveKilo[indexManav]:
                    manavMeyveKilo[indexManav] -= kilo

                    if manavMeyve[indexManav] not in musteriUrun:
                        musteriUrun.append(manavMeyve[indexManav])
                        musteriUrunKilo.append(kilo)
                    else:
                        urun=manavMeyve[indexManav]
                        indexUrun=musteriUrun.index(urun)
                        musteriUrunKilo[indexUrun]+=kilo

                    if manavMeyveKilo[indexManav]==0:
                        del manavMeyve[indexManav]
                        del manavMeyveKilo[indexManav]
                else:
                    print(f"Yetersiz Kilo! Elimizde {manavMeyve[indexManav]} {manavMeyveKilo[indexManav]} kilo mevcut")

                donus = input("Başka arzunuz var mı?(E\H)").upper()
                if donus == "E":
                    continue
                else:
                    break

            elif indexManav==100:
                break
            else:
                print("Hatalı ürün seçimi!!")

    elif manavSecim=="S":
        if len(manavSebze) == 0:
            print("Meyveler Tükenmiştir.")
            continue
        while True:
            for i in range(len(manavSebze)):
                print(f"{i}-{manavSebze[i]}:{manavSebzeKilo[i]}")
            indexManav = int(input("100-Çıkış\nİstediğiniz ürün numarası:"))
            if 0 <= indexManav < len(manavSebze):
                kilo = int(input("Kaç kilo istersiniz?"))
                if kilo <= manavSebzeKilo[indexManav]:
                    manavSebzeKilo[indexManav] -= kilo

                    if manavSebze[indexManav] not in musteriUrun:
                        musteriUrun.append(manavSebze[indexManav])
                        musteriUrunKilo.append(kilo)
                    else:
                        urun = manavSebze[indexManav]
                        indexUrun = musteriUrun.index(urun)
                        musteriUrunKilo[indexUrun] += kilo

                    if manavSebzeKilo[indexManav] == 0:
                        del manavSebze[indexManav]
                        del manavSebze[indexManav]
                else:
                    print(f"Yetersiz Kilo! Elimizde {manavSebze[indexManav]} {manavSebzeKilo[indexManav]} kilo mevcut")

                donus = input("Başka arzunuz var mı?(E\H)").upper()
                if donus == "E":
                    continue
                else:
                    break

            elif indexManav == 100:
                break
            else:
                print("Hatalı ürün seçimi!!")
    elif manavSecim=="Q":
        print("Yine Bekleriz.")
        break
    else:
        print("Hatalı Seçim!!")

for i in range(len(musteriUrun)):
    print(f"Ürün Adı:{musteriUrun[i]} Kilosu:{musteriUrunKilo[i]}")