Linux'u her açtığımızda yapılması gerekler bir kaç işlem vardır. Bunlar :
apt-get clean : bu komut gereksiz güncelleme dosyalarını siler, hafızada yer açar.
apt-get update : bu komut güncellemeleri denetler ve günveller. Ancak kalideki yüklü uygulamaları bu komu güncellemez.
apt-get upgrade : bu komut ise kalideki mevcut uygulamaları günceller. (kaliyi yeni yüklemiş olanlar için tavsiye edilmez, zira çok uzun sürer, bilgisayarı yorar, hatta bilgisayar çöker.)

sudo su : bir oturumluk root yetkisi verir. Terminali kapatınca yetki gider. Ya da yeni bir terminal ekranı açınca yine kali@kali olarak kullanırız. En mantıklı ve güvenli işlemin bu olduğunu söylerler.
Root yetkisini tamamen almak için ise : sodu su komutu ile geçici yetki aıkken "passwd" komutu girilir, new password ister, bu rootun şifresidir. Şifre yazarken güvenlik sebebi ile kararkterler görünmez.

-------------------------------------------------------------------------------------------------------------------

1. ls -l : aktif klasörlerdeki dosya ve klasörün özelliklerini gösterir.
2. pwd : mevcut konumu gösterir. (sızdığımız makinada konumumuz nedir, bunun için kullanırız.)
3. ls [klasör adı] : içerisine girmeden klasörün içine bakmayı sağlar.
4. mkdir [klasör adı] : bu isimle bir klasör oluşturur.
5. rm -r [klasör adı] : bu isimdeki klasörü siler.
6. touch [dosya adı].txt : bu isimde bir .txt dosyası oluşturur.
7. cat [dosya adı].txt : bu isimde .txt dosyasını okumamız için açar.
8. cat -n [dosya adı].txt : uzun metinlerde satırları numaralandırır.
9. cp [kopyalanacak dosya adı] [hedef dosya adı]/ : ilk dosyayı ikincinin içine kopyalar.
10. mv [taşınacak dosya adı] [hedef dosya adı]/ : ilk dosyayı ikincinin içine taşır. NOT : Bu taşıma işlemi sırasında dosyanın adını ve uzantısını da değiştirebiliriz. Mantığı ise mv komutu dosyayı ilk konumundan kaldırıp ikinci konumda baştan oluşturuyor, bu durumda istediğimiz isim ve uzantıda oluşturabiliyoruz.
11. head [dosya adı].txt : çok uzun metinlerde sadece ilk 10 satırı ekrana yazar.
12. uname -a : bilgisayarın işletim sistemi bilgisini verir. (hacklenen makinada sistem bilgisi için kullanılır.
13. whoami : kim olduğumu söyler.
14. wc [dosya adı].txt : bu komut dosyayı açmadan dosya hakkında bilgi verir. Satır bilgisi, dosya büyüklüğü vs.
15. ctrl + c : çalışan bir uygulamayı kapatır. Ör: nmap çalışıyordur istediğimiz anda ctrl+c basarız direkt kapanır.
16. setxkbmap tr -> klavyeyi türkçe yapar.
17. 
