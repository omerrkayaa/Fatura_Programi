import os
import xml.etree.ElementTree as ET
import pandas as pd

XML_KLASORU = 'xmller'
GRUP_DOSYASI = 'urungruplari.txt'
CIKTI_EXCEL = 'Fatura_Analiz_Raporu.xlsx'

NS = {
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
}

def degeri_bul(element, paths, ns):
    for path in paths:
        found = element.find(path, ns)
        if found is not None and found.text:
            return found.text
    return "0"

def gruplari_yukle():
    gruplar = {}
    if os.path.exists(GRUP_DOSYASI):
        with open(GRUP_DOSYASI, 'r', encoding='utf-8') as f:
            for satir in f:
                if ':' in satir:
                    anahtar, deger = satir.split(':', 1)
                    gruplar[anahtar.strip().lower()] = deger.strip()
    return gruplar

def ana_program():
    print("="*40)
    print("FATURA ANALIZI BASLATILIYOR...")
    print("="*40)
    
    urun_sozlugu = gruplari_yukle()
    veriler = []

    if not os.path.exists(XML_KLASORU):
        print(f"HATA: '{XML_KLASORU}' klasoru bulunamadi!")
        return

    for dosya in os.listdir(XML_KLASORU):
        if dosya.endswith('.xml'):
            try:
                tree = ET.parse(os.path.join(XML_KLASORU, dosya))
                root = tree.getroot()

                fatura_no = degeri_bul(root, ['cbc:ID'], NS)
                tarih = degeri_bul(root, ['cbc:IssueDate'], NS)
                
                for line in root.findall('cac:InvoiceLine', NS):
                    urun_adi = degeri_bul(line, ['cac:Item/cbc:Name'], NS)
                    
                    matrah_str = degeri_bul(line, ['cbc:LineExtensionAmount', 'cac:Price/cbc:PriceAmount', './/cbc:Amount'], NS)
                    matrah = float(matrah_str.replace(',', '.'))

                    kdv_oran_str = degeri_bul(line, ['.//cac:TaxCategory/cbc:Percent', './/cac:TaxTotal//cbc:Percent'], NS)
                    kdv_oran = float(kdv_oran_str.replace(',', '.'))
                    
                    kdv_tutari = (matrah * kdv_oran) / 100
                    genel_toplam = matrah + kdv_tutari
                    
                    grup = "Diger"
                    for anahtar, deger in urun_sozlugu.items():
                        if anahtar in urun_adi.lower():
                            grup = deger
                            break

                    veriler.append({
                        'TARİH': tarih,
                        'BELGE TÜRÜ': 'E-Fatura',
                        'FATURA NO': fatura_no,
                        'ÜRÜN CİNSİ': urun_adi,
                        'ÜRÜN GRUBU': grup,
                        'KDV (%)': f"%{int(kdv_oran)}",
                        'GENEL TOPLAM': round(genel_toplam, 2),
                        'MATRAH': round(matrah, 2),
                        'KDV TUTARI': round(kdv_tutari, 2)
                    })
                print(f"[BASARILI] {dosya} islendi.")
            except Exception as e:
                print(f"[HATA] {dosya}: {e}")

    if veriler:
        df = pd.DataFrame(veriler)
        df.to_excel(CIKTI_EXCEL, index=False)
        print("="*40)
        print(f"ISLEM TAMAM! '{CIKTI_EXCEL}' dosyasi olusturuldu.")
    else:
        print("Veri bulunamadi.")
    
    input("\nKapatmak icin Enter'a basin...")

if __name__ == "__main__":
    ana_program()