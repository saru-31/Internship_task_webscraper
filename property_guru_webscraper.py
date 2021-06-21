import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import pprint as pp
from collections import OrderedDict


driver=webdriver.Chrome('C:/Users/sarve/chromedriver.exe')
url = 'http://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'

driver.get(url)
content=driver.page_source
tryl=int(driver.find_element_by_id('currentpage').get_attribute("value"))
prevHt=driver.execute_script("return document.body.scrollHeight")
#
while tryl < 20:
    
    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
    tryl=int(driver.find_element_by_id('currentpage').get_attribute("value"))
time.sleep(5)
ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
for tr in targets:
    print(tr.text)
        
bsp=BeautifulSoup(content,"html.parser")
ad_title=[]
ad_addr=[]
prp_price=[]
prp_rate=[]
prp_area=[]
prp_facing_dir=[]
prp_status=[]
prp_details=[]
prp_owner=[]
ad_posted_on=[]

for i in range(len(targets)):
    filt_wrds = {'featured','area','facing','status','at','request details'}
    resultwords  = [word for word in targets[i].text.split('\n') if word.lower() not in filt_wrds]
    arr= resultwords
    #print(resultwords)
    ad_title.append(arr[0])
    ad_addr.append(arr[1])
    prp_price.append(arr[2])
    prp_rate.append(arr[3])
    prp_area.append(arr[4])
    prp_facing_dir.append(arr[5])
    prp_status.append(arr[6])
    prp_details.append(arr[7]+', '+arr[8]+', '+arr[9])
    prp_owner.append(arr[10])
    ad_posted_on.append(arr[11])

df=pd.DataFrame(zip(ad_title,ad_addr,prp_price,prp_rate,prp_area,prp_facing_dir,prp_status,prp_details,prp_owner,ad_posted_on),columns=['Title','Address','property_price','rate','area','Direction_facing','status','details','owner_name','post_date'],)
df.to_csv('file1.csv')

##---------------next-task-------------------------------
driver.execute_script('window.scrollTo(0,0);')
url = 'http://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'

driver.get(url)
resettr=driver.find_element_by_id("resetsearch")
resettr.click()
temp=[]
temp=driver.find_elements_by_name('rooms-no')
bhk=driver.find_elements_by_id("navbarDropdownMenuLink")
ActionChains(driver).click(bhk[2]).perform()
ActionChains(driver).click(temp[2]).perform()
ActionChains(driver).click(temp[3]).perform()
time.sleep(3)
bhk=driver.find_elements_by_id("navbarDropdownMenuLink")
ActionChains(driver).click(bhk[2]).perform()

#btn=driver.find_elements_by_xpath('//div[@class="multi-search-btn"]')
#
#ActionChains(driver).click(btn).perform()

content=driver.page_source
tryl=driver.find_element_by_id('currentpage').get_attribute("value")
prevHt=driver.execute_script("return document.body.scrollHeight")
time.sleep(5)
while tryl!=40:
    
    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)

    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
    tryl=int(driver.find_element_by_id('currentpage').get_attribute("value"))
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(5)
ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
for tr in targets:
    print(tr.text)

time.sleep(5)       
bsp=BeautifulSoup(content,"html.parser")
n_ad_title=[]
n_ad_addr=[]
n_ad_url=[]
n_prp_price=[]
n_prp_rate=[]
n_prp_img_url=[]
n_prp_area=[]
n_prp_facing_dir=[]
n_prp_status=[]
n_prp_details=[]
n_prp_owner=[]
n_ad_posted_on=[]

for i in range(len(targets)):
    filt_wrds = {'featured','area','facing','status','at','request details'}
    resultwords  = [word for word in targets[i].text.split('\n') if word.lower() not in filt_wrds]
    arr= resultwords
    #print(resultwords)
    n_ad_title.append(arr[0])
    n_ad_addr.append(arr[1])
    n_prp_price.append(arr[2])
    n_prp_rate.append(arr[3])
    n_prp_area.append(arr[4])
    n_prp_facing_dir.append(arr[5])
    n_prp_status.append(arr[6])
    n_prp_details.append(arr[7]+', '+arr[8]+', '+arr[9])
    n_prp_owner.append(arr[10])
    n_ad_posted_on.append(arr[11])

