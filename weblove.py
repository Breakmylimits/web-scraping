from urllib.request import urlopen as req 
from bs4 import BeautifulSoup as soup 

url = 'https://www.facebook.com/people/Thawatchai-Nunak/100009257463458'

webopen = req(url)
page_html = webopen.read()
webopen.close()

#print(page_html)

data =soup(page_html, 'html.parser')

midia = data.findAll('div', {'class', 'mediaPageName'})


try:
    print(f'ดนตรีที่ชอบ : {midia[0].text}               ')
    print('.'*50)
except:
    pass
try:
    print(f'หนังสือที่ชอบ : {midia[1].text}')
    print('.'*50)
except:
    pass
try:
    print(f'รายการทีวีที่ชอบ : {midia[2].text}')
    print('.'*50)
except:
    pass
try:
    print(f'เกมที่ชอบ : {midia[3].text}')
    print('.'*50)
except:
    pass
try:
    print(f'กีฬาที่ชอบ : {midia[4].text}')
    print('.'*50)
except:
    pass




#province =data.findAll('span', {'class':'title'})
#pv = province[0].text.replace(' ','')
#tp =temp[0].text
#print(f'จังหวัด:{pv} อุณหภูมิ:{tp}')
