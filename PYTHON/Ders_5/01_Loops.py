####################################################
################### DÖNGÜLER #######################
####################################################

###    WHILE   ###
"""
while(koşul):
    while koşulu true olduğu sürece bu kod bloğu tekrar tekrar çalışır
"""

#1-10 aralığında sayı ekrana yazdırınız.
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)

# i=1
# while(i<11):
#     print(i)
#     i+=1


## *** BREAK KOMUTU ***

# i=1
# while(True):
#     print(i)
#     i+=1
#     if i==10:
#         break # break komutu çalıştığında içinde bulunduğu loop(döngü) u kırar.



## 1 ile 10 arasındaki sayıları ekrana yazdırınız ama 7 sayısını atlayınız
# i=1
# while(i<11):
#     if i==7:
#         i+=1
#     else:
#         print(i)
#         i+=1
#

## *** CONTINUE KOMUTU ***
# i=1
# while(i<11):
#     if i==7:
#         i+=1
#         continue
#     print(i)
#     i+=1

######################## ALIŞTIRMALAR ################################
# 90-100 arasındaki çift sayıları ekrana yazdıran program.

# i=90
# while i<101:
#     if i%2==0:
#         print(i)
#     i+=1

# 70-55 arasındaki sayılardan 3'e tam bölünenleri ekrana yazdıran program.
# sayi=70
# while(sayi>=55):
#     if sayi%3==0:
#         print(sayi)
#     sayi-=1


# 7- 77 arasındaki tüm sayıları toplayıp ekrana yazdıran program.
# number = 7
# sum=0
# while number < 77:
#     sum+=number
#     number += 1
#
# print(sum)

# 1'den klavyeden girilen sayıya kadar olan sayıların karelerini toplayan program.
# start_num = 1
# sum = 0
# while True:
#     number = int(input("Bir Sayı Giriniz: "))
#     if(start_num>number):
#         print("Negatif değer girilemez")
#     else:
#         while start_num < number:
#             sum += start_num **2
#             start_num += 1
#         print(sum)
#         break


# start_num = 1
# sum = 0
# loop=True
# while loop:
#     number = int(input("Bir Sayı Giriniz: "))
#     if(start_num>number):
#         print("Negatif değer girilemez")
#     else:
#         while start_num < number:
#             sum += start_num **2
#             start_num += 1
#         print(sum)
#         loop=False

# Klavyeden girilen değer 'cık' ise döngüden çıksın. Değilse girilen sayıları toplayıp cıkılınca ekrana yazdırsın.
# toplam=0
# while True:
#     sayi=input("Bir sayı giriniz")
#     if sayi=="cik":
#         print(toplam)
#         break
#
#     toplam+=int(sayi)


# 1-100 arasındaki sayıların toplayan program. Ancak aşağıdaki durumlarda sayıyı toplama eklemeyecek.
# * Sayı 7'nin katı ise toplama eklenmesin.
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıksın.

# toplam=0
# i=1
# while i<101:
#     if i%7==0:
#         i+=1
#         continue
#     if ((3*i)+7)%37==0:
#         break
#     print(i)
#     toplam+=i
#     i+=1
#
# print(toplam)

# Kullanıcının girdiği 2 değer arasındaki tek ve çift sayıları ayrı ayrı toplayarak ekrana yazıran program
"""
cifttoplam=0
tektoplam=0


basla=int(input("Başlangıç Değeri:"))
bitis=int(input("Bitiş Değeri:"))

if basla>bitis:
    basla,bitis=bitis,basla

while basla<bitis:
    if basla%2==0:
        cifttoplam+=basla
    else:
        tektoplam+=basla
    basla+=1

print(f"Tek sayı toplamı:{tektoplam}")
print("Çift sayı toplamı:",cifttoplam)
"""

#Kullanıcıdan alınan sayının asal olup olmadığını döndüren program.
# asal sayı sadece kendisine ve 1 e bölünen
# sayi=int(input("Bir asal sayı giriniz:"))
#
# asalMi=True
# bolen=2
# if(sayi<2):
#     print("Sayı Asal Değildir")
# elif(sayi==2):
#     print("Asaldır")
# else:
#     while sayi>bolen:
#         if sayi%bolen==0:
#             print("Asal Değildir")
#             asalMi=False
#             break
#         bolen+=1
#     if(asalMi):
#         print("Asaldır")

