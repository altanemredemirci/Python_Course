######## ****** VERİ TİPLERİ-Data Types ******* ########

# Python dilinde 3 veri tipi vardır.
# Sayısal(Integer),Sözel(String),Mantıksal(Boolean)


# **** SAYISAL VERİ TİPLERİ
"""
int: -/+ tam sayıları tanımlar
float: -/+ ondalıklı sayıları tanımlar
complex: Karmaşık sayıları tanımlar. (c=5+3j)

"""

# yas=34
# print(type(yas))
# bakiye = 50000.50
# print(type(bakiye))
# c=5+3j
# print(type(c))
# print(c.imag)
# print(c.real)
# print(type(c.imag))

# Klavyeden 3 sayı girilecek ve girilen sayıların toplamı ekrana yazdırılacak
# sayi1=1
# sayi2=2
# sayi3=3
# toplam=sayi1+sayi3+sayi2
# print(toplam)
# print(sayi1+sayi3+sayi2)


## Çoklu Değişken Tanımlama
# c1=c2=c3=12
# print(c1)
# print(c2)
# print(c3)
#
# x,y=11,13
# print(x)
# print(y)

# Aşağıda tanımlı iki değişkenin değerini 3. değişken kullanmadan takas edin
# x=10
# y=20
#
# x,y = y,x
# print("x değeri:",x)
# print("y değeri:",y)


# **** SÖZEL VERİ TİPLERİ
# string: metinsel datalar string olarak tanımlanır ve tanımlanırken ' veya " tırnak kullanılır.
# ad="Altan"
# soyad='Demirci'
# print(ad)
# print(soyad)
#
# yas=34

# + operatörü sözel iki değer için birleştirme(concat) işlemi yapar
# print(ad+soyad)
# print(ad+"      "+soyad)

# adSoyad=ad+" "+soyad
# print(adSoyad)
# + operatörü iki sayısal değer için toplama işlemi yapar.

#*** + operatörü biri string diğeri integer değer olan değişkenler için kullanılamaz. HATA!!!!

# print(ad+yas)
# yas=34
# maas=150.50
# ad="Erkan"
# print(ad,yas)
# print(yas+maas)


# **** MANTIKSAL VERİ TİPLERİ(BOOLEAN)
# bool: sadece bir karşılaşırma cevabı olarak TRUE veya FALSE verir.

# cevap=True
# print(type(cevap))

# sonuc = 3>5
# print(type(sonuc))
# print(sonuc)

# username="altanemre"
#
# kullanici=input("Username:")
# print(kullanici==username)


### ****** CONVERT ********
### Kullanıcıdan 2 sayı alın ve toplamını ekrana yazdırınız
# sayi1=input("1.Sayıyı giriniz")
# s1=int(sayi1)
# print(type(sayi1))
# print(type(s1))

# sayi1=int(input("1.Sayıyı giriniz"))
# sayi2= int(input("2.Sayıyı Giriniz"))
# print(sayi2+sayi1)



### SORU: Kullanıcıdan vize ve final notlarını alınız ve ortalamayı ekrana yazdırınız.
##Ortalama: vize%40 final%60

# vize= int(input("Vize Notunu Giriniz :"))
# final = int(input("Final Notunu Giriniz :"))
# ortalama= vize*0.4 + final*0.6
# print(ortalama)

##turtle

##### STRING KAÇIŞ KARAKTERİ ########
# print("Altan\nEmre\nDemirci")

# print("""
# Altan
#             EMRE
#     Demirci
#
#
# """)
#
# print('''
# Altan
#             EMRE
#     Demirci
#
#
# ''')