df=pd.DataFrame(zip(n_ad_title,n_ad_addr,n_prp_price,n_prp_rate,n_prp_area,n_prp_facing_dir,n_prp_status,n_prp_details,n_prp_owner,n_ad_posted_on),columns=['Title','Address','property_price','rate','area','Direction_facing','status','details','owner_name','post_date'])
df.to_csv('file2.csv')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
##import numpy as np
##import pandas as pd
##from bs4 import BeautifulSoup
##
##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##from selenium.common.exceptions import NoSuchElementException
##from selenium.webdriver.common.action_chains import ActionChains
##import time
##import csv
##import pprint as pp
##from collections import OrderedDict
##
##
##driver=webdriver.Chrome('C:/Users/sarve/chromedriver.exe')
##url = 'http://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'
##
##driver.get(url)
##content=driver.page_source
##tryl=int(driver.find_element_by_id('currentpage').get_attribute("value"))
##prevHt=driver.execute_script("return document.body.scrollHeight")
###
##while tryl < 20:
##    
##    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
##    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
##    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
##    tryl=int(driver.find_element_by_id('currentpage').get_attribute("value"))
##for tr in targets:
##    print(tr.text)
##        
##bsp=BeautifulSoup(content,"html.parser")
##ad_title=[]
##ad_addr=[]
##ad_url=[]
##prp_price=[]
##prp_rate=[]
##prp_img_url=[]
##prp_area=[]
##prp_facing_dir=[]
##prp_status=[]
##prp_details=[]
##prp_owner=[]
##ad_posted_on=[]
##
##for i in range(len(targets)):
##   arr= targets[i].text.split('\n')
##   ad_title.append(arr[0])
##   ad_addr.append(arr[1])
##   ad_url.append(arr[2])
##   prp_price.append(arr[3])
##   prp_rate.append(arr[4])
##   prp_img_url.append(arr[5])
##   prp_area.append(arr[6])
##   prp_facing_dir.append(arr[7])
##   prp_status.append(arr[8])
##   prp_details.append(arr[9])
##   prp_owner.append(arr[10])
##   ad_posted_on.append(arr[11])
###---------------next-task-------------------------------
##resettr=driver.find_element_by_id("resetsearch")
##resettr.click()
##temp=[]
##temp=driver.find_elements_by_name('rooms-no')
##bhk=driver.find_elements_by_id("navbarDropdownMenuLink")
##ActionChains(driver).click(bhk[2]).perform()
##ActionChains(driver).click(temp[2]).perform()
##
##ActionChains(driver).click(temp[3]).perform()
##
##content=driver.page_source
##tryl=driver.find_element_by_id('currentpage').get_attribute("value")
##prevHt=driver.execute_script("return document.body.scrollHeight")
###
##while tryl!=40:
##    
##    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
##    driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
##    targets=driver.find_elements_by_xpath('//div[@class="filter-property-list detailurl"]')
##    tryl=driver.find_element_by_id('currentpage').get_attribute("value")
##for tr in targets:
##    print(tr.text)
##        
##bsp=BeautifulSoup(content,"html.parser")
##n_ad_title=[]
##n_ad_addr=[]
##n_ad_url=[]
##n_prp_price=[]
##n_prp_rate=[]
##n_prp_img_url=[]
##n_prp_area=[]
##n_prp_facing_dir=[]
##n_prp_status=[]
##n_prp_details=[]
##n_prp_owner=[]
##n_ad_posted_on=[]
##
##for i in range(len(targets)):
##   arr= targets[i].text.split('\n')
##   n_ad_title.append(arr[0])
##   n_ad_addr.append(arr[1])
##   n_ad_url.append(arr[2])
##   n_prp_price.append(arr[3])
##   n_prp_rate.append(arr[4])
##   n_prp_img_url.append(arr[5])
##   n_prp_area.append(arr[6])
##   n_prp_facing_dir.append(arr[7])
##   n_prp_status.append(arr[8])
##   n_prp_details.append(arr[9])
##   n_prp_owner.append(arr[10])
##   n_ad_posted_on.append(arr[11])
###while True
##    #print(driver.find_element_by_xpath('//div[@class="filter-property-list detailurl"]').text)
##
###bsp=BeautifulSoup(content,"html.parser")
###advert.append(bsp.find_all('div', attrs={'class': 'filter-property-list detailurl'}))
###driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
###content=driver.page_source
###print(driver.find_element_by_xpath('//div[@class="filter-property-list detailurl"]').text)
####resp=requests.get(url)
###bsp=BeautifulSoup(content,"html.parser")
###advert.append(bsp.find_all('div', attrs={'class': 'filter-property-list detailurl'}))
###driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
###content=driver.page_source
###print(driver.find_element_by_xpath('//div[@class="filter-property-list detailurl"]').text)
####resp=requests.get(url)
###bsp=BeautifulSoup(content,"html.parser")
###advert.append(bsp.find_all('div', attrs={'class': 'filter-property-list detailurl'}))
###driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
###content=driver.page_source
###print(driver.find_element_by_xpath('//div[@class="filter-property-list detailurl"]').text)
####resp=requests.get(url)
###bsp=BeautifulSoup(content,"html.parser")
###advert.append(bsp.find_all('div', attrs={'class': 'filter-property-list detailurl'}))
###driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
##print(advert)
##print(driver.page_source)