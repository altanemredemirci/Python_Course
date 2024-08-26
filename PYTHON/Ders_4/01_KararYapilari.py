################## AKIŞ KONTROL-KARAR YAPILARI (IF ELIF ELSE) ##########################

"""
###IF ELSE TANIMLAMA
if elif else deyimleri bir kod akışında kontrol yapmayı ve kontrol sonucuna göre işlem adımını belirlediğimiz yazılım yapısıdır.

if ile ilk kontrol durumu yazılır.
if deyimindeki kontrol başarısız(false) olursa bir diğer durumu elif deyimi ile kontrol ederiz.
önceki elif deyimindeki kontrol başarısız(false) olursa bir diğer durumu elif deyimi ile kontrol ederiz.
if ve elif deyimleri ile gerekli kontroller yapıldıktan sonra geriye kalan ve kontrol edilmeyen bütün durumlar için else deyimi kullanılır.


if(kontrol1):
  kontrol1 true olursa bualandaki kod bloğu çalışır
elif(kontrol2):
   kontrol2 true olursa bualandaki kod bloğu çalışır
elif(kontrol3):
   kontrol3 true olursa bualandaki kod bloğu çalışır
else:
    if ve elif kontrolleri dışında bir durum oluşursa bu kod bloğu çalışır.
"""

#Kullanıcıdan bir sayı alınız ve alınan sayının pozitif mi negatif mi olduğunu kontrol ederek ekrana yazdırınız
"""
1-başla
2-sayi1 = 1.sayıyı giriniz
3-Eğer sayi1>0 ise ekrana "Pozitif" Yaz
4-değilse Eğer sayi1<0 ekrana "Negatif" Yaz
5-Değilse Ekrana 0 Yaz
6-Bitti 
"""
# sayi1=int(input("1 sayı giriniz"))
# if sayi1>0:
#    print("Pozitif")
# elif sayi1<0:
#     print("Negatif")
# else:
#     print("0")


###################### ALIŞTIRMALAR ##########################
# ÖRNEK: Kullanıcıdan haftanın kaçıncı günü olduğu bilgisini alınacak ve gün adı ekrana yazılacak.
# gunsayisi = int(input("Haftanın kaçıncı günü?"))
# if(gunsayisi==1):  #if gunsayisi==1:
#     print("Pazartesi")
# elif gunsayisi==2:
#     print("Salı")
# elif gunsayisi==3:
#     print("Çarşamba")
# elif gunsayisi==4:
#     print("Perşembe")
# elif gunsayisi==5:
#     print("Cuma")
# elif gunsayisi==6:
#     print("Cumartesi")
# elif gunsayisi==7:
#     print("Pazar")
# else:
#     print("HATALI İŞLEM!! Hafta 7 günden oluşur.")


# gunsayisi = int(input("Haftanın kaçıncı günü?"))
# if gunsayisi<0 or gunsayisi>7:
#     print("HATALI İŞLEM!! Hafta 7 günden oluşur.")
# elif(gunsayisi==1):  #if gunsayisi==1:
#     print("Pazartesi")
# elif gunsayisi==2:
#     print("Salı")
# elif gunsayisi==3:
#     print("Çarşamba")
# elif gunsayisi==4:
#     print("Perşembe")
# elif gunsayisi==5:
#     print("Cuma")
# elif gunsayisi==6:
#     print("Cumartesi")
# else:
#     print("Pazar")

#SORU: Klavyeden girilen değer 100'den büyükse karesini, 100'den küçük ise küpünü ekrana yazdıran program.

# sayi=int(input("Sayı giriniz:"))
# if sayi>100:
#     print(sayi**2)
# elif sayi<100:
#     print(sayi**3)
# else:
#     print("Sayı 100'e eşittir.")


# sayi=78
# # if(sayi>10 and sayi<100):
# if(10<sayi<100):
#     print("sayı 10 dan büyük 100 den küçük")
# elif(sayi>20 and sayi<80):
#     print("sayı 20 den büyük 80 den küçük")

