from bs4 import BeautifulSoup
import pandas as pd
import lxml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time

w = webdriver.Chrome("chromedriver.exe")
w.get('https://agent.studyinturkey.com/')
username = w.find_element_by_id("userSigninLogin")
password = w.find_element_by_id("userSigninPassword")
username.send_keys("turkey study center")
password.send_keys("TSCintoffice123!")
time.sleep(5)
w.find_element_by_css_selector("button[type='submit']").click()
time.sleep(5)
headers = ["Program","University Name","Program Detail","Price"]
mydata = pd.DataFrame(columns = headers)
w.get('https://agent.studyinturkey.com/dashboard/programs?page=1') #523 sayfa var 
time.sleep(1)
currentPageSource=w.page_source
time.sleep(1)
soup = BeautifulSoup(currentPageSource, 'lxml')
table1 = soup.find_all("span", {"class":"mt-action-author"})
table2 = soup.find_all("div", {"class":"mt-action-desc"})
time.sleep(1)

sayfa=0
while sayfa<524:
    if(sayfa!=0):
        w.get('https://agent.studyinturkey.com/dashboard/programs?page='+str(sayfa))
        time.sleep(1)
        currentPageSource=w.page_source
        soup = BeautifulSoup(currentPageSource, 'lxml')
        table1 = soup.find_all("span", {"class":"mt-action-author"})
        table2 = soup.find_all("p", {"class":"mt-action-desc"})
    #Create a for loop to fill mydata
    for i in range(0,10):
        try:
            Data=[]
            data1=(table1[i].get_text()).strip()
            data2=[ " ".join(txt.text.split()) for txt in table2]
            Data.append(data1)
            Data=Data+(data2[(3*i):(3*i)+3])
            print(Data)
            mydata.loc[len(mydata)] = Data
        except Exception as e:
            mydata.to_excel("sayfa-"+str(sayfa)+".xlsx")
            print("hata sebebi: ")
            print(e)
            break
    mydata.to_excel("sayfa-"+str(sayfa)+".xlsx")
    sayfa=sayfa+1

mydata.to_excel("sayfa.xlsx")