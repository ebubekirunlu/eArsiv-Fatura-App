import pandas as pd

# Excel dosyasını oku
excel_data = pd.read_csv('faturalar.csv')

# İstenilen sütunları seç ve verileri değişkenlere aktar
faturaTarihleri = excel_data['faturaTarihi']
vergiNumaralari = excel_data['vergiNumarasi']
ulkeSecimleri = excel_data['ulkeSecimi']
faturaAdresleri = excel_data['faturaAdresi']
urunAdlari = excel_data['urunAdi']
urunMiktarlari = excel_data['urunMiktari']
urunBirimleri = excel_data['urunBirimi']
birimFiyatlar = excel_data['birimFiyati']
kdvOranlari = excel_data['kdvOrani']

# Her satırdaki verileri ekrana yazdır
for i in range(len(faturaTarihleri)):
    print("Satır", i+1)
    print("faturaTarihi:", faturaTarihleri[i])
    print("vergiNumarasi:", vergiNumaralari[i])
    print("ulkeSecimi:", ulkeSecimleri[i])
    print("faturaAdresi:", faturaAdresleri[i])
    print("urunAdi:", urunAdlari[i])
    print("urunMiktari:", urunMiktarlari[i])
    print("urunBirimi:", urunBirimleri[i])
    print("birimFiyati:", birimFiyatlar[i])
    print("kdvOrani:", kdvOranlari[i])
    print("-------------------------")
 print("Satır", i+1)
    print("faturaTarihi:", faturaTarihleri[i])
    print("vergiNumarasi:", vergiNumaralari[i])
    print("ulkeSecimi:", ulkeSecimleri[i])
    print("faturaAdresi:", faturaAdresleri[i])
    print("urunAdi:", urunAdlari[i])
    print("urunMiktari:", urunMiktarlari[i])
    print("urunBirimi:", urunBirimleri[i])
    print("birimFiyati:", birimFiyatlar[i])
    print("kdvOrani:", )
    print("-----------------kdvOranlari[i]--------")

faturaTarihleri[i],
vergiNumaralari[i],
ulkeSecimleri[i],
faturaAdresleri[i],
urunAdlari[i],
urunMiktarlari[i],
urunBirimleri[i],
birimFiyatlar[i],
kdvOranlari[i]