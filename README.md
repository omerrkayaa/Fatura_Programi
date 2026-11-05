# E-Fatura Analiz Programı

XML formatındaki (UBL-TR) e-faturaları toplu olarak okur, her fatura satırını anahtar kelimelere göre bir ürün grubuna atar ve sonucu `Fatura_Analiz_Raporu.xlsx` adında bir Excel raporu olarak kaydeder.

## Özellikler

- **Toplu işleme:** `xmller/` klasöründeki bütün `.xml` dosyalarını okur. Bozuk bir dosya yüzünden işlem durmaz; o dosya atlanır ve hatası ekrana yazılır.
- **Gruplandırma:** `urungruplari.txt` içindeki `anahtar:grup` satırlarına göre ürün adında geçen kelimeyi arar (büyük/küçük harf fark etmez). Eşleşmeyen ürün "Diger" grubuna düşer.
- **Tutarlar:** satır başına matrah, KDV oranı, KDV tutarı ve genel toplam. KDV tutarı faturada yazıyorsa o kullanılır, yoksa matrah ve orandan hesaplanır.
- **Güvenli XML okuma:** dışarıdan gelen dosyalar `defusedxml` ile okunur. Böylece varlık genişletme (billion laughs) ve dış varlık (XXE) içeren zararlı XML'ler reddedilir.

## Kullanım

```bash
pip install -r requirements.txt
mkdir xmller
cp ornek/ornek_fatura.xml xmller/     # denemek için örnek fatura; kendi faturalarınızı da buraya koyun
python fatura_oku.py
```

Rapor aynı klasörde `Fatura_Analiz_Raporu.xlsx` olarak oluşur.

`urungruplari.txt` biçimi (her satıra bir kural):

```
Suda:Takviye Gıda
Youplus:Vitamin
```

## Python yüklü olmayan bilgisayarlar için

PyInstaller ile tek dosyalık bir `.exe` üretilebilir. Üretilen dosya depoya eklenmez.

```bash
pip install pyinstaller
pyinstaller --onefile --name Fatura_Projesi_Final fatura_oku.py
```

`.exe` dosyası `dist/` klasöründe oluşur. Yanına `urungruplari.txt` ve `xmller/` klasörü konmalıdır.

## Gizlilik

Gerçek faturalar kişisel ve ticari bilgi içerir. Bu yüzden `xmller/` klasörü ve üretilen Excel dosyaları `.gitignore` ile depo dışında tutulur. `ornek/` altındaki fatura uydurmadır.
