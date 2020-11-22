from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup 

url = 'https://www.tmd.go.th/province.php?StationNumber=48569'

webopen = req(url)
page_html = webopen.read()
webopen.close()

#print(page_html)

data =soup(page_html, 'html.parser')

temp = data.findAll('td', {'class', 'strokeme'})
province =data.findAll('span', {'class':'title'})
pv = province[0].text.replace(' ','')
tp =temp[0].text
print(f'จังหวัด:{pv} อุณหภูมิ:{tp}')
