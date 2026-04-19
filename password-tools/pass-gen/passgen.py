import random
import string
import datetime

def guclu_sifre_uret(uzunluk=12):
    """Harf, rakam ve sembollerden oluşan karmaşık şifre üretir"""
    karakterler = string.ascii_letters + string.digits + string.punctuation
    # şifreyi oluşturur
    sifre = "".join(random.choice(karakterler) for i in range(uzunluk))
    return sifre


def sifreyi_kaydet(site_adi, sifre):
    """Şifreyi dosyaya tarihle beraber ekler (Append modu)"""
    zaman = datetime.datetime.now().strftime("%Y-%m-D %H:%M:%S")

    # Dikkat : 'a' modu kullanıyoruz ki eskiler silinmesin!
    with open("sifrelerim.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"[{zaman}] {site_adi} -> {sifre}\n")

    print(f"✅ {site_adi} için şifre başarıyla kaydedildi.")


# --- ANA PROGRAM ---
if __name__ == "__main__":
    print(("--- 🔐 PASSGEN SİBER GÜVENLİK ARACI 🔐 ---"))

    site = input("Şifre hangi site/uygulama için ? : ")
    uzunluk_soru = input("Kaç karakter olsun ? (Boş geçersen 12) : ")

    # Eğet kullanıcı boş geçerse varsayılan 12 olsun
    if uzunluk_soru == "":
        uzunluk = 12
    else:
        uzunluk = int(uzunluk_soru)

    yeni_sifre = guclu_sifre_uret(uzunluk)

    print(f"\nOluşturulan Şifre : {yeni_sifre}")

    kayit_sorusu = input("Dosyaya kaydedilsin mi ? (e/h) : ").lower()


    if kayit_sorusu == "e":
        sifreyi_kaydet(site, yeni_sifre)
    else:
        print("Kayıt edilmedi. Günvelik önemli alındı. 🚫")