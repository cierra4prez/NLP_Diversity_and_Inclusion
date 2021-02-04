#pip3 install requests-html
#pip3 install selenium

from requests_html import HTMLSession
import selenium
from selenium import webdriver

import time
import numpy as np

url = "https://www.glassdoor.com/Explore/browse-companies.htm?overall_rating_low=0&page=1&isHiringSurge=0" #starting url
s = HTMLSession() #session
r=s.get(url) #response
r.html.render(sleep=1, timeout=20)  #renders page in background

companies = r.html.xpath('//*[@id="ReactCompanyExplorePageContainer"]/div/div/div/div/div[2]', first=True) 

for url in companies.absolute_links:
    r = s.get(url)
    if 'Overview' in url:
        name = r.html.find('div.header.cell.info', first=True).text
        size = r.html.xpath('//*[@id="EIOverviewContainer"]/div/div[1]/ul/li[3]/div', first=True).text
        headquarters = r.html.xpath('//*[@id="EIOverviewContainer"]/div/div[1]/ul/li[2]/div', first=True).text
        industry = r.html.xpath('//*[@id="EIOverviewContainer"]/div/div[1]/ul/li[6]/div', first=True).text
        
        time.sleep(np.random.choice([x/10 for x in range(7,15)]))
        print(name, size, headquarters, industry, mission)
print('SUCCESS')