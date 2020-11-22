from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup 

url = 'https://www.facebook.com/mark.regulators'

webopen = req(url)
page_html = webopen.read()
webopen.close()

#print(page_html)

data =soup(page_html, 'html.parser')

midia = data.findAll('div', {'class', 'mediaPageName'})
print(midia[0].text)

#province =data.findAll('span', {'class':'title'})
#pv = province[0].text.replace(' ','')
#tp =temp[0].text
#print(f'จังหวัด:{pv} อุณหภูมิ:{tp}')
