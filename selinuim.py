from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url= 'https://twitter.com/hashtag/hrk'
driver.get(url)


#elem_search = driver.find_element_by_name('q')
#elem_search.clear()
#elem_search.send_keys('emi fukada')
#elem_search.send_keys(Keys.ENTER)
#css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0