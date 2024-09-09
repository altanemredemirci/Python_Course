###      TRY CATCH
"""
try:
    #Hata oluşturma ihtimali olan kodlar
except:
    #Hata oluşması durumunda çalıştırılacak kod bloğu.
"""
# while True:
#     try:
#         sayi = int(input("Sayı:"))
#         print(sayi)
#         print(sayi/2)
#         import Kare
#         break
#
#     except ValueError:
#         print("Lütfen sayıyı RAKAM olarak giriniz")
#
#     except ZeroDivisionError:
#         print("Matematiksel olarak hiç bir sayı 0 a bölünemez.")
#
#     except ModuleNotFoundError:
#         print("Modüle erişim yok!!!")
#
#     except:
#         print("Sistem yöneticiniz ile görüşünüz")
"""
#ValueError: veri tipi uymadığında.
#Import error: içeri aktarılmaya çalışan modül aktarılırken bir hata oluşursa.
#ModuleNotFoundError: içeri aktarılmaya çalışan modül yerinde yoksa bu hata üretilir.
#MemoryError: Bellek programa yetmediği zaman üretilir.
#ZeroDivisionError: 0'a bölünme hatası.
#OverflowError: bir değişkene kapasitesinden fazla değer atamak istediğimizde üretilen hatadır.(int 32 bit ise: 11 basamaklı sayı alamaz.)
#IndexError: 4 elemanlı bir listenin 5. elemanına ulaşmaya çalıştığımızda bu hata ile karşılaşırız.
"""
###################   Hata Tanımlama:Fırlatma   ###################

# El Yordamı İle Hata Fırlatma
# not1=int(input("Ders Notunuz:"))
# if(not1<0 or not1>100):
#     # raise Exception("Not Aralığı Hatalı!!")
#     # raise OverflowError ("Not Aralığı Hatalı!!")
# print(not1)

#ASSERT => iddaa etmek anlamına gelir
# eposta = input("E-posta adresinizi giriniz:")
# assert eposta == "sercan@ucuncubinyil.com" #eposta sercan@ucuncubinyil.com değilse AssertionError üretir.
# print("Eposta'yı doğru girdiniz.")


#################     ALIŞTIRMALAR     #################

# Kullanıcıdan 2 sayı 1 işlem alınız.
# işlem topla,cikar,carp,bol'den birisi değilse assert fırlatsın
# Kullanıcıdan veri alınırken VALUEERROR hatası alınırsa tekrar veri istensin
# ZeroDivisionError hatası alınırsa veri tekrar istenmesin.
while True:
    try:
        num1=int(input("Birinci Sayıyı Giriniz: "))
        num2=int(input("İkinci Sayıyı Giriniz: "))
        sign=input("+, -, *, /, İşaretlerinden Birini Giriniz: ")

        assert sign =="+" or sign=="-" or sign=="*" or sign=="/"

        if sign == "+":
            print(num1+num2)
        elif sign == "-":
            print(num1-num2)
        elif sign == "*":
            print(num1*num2)
        elif sign == "/":
            if num2 == 0:
                raise ZeroDivisionError ("Sayı 0'a Eşit Olamaz")
            else:
                print(num1/num2)
        else:
            print("+, -, *, /, İşaretlerinden Birini Girmediniz !!!!!!")
    except ValueError:
        print("Geçersiz Karakter Girdiniz!! Sayı Giriniz.")
