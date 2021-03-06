import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

a = float(input("Ratingi giriniz:"))

baslıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})


for baslık,rating in zip(baslıklar,ratingler):
    baslık = baslık.text
    rating = rating.text

    baslık = baslık.strip()
    baslık = baslık.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Film İsmi: {} Filmin Ratingi: {}".format(baslık,rating))
        print("**********************************************************************************************************")

