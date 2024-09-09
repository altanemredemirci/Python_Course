############### RANDOM KÜTÜPHANESİ ################

# Belirtilen aralıklarda Rastgele sayılar üretir.

import random
import time

# print(random.random()) # 0-1 aralığında rastgele bir sayı verir.

# i = random.randint(1,5) # belirtilen aralıkta rastgele int(tamsayı) verir.

# i = random.uniform(1.5,5.75) #belirtilen aralıkta rastgele float(ondalıklısayı) verir.

# i = random.randrange(1,5) # belirtilen aralıkta rastgele int(tamsayı) verir ama max değeri vermez.

# i = random.randrange(1,10,2) ## belirtilen aralıkta ve artış miktarıyla rastgele int(tamsayı) verir

# print(i)

####### ÖDEV #######
"""
# Aynı soruyu 1-100 arasında sayı üreterek. 6 hak ile yapınız.
# Farklı olarak daha büyük,daha küçük sayı giriniz gibi yönerge olsun.
"""
import random
rastgele = random.randint(1,100)

# for hak in range(6):
#     tahmin=int(input("Tahmininiz:"))
#
#     if tahmin==rastgele:
#         print("Tebrikler")
#         break
#     elif hak==5:
#         print("Hakkınız Bitti")
#         time.sleep(3)
#     elif tahmin>rastgele:
#         print("Tahmininizi Küçültünüz")
#     else:
#         print("Tahmininizi Büyültünüz")

### WHILE ÇÖZÜMÜ
# hak=0
# while hak<6:
#     tahmin=int(input("Tahmininiz:"))
#     hak+=1
#     if tahmin==rastgele:
#         print("Tebrikler")
#         break
#     elif hak==6:
#         print("Hakkınız Bitti")
#         time.sleep(3)
#         hak=0
#     elif tahmin>rastgele:
#         print("Tahmininizi Küçültünüz")
#     else:
#         print("Tahmininizi Büyültünüz")




# Klavyeden girilen metnin harflerinin ASCII tablosundaki sayısal değerleri toplamını bulan program.

# print(ord("A")) # Verilen değerin bilgisayar tarafında ASCII numarasını yazdırır.
# print(ord("a")) # Verilen değerin bilgisayar tarafında ASCII numarasını yazdırır.

# metin = input("Metin giriniz")
# toplam=0
# for harf in metin:
#     print(ord(harf))
#     toplam+=ord(harf)
#
# print(toplam)

print(chr(97))