#SORU: Öğrenciden vize final notlarını alın ve ortalamaya göre harf notunu yazdırınız
# 0-24       : FF
# 25-44      : DD
# 45-54      : CC
# 55-69      : CB
# 70-84      : BB
# 85 ve üstü : AA
# vize = int(input("Vize Notunu Giriniz:"))
# final = int(input("Final Notunu Giriniz:"))
#
# if vize<0 or vize>100 or final<0 or final>100:
#     print("Vize Final notlarını hatalı")
# else:
#     nott = (vize + final)/2
#     if nott>=0 or nott<25:
#         print("Notunuz : FF")
#     elif nott>24 and nott<45:
#         print("Notunuz : DD")
#     elif nott>45 and nott<55:
#         print("Notunuz : CC")
#     elif nott>55 and nott<70:
#         print("Notunuz : CB")
#     elif nott>70 and nott<85:
#         print("Notunuz : BB")
#     else:
#         print("Notunuz: AA")



"""
vize = int(input("Vize Notunu Giriniz:"))
final = int(input("Final Notunu Giriniz:"))

if vize<0 or vize>100 or final<0 or final>100:
    print("Vize Final notlarını hatalı")
   
else:
    nott = (vize + final)/2
    if nott<25: #25,26....
        print("Notunuz : FF")
    elif nott<45:
        print("Notunuz : DD")
    elif nott<55:
        print("Notunuz : CC")
    elif nott<70:
        print("Notunuz : CB")
    elif nott<85:
        print("Notunuz : BB")
    else:
        print("Notunuz: AA")
"""
"""
while True:
    vize = int(input("Vize Notunu Giriniz:"))
    final = int(input("Final Notunu Giriniz:"))

    if vize < 0 or vize > 100 or final < 0 or final > 100:
        print("Vize Final notlarını hatalı")

    else:
        nott = (vize + final) / 2
        if nott < 25:  # 25,26....
            print("Notunuz : FF")
        elif nott < 45:
            print("Notunuz : DD")
        elif nott < 55:
            print("Notunuz : CC")
        elif nott < 70:
            print("Notunuz : CB")
        elif nott < 85:
            print("Notunuz : BB")
        else:
            print("Notunuz: AA")
        break
"""
#SORU: Müşteriden iki ürün fiyatı alınacak. Bu ürünlerden pahalı olana %25 indirim uygulanacak ve toplam ödeme tutarı ekrana yazdırılıacak.

# Soru Kullanıcıdan isim, yaş, maaş ve çocuk sayısı alınsın.
"""
    Eğer kulanıcının yaşı 45'in altındaysa;
    Çocuk sayısına bakılacak. Ve çocuk sayısı 3'ten az ise çocuk başına 2500₺ çok ise çocuk başına 2000₺ 
    maaşa ekleme yapılacak.(Temel Maaş= 30000₺)
    45 ve üzerinde ise çocuk başına para verilmeyecek ancak 5000₺ ekleme yapılacak.
    Son olarak ekrana : "Nesrin Yılmaz, Maaşınız: 40000₺" yazılacak.  
"""

isim=input("İsminiz:")
yas=int(input("Yaş:"))
maas=float(input("Maaş:"))
cocukSayisi=int(input("Çocuk Sayısı:"))
if(yas<45):
    if(cocukSayisi<3):
        maas+=cocukSayisi*2500 # maas=maas+(cocukSayisi*2500)
        print(isim+" Maaşınız:",maas,sep="")
    else:
        maas+=cocukSayisi*2000
        print(f"{isim} Maaşınız:{maas}")
elif(yas>44 and yas<80):
    maas+=5000
    print("{} Maaşınız:{}".format(isim,maas))
else:
    print("Yaş Bilgisi Hatalı!!")








