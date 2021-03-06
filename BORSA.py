import requests
from bs4 import BeautifulSoup

url = "https://kur.doviz.com/"

response = requests.get(url)

html_icerik = response.content

soup = BeautifulSoup(html_icerik,"html.parser")

sembol = soup.find_all("td")
alıs = soup.find_all("td",{"class":"text-bold"})
satıs = soup.find_all("td",{"class":""})



for isim,rakam1,  in zip(sembol,alıs):
    isim = isim.text
    rakam1 = rakam1.text


    isim = isim.strip()
    isim = isim.replace("\n","")

    rakam1 = rakam1.strip()
    rakam1 = rakam1.replace("\n","")


    print(isim,rakam1,)
    print("************************************************************")
