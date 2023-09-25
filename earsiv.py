from bs4 import BeautifulSoup
import pandas as pd
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os, time

#degisken tanimlamalari
#earsiv giris bilgileri
kullaniciAdi="xxxxx"
kullaniciSifre="xxxxxx"

# Excel dosyasını oku
excel_data = pd.read_csv('faturalar.csv',dtype=str)

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

#giris islemleri
w = webdriver.Chrome("chromedriver.exe")
w.get('https://earsivportal.efatura.gov.tr/intragiris.html')
username = w.find_element_by_id("userid")
password = w.find_element_by_id("password")
username.send_keys(kullaniciAdi)
password.send_keys(kullaniciSifre)
w.find_element_by_css_selector("button[type='submit']").click()
time.sleep(2)

#e arsiv modül secimi
select = Select(w.find_element_by_css_selector("div[rel='selectProject'] select"))
select.select_by_visible_text('e-Arşiv Portal')
time.sleep(0.5)

#menuden Belge işlemlerinin açılması 
w.find_element(By.LINK_TEXT, "Belge İşlemleri").click()

def faturaOlustur(faturaTarihi, vergiNumarasi, ulkeSecimi, faturaAdresi, urunAdi, urunMiktari, urunBirimi, birimFiyat, kdvOrani):
    #fatura olusturma ekranin acilmasi 
    w.find_element(By.LINK_TEXT, "e-Arşiv Fatura (İnteraktif) Oluştur").click()
    time.sleep(1)

    #Tarih elementinin secilip düzenlenebilir hale getirilmesi ve düzenlenmesi
    element = w.find_element_by_css_selector("td[rel='faturaTarihi'] input")
    time.sleep(1)
    w.execute_script("arguments[0].removeAttribute('disabled')", element)
    time.sleep(1)
    element.click()
    element.send_keys(faturaTarihi) #tarih degiskeni gelecek

    #Fatura bilgilerinin secimi ve doldurulmasi 
    input_element = w.find_element_by_css_selector("td[rel='vknTckn'] input")
    input_element.send_keys(vergiNumarasi) #vergi numarasi degiskeni gelecek

    select = Select(w.find_element_by_css_selector("td[rel='ulke'] select"))
    select.select_by_visible_text(ulkeSecimi) #ülke degiskeni gelecek

    input_element = w.find_element_by_css_selector("td[rel='bulvarcaddesokak'] textarea")
    input_element.send_keys(faturaAdresi) #adres degiskeni gelecek

    #mal hizmet ekleme bölümü
    w.find_element_by_css_selector("input[rel='satirEkle']").click()
    w.find_element_by_css_selector("input[rel='button']").click()
    time.sleep(0.5)
    input_element = w.find_element_by_css_selector("td[rel='malHizmetP'] input")
    input_element.send_keys(urunAdi) #ürün/hizmet adi degiskeni

    input_element = w.find_element_by_css_selector("td[rel='miktarP'] input")
    input_element.send_keys(urunMiktari)#ürün/hizmet miktari degiskeni

    select = Select(w.find_element_by_css_selector("td[rel='birimP'] select"))
    select.select_by_visible_text(urunBirimi)#ürün/hizmet birimi degiskeni

    input_element = w.find_element_by_css_selector("td[rel='birimFiyatP'] input")
    input_element.click()
    time.sleep(0.2)
    input_element.send_keys(birimFiyat)#ürün birim fiyat degiskeni

    select = Select(w.find_element_by_css_selector("td[rel='kdvOraniP'] select"))
    select.select_by_visible_text(kdvOrani)#kdv orani degiskeni
    time.sleep(0.1)

    w.find_element_by_css_selector("td[rel='kapat'] input").click() #ürün/hizmet ekleme formunu kapat butonu
    time.sleep(0.5)

    #w.find_element_by_css_selector("div[rel='olustur'] input").click()

for i in range(len(faturaTarihleri)):
    faturaOlustur(str(faturaTarihleri[i]),
                    str(vergiNumaralari[i]),
                    str(ulkeSecimleri[i]),
                    str(faturaAdresleri[i]),
                    str(urunAdlari[i]),
                    str(urunMiktarlari[i]),
                    str(urunBirimleri[i]),
                    str(birimFiyatlar[i]),
                    str(kdvOranlari[i]))
    time.sleep(10)
