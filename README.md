# E-Fatura Analiz Projesi 🧾

Bu proje, XML formatındaki e-faturaları otomatik olarak okuyup, içerisindeki ürünleri belirli kategorilere göre gruplandırarak bir Excel raporu (`Fatura_Analiz_Raporu.xlsx`) oluşturur.

## 🚀 Özellikler

* **Otomatik XML İşleme:** Belirlenen klasördeki tüm e-faturaları toplu halde okur.
* **Akıllı Gruplandırma:** `urungruplari.txt` dosyasındaki anahtar kelimelere göre ürünleri (Takviye Gıda, Vitamin vb.) otomatik sınıflandırır.
* **Finansal Hesaplama:** Matrah, KDV oranı ve Genel Toplam verilerini hatasız ayrıştırır.
* **Excel Raporlama:** Tüm verileri düzenli bir tablo halinde dışa aktarır.

## 📂 Dosya Yapısı

* `fatura_oku.py`: Analiz işlemini yapan ana Python kodu.
* `urungruplari.txt`: Ürünlerin hangi gruba gireceğini belirleyen tanımlama dosyası.
* `xmller/`: İşlenecek XML faturalarının konulacağı klasör.
* `Fatura_Projesi_Final.exe`: Python yüklü olmayan bilgisayarlar için taşınabilir uygulama.

## 🛠 Kullanım

1.  **Hazırlık:** Analiz etmek istediğiniz XML faturalarını `xmller` isimli bir klasöre kopyalayın.
2.  **Gruplandırma:** `urungruplari.txt` dosyasını açarak ürün anahtar kelimelerini şu formatta düzenleyin: `Marka/Ürün:Grup Adı` (Örn: `Suda:Takviye Gıda`).
3.  **Çalıştırma:** * İster `fatura_oku.py` dosyasını çalıştırın,
    * İsterseniz de `Fatura_Projesi_Final.exe` dosyasına çift tıklayın.
4.  **Sonuç:** İşlem bittiğinde aynı klasörde `Fatura_Analiz_Raporu.xlsx` dosyası oluşacaktır.

## 📦 Gereksinimler (Python için)

Kodun çalışması için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install pandas openpyxl