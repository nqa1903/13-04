from bs4 import BeautifulSoup
import requests
url= requests.get("https://hoccode.org/html-la-gi-html-la-gi-khai-niem-ve-html")
soup = BeautifulSoup(url.content,'lxml')
ss = soup.find_all(True , limit=1)
for a in ss:
    print(a.text)