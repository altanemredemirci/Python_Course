############### COLLECTIONS - KOLEKSİYONLAR #############
"""
* list
* tuple
* set
* dict
"""
######### LIST ##########
### Boş Liste Tanımı
# sayilar=list()
# sayilar=[]

### Dolu Liste Tanımı
# sayilar=[1,2,3,4,5]
# print(type(sayilar))

### Liste Değer Sayısı
# sayilar=[11,12,13,14]
# print("Eleman Sayısı:",len(sayilar))


### Liste Değerlerini Yazdırma
# Koleksiyonlar içindeki değerleri INDEX adı verilen 0 dan başlayarak 1'er 1'er artan numaralandırma sitemiyle tutarlar.
# sayilar=[11,12,13,14,15]
# print(sayilar[2])
# print(sayilar[5]) #IndexError hatası verir.

# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i+=1

### Listeye Değer Ekleme
# sayilar=list()
# sehirler=["Adana","İstanbul"]
# sayilar=[11,12,13,14,15]
# sayilar.append(16)
# sayilar.append(17)
# sayilar.append(18)

#2.yöntem
# sehirler+=["Ardahan"]
# sehirler+=["Kars"]
#
# sayilar+=[16]
# sayilar+=[17]
# sayilar+=["Hakan"]
# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i+=1

# for sehir in sehirler:
#     print(sehir)
#
# for sayi in sayilar:
#     print(sayi)


### Liste Değer Silme
# Değer üzerinden silme
# sehirler=["Adana","İstanbul","Kars","Bitlis"]
# # sehirler.remove("Adana")
#
# # Index ile slme
# del sehirler[2]
#
# for sehir in sehirler:
#     print(sehir)


### Çoklu Eleman Ekleme
# karisikListe=[1,"Adana",75,"Aradahan",36,"Kars"]
# karisikListe += [10,"Balıkesir",41,"Kocaeli"]
# karisikListe.append(10,"Balıkesir",41,"Kocaeli") # HATA
# karisikListe.append([10,"Balıkesir",41,"Kocaeli"]) # YAPI HATASI
# print(karisikListe[6][1])
# for value in karisikListe:
#     print(value)

### Istenilen Index'e Değer Ekleme
# sehirler=["Adana","İstanbul","Kars","Bitlis"]

# sehirler.insert(2,"Zonguldak")
#
# for sehir in sehirler:
#     print(sehir)

### Istenilen Değerin Index Numarasını Alma
# sehirler=["Adana","İstanbul","Kars","Bitlis","Adana","Kilis","Gaziantep","Adana","Tekirdağ"]
# index=sehirler.index("Adana")
# index=sehirler.index("Adana",1) # değeri aramaya başlanacak indexi belirleme
# index=sehirler.index("Adana",4,8) #değeri aramaya index aralığı belirleme
# print(index)

### Liste İçerisinde Bir Değerin Kaç Tane Olduğunu Bulma
# sehirler=["Adana","İstanbul","Kars","Bitlis","Adana","Kilis","Gaziantep","Adana","Tekirdağ"]
#
# adet=sehirler.count("Adana")
# print(adet)

listem = ["Manisa","Çanakkale","Kocaeli","Konya","Sivas","Gaziantep","İzmir","İstanbul","Çorum"]
# print(listem[-1])
# print(listem[-2])
# print(listem)

## Liste Elemanlarını Sıralama (A->Z  0->9)
# listem.sort()
# print(listem)
# listem.sort(reverse=True)


## Listedeki Elemanları Ters Çevirme
# print(listem)
# listem.reverse()
# print(listem)

"""

"""
## Listedeki Elemanı Dışarı Atma
#LIFO(Last In First Out) FIFO(First In First Out)
# sayilar = [10,20,30,40,50]
# # sayi = sayilar.pop() # son eklenen değer dışarı atılır.
# sayi = sayilar.pop(2) # istenilen indexdeki değer dışarı atılır.
# print(sayilar)
# print(sayi)


## Bir Değerin Liste Varlık Kontrolü
# sayilar = [10,20,30,40,50]
#
# print(40 in sayilar)
# print(40 not in sayilar)



harfler = ["a","c"]
harfler += ["ç"]  # sona ekleme
harfler += ["d","e"] # sona birden fazla ekleme
print(harfler)
harfler.insert(1,"b") # araya eleman ekleme. 1. indise değer ekleme
harfler[2:1] = ["o"]*3 # o elemanını 2. indisten başlayıp 3 adet ekle.
print(harfler)

# ????