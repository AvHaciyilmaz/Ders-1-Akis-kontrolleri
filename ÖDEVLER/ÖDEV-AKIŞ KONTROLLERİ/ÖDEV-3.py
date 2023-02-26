# ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
# not aralığı 0 ile 100 arasında olmalıdır.
# vize ve finalin ortalaması alınsın.
# 0-44 : Kaldınız
# 45-69: Geçtiniz
# 70-84: İyi
# 85-100: Pekiyi

s1: float = float(input("Vize Notunuz: "))
s2: float = float(input("Final Notunuz: "))

ortalama = (s1+s2)/2

if (0 <= s1 <= 100) and (0 <= s2 <= 100):

    if 0 <= ortalama and ortalama <= 44:
        print("Kaldınız")
    elif 45 <= ortalama and ortalama <= 69:
        print("Geçtiniz")
    elif 70 <= ortalama and ortalama <= 84:
        print("İyi")
    elif 85 <= ortalama and ortalama <= 100:
        print("Pekiyi")

print(f"Ortalamanız: {ortalama}")
