import random
import string


# (Varsayılan değer 8)
def sifre_olusturucu(uzunluk=8):
    karakterler = string.ascii_letters + string.digits + string.punctuation

    # List comprehension + join 
    sifre = "".join(random.choice(karakterler) for i in range(uzunluk))
    return sifre


print("--- 🔐 SİBER KASA V1.0 ---")

while True:
    try:
        # ADIM 1: Veriyi direkt int() yapmadan, ham haliyle (string) alıyoruz.
        giris = input("\nŞifre uzunluğu kaç olsun? (Varsayılan 8 için Enter'a bas, Çıkış 'q'): ").strip()

        # Çıkış kontrolü
        if giris.lower() == 'q':
            print("Sistem kapatılıyor...")
            break

        # ADIM 2: Eğer giriş BOŞSA (Yani Enter'a basıldıysa)
        if giris == "":
            print(f"Varsayılan uzunluk kullanılıyor...")
            yeni_sifre = sifre_olusturucu()  # Parametre göndermedik -> 8 oldu
            print(f"✅ Oluşturulan Şifre: {yeni_sifre}")

        # ADIM 3: Eğer giriş DOLUYSA
        else:
            # Şimdi sayıya çevirmeyi deneyebiliriz
            sayi_uzunluk = int(giris)

            # Negatif sayı veya 0 girerse uyaralım
            if sayi_uzunluk <= 0:
                print("⚠️ Hata: Şifre uzunluğu en az 1 olmalı!")
            else:
                yeni_sifre = sifre_olusturucu(sayi_uzunluk)
                print(f"✅ Oluşturulan Şifre: {yeni_sifre}")

    except ValueError:
        # int(giris) başarısız olursa (Örn: 'abc' yazarsa) buraya düşer
        print("❌ Hata: Lütfen sadece sayı giriniz veya Enter'a basınız.")
