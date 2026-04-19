istihbarat = [
    {"kod_adi": "SiyahŞapka", "suc": "DDoS", "tehlike": 8, "konum": "İstanbul"},
    {"kod_adi": "Gölge", "suc": "Phishing", "tehlike": 5, "konum": "Ankara"},
    {"kod_adi": "Kripto", "suc": "Fidye Yazılımı", "tehlike": 9, "konum": "İstanbul"},
    {"kod_adi": "Çaylak", "suc": "Wifi Sızma", "tehlike": 3, "konum": "İzmir"}
]

# GÖREV 1: Kayıt Ekleme (Burası harikaydı, aynen korudum)
istihbarat.append({"kod_adi": "Hayalet", "suc": "Veri Sızıntısı", "tehlike": 7, "konum": "Ankara"})

# --- GÖREV 2: SORGULAMA (Arama Motoru) ---
print("\n--- 🔍 ARAMA SONUÇLARI ---")
aranan_sehir = input("Hangi şehirde arama yapılacak? (Örn: İstanbul): ").strip().capitalize()

bulunan_sayisi = 0 # Hiç suçlu bulamazsak uyarmak için sayaç

# 'suclu' değişkeni her turda sıradaki sözlüğü (kişiyi) temsil eder
for suclu in istihbarat:
    # 1. Önce bu kişinin konumuna bakalım
    if suclu["konum"] == aranan_sehir:
        # 2. Eşleşme varsa adını yazdıralım
        print(f"🚨 TESPİT EDİLDİ: {suclu['kod_adi']} ({suclu['suc']})")
        bulunan_sayisi += 1

# Döngü bitti, eğer sayaç hala 0 ise kimse bulunamadı demektir.
if bulunan_sayisi == 0:
    print(f"❌ {aranan_sehir} konumunda tehdit bulunamadı.")


# --- GÖREV 3: ANALİZ (Filtreleme) ---
print("\n--- ⚠️ KRİTİK TEHDİT RAPORU (Tehlike >= 7) ---")

for tehdit in istihbarat:
    # Tehlike puanını kontrol et (Sayısal karşılaştırma)
    if tehdit["tehlike"] >= 7:
        print(f"🔥 YÜKSEK RİSK: {tehdit['kod_adi']} - Seviye: {tehdit['tehlike']}")
