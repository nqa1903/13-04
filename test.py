from bs4 import BeautifulSoup

with open('teachers.xml', 'r') as f:
	file = f.read()
soup = BeautifulSoup(file,'lxml')

names = soup.find_all(True,limit=1)
for name in names:
    print(name.text)