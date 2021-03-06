import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=ANKARA"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

for i in soup.find_all("a"):
    print(i)
    print("**************************************")