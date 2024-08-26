
### OPERATORLER ###

# Atama(=) / İşlemli Atama Operatörleri
"""
sayi=5

sayi+=1 #sayi=sayi+1
sayi-=1 #sayi=sayi-1
sayi*=1 #sayi=sayi*1
sayi/=1 #sayi=sayi/1
print(sayi)
"""

### Aritmatik Operatörler ###
"""
    +,-,* : toplama,çıkarma,çarpma
    /     : ondalıklı bölme
    //    : tamsayı bölme
    %     : mod alma => bölme sonucunda kalanı verir
    **    : üs alma
"""

# print(10/5)
# print(10/3)

# print(10//5)
# print(10//3)

# print(10%3)

#Mod Alma
##girilen sayı çift mi?
# sayi=11
# print("Çift mi:",sayi%2==0)

#Üs Alma
# print(3**2)

### Karşılaştırma Operatörleri

# sayi1=4
# sayi2=8
#
# bool1 = sayi1 == sayi2 #eşitse True değilse False
# bool2 = sayi1 != sayi2 # eşitse False değilse True
# bool3 = sayi1 >= sayi2 # büyük veya eşitse True, küçükse False
# bool4 = sayi1 <= sayi2 # küçük veya eşitse True, küçük False
#
# print(bool1,bool2,bool3,bool4)

## MANTIKSAL OPERATÖRLER (AND,OR)
#And Operatorü:birden fazla durum kontrolü yapılacak ve her kontrolün TRUE olma şartı var ise AND operatörü kullanılır.

"""
1.durum * 2.durum   sonuc
    0      0        0 
    0      1        0
    1      0        0
    1      1        1
"""

# Kullanıcının işe alınması için yas aralığının 18 ile 45 arasında olması gerekli
"""
yas=int(input("Yaşınız:"))

sonuc= yas>17 and yas<46

print(sonuc)
    """

# username="altanemre"
# password="123"
#
# kullaniciAdi=input("Kullanıcı Adı:")
# sifre=input("Şifreniz:")
#
# print(username==kullaniciAdi and sifre==password)

# OR Operatörü:Birden fazla durum kontrolü yapılacak ve herhangi bir kontrolün TRUE olması yeterli ise OR operatörü kullanılır.

"""
instagram giriş => kullanıcıAdı/Email
                   şifre
"""
# username="admin"
# email="admin@gmail.com"
# password="123"

# kullanici=input("Username/Email:")
# sifre=input("Şifre:")
#
# print( (username==kullanici or email==kullanici) and  sifre==password )
"""
1.durum  + 2.durum   sonuc
    0      0            0  
    0      1            1  
    1      0            1  
    1      1            1  
"""

## NOT Operatoru: True => False   False => True

# print(not 2>3)


##Seperatörler
# print("Altan","Emre","Demirci")
# print("Altan","Emre","Demirci",sep=" ")     #default tanımı
# print("Altan","Emre","Demirci",sep="-")
# print("Altan","Emre","Demirci",sep="")

# print("Altan","Emre","Demirci")
# print("Altan","Emre","Demirci",end="\n")
# print("Altan","Emre","Demirci",end="")
# print("Altan","Emre","Demirci")

# sayi10 = 100
# sayi20 = 100
# esitKontrol1 = (sayi10==sayi20)
# print("sayi10 ve sayi20 eşit mi?:",esitKontrol1)
#
# esitKontrol2 = sayi10 is sayi20
# print("sayi10, sayi20 mi?:",esitKontrol2)
#
# esitKontrol3 = sayi10 != sayi20
# print("sayi10 sayi20 den farklı mı?:",esitKontrol3)
#
# esitKontrol4 = sayi10 is not sayi20
# print("sayi10 sayi20 den farklı mı?:",esitKontrol4)




# print("Adı" in "Kadıköy") # Kadıköy içerisinde adı var mı?
#
# print("arı" in "Kadıköy") # Kadıköy içerisinde arı var mı?
# print("arı" not in "Kadıköy") # Kadıköy içerisinde yok mu?


# print("esitKontrol1 değişkeninin bellekteki(ram) adresi:",id(esitKontrol1))

###############################         ALIŞTIRMALAR        ####################################
"""
# SORU: Kullanıcıdan alınan 1. sayının, kullanıcının girdiğe 2. sayıya kuvvetini ekrana yazdıran program.
# Örnek: sayi1 = 10 sayi2 = 2 Sonuç=100
"""
sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))
kuvvetal = sayi1 ** sayi2
print(kuvvetal)


