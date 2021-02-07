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
    ## MAY NEED TO INSERT SIGN-IN CREDENTIALS FROM ratings_scrape NOTEBOOK ##
    if 'Overview' in url:
        try: #webpage layout 1: (Google, Microsoft, Apple, etc)
            r.html.page.click('//*[@id="EIOverviewContainer"]/div/div[3]/div[1]/div[2]')
            time.sleep(3)
        
            rating_overall = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div[3]').text
            rating_DI = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[3]/div/div[3]').text
            rating_CV = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/div[3]').text
            rating_WL = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[4]/div/div[3]').text
            rating_SM = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div[3]').text
            rating_CB = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[6]/div/div[3]').text
            rating_CO = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[7]/div/div[3]').text

            print(rating_overall, rating_DI, rating_CV, rating_WL, rating_SM, rating_CB, rating_CO)
            time.sleep(np.random.choice([x/10 for x in range(7,20)]))
    
        except: #webpage layout 2: (Cisco, Capital One, etc)
            r = s.get(url) #recalling url
            time.sleep(2)
            r.html.xpath('//*[@id="EIOverviewContainer"]/div/div[4]/div[1]/div[2]').click()
            rating_overall = r.html.xpath('//*[@id="reviewDetailsModal"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[1]/div/div[3]').text

            ### INSERT ADDITIONAL RATINGS HERE
            print(rating_overall)
            time.sleep(np.random.choice([x/10 for x in range(7,15)]))

        print('SUCCESS')