#ÖDEV: Girilen iki sayı arasındaki ASAL sayıları ekrana yazdırınız

###   FOR DÖNGÜSÜ   ###
#Aralık Tanımlama
#*** başlangıç değeri default 0 olur. Bitiş değeri aralığa DAHİL EDİLMEZ.
range(5) #0,1,2,3,4 (bitiş)
range(2,7) #2,3,4,5,6 (başlangıç,bitiş)
range(1,9,3) #1,4,7 (başlangıç,bitiş,artış)

# 0 ile 5 arasındaki sayıların ekrana yazdır
# i=0
# while i<5:
#     print(i)
#     i+=1

# for i in range(5):
#     print(i)

# for i in range(2,7):
#     print(i)

# for i in range(1,9,3):
#     print(i)

# isim="HAKAN BALTA"
# for harf in isim:
#     print(harf)

# for i in range(100):
#     print("BEN PYTHON ÖĞRENEMİCEM")

#######################         ALIŞTIRMALAR      #############################

# 1 ile 40 arasındaki sayıları toplayan program.(1,40 dahil)

# sum=0
# for i in range(1,41):
#     sum+=i
#
# print(sum)

# Aşağıdaki çıktıyı veren kodu for döngüsü ile yazınız.
"""
*
**
***
****
*****
"""
# print("Altan hoca mükemmeldir"*10)
# for i in range(1,6): #i:1,2,3,4,5
#     print("*"*i)

# i=1
# while i<6:
#     print("*"*i)
#     i+=1


"""
***********
*         *  
*         *
*         *
***********
"""
# for i in range(1,6):
#     if i==1 or i==5:
#         print("*"*10)
#     else:
#         print("*"+" "*8+"*")
#
# i=1
# while i<6:
#     if i==1 or i==5:
#         print("*"*10)
#     else:
#         print("*"+" "*8+"*")
#     i+=1
"""
                *
               ***
              *****
             *******
            *********   
"""
# bosluk=13
# for i in range(1,17,2):
#     print(bosluk*" ",end="")
#     print(i*"*")
#     bosluk-=1


#Çarpım Tablosu
"""
1*1=1   2*1=2
1*2=2   2*2=4
1*3=3   2*3=6

for i in range(1,11):
    for j in range(1,11):
        print(j,"*",i,"=",(i*j),sep="",end="\t")
    print()#end="\n"
"""
# Kullanıcı: personel sayısını girsin. Her personel için çocuk sayısı sorulsun.
# Program her çocuk için : "Çocuğunuz adına 1 ağaç dikilmiştir."
# Toplam dikilen ağaç sayısını yazsın.
# tree_sum = 0
# staffnum = int(input("Personel Sayısını Giriniz: "))
# for i in range(staffnum):
#     child_num = int(input(f"{i+1}.Personelin çocuk sayısını girin: "))
#     tree_sum += child_num
#     for j in range(child_num):
#         print("Çocuğunuz adına 1 ağaç dikilmiştir")
# print("Toplam dikilen ağaç sayısı:",tree_sum)


# toplamAgacSayisi=0 #Camel Case
# personelSayisi = input("Personel Sayısı:")
# # if personelSayisi.isnumeric(): # değer içindeki herşey sayısal mı?
# if personelSayisi.isdigit(): # değer içindeki herşey dijital mi?
#     for personel in range(int(personelSayisi)):
#         print("Çocuk Sayısı")
# else:
#     print("Personel sayısını rakam olark giriniz!!!")


#
# alfabe = "abcdefghijklmnoprstuvyz"
#
# sifrelecek = input("şifrelenecek olan veriyi giriniz :").lower()
# sifrelecek = sifrelecek.replace(" ", "")  # space kurtulduk
# sifrelenmis = ""
#
# for item in sifrelecek:
#     if item in alfabe:
#         sifrelenmis += alfabe[(alfabe.index(item) + 4) % len(alfabe)]
#     else:
#         sifrelenmis += " "
#
# print(sifrelenmis)
# ###
# sifre=""
# for i in sifrelenmis:
#     sifre+=alfabe[(alfabe.index(i)-4)%len(alfabe)]
# print(sifre)


# for i in range(1,6):
#     print(i)
# else:
#     print("for bitti")

# sehir="Ardahan"
# for i in sehir:
#     print(i)

