# Ödev :
#  Kullanıcıdan 1-12 arası sayı alın.
# Alınan sayıya göre ayları islami isimlerini yazdırın


ay_sayisi: int= int(input("Lütfen 1 ile 12 arasında bir sayı seçiniz: "))

if (ay_sayisi >12) or (ay_sayisi <1):
    print("Girmiş oldunuz sayı 12 den büyük veya 1 den küçük olamaz")
elif ay_sayisi == 1:
    print("Muharrem")
elif ay_sayisi == 2:
    print("Safer")
elif ay_sayisi == 3:
    print("Rebiülevvel")
elif ay_sayisi == 4:
    print("Rebiülahir")
elif ay_sayisi == 5:
    print("Cemaziyelevvel")
elif ay_sayisi == 6:
    print("	Cemaziyelahir")
elif ay_sayisi == 7:
    print("Recep")
elif ay_sayisi == 8:
    print("	Şaban")
elif ay_sayisi == 9:
    print("	Ramazan")
elif ay_sayisi == 10:
    print("Şevval")
elif ay_sayisi == 11:
    print("	Zilkade")
elif ay_sayisi == 12:
    print("Zilhicce")