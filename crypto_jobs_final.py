
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import requests
from requests.auth import HTTPBasicAuth
import traceback

import re

def tokens(text):
    "List all the word tokens in a text."
    word_list=re.findall('[\w]+', text.lower())
    sentence=' '.join(word for word in word_list)
    return sentence

driver=webdriver.Chrome('/Users/casper.local/Desktop/Dev/job_listing/chromedriver')

driver.get('https://crypto.jobs/?page=4')

def createIfNotExist(slug,title):


    slug=tokens(slug)
    title=tokens(title)
    url = "https://www.jobs-blockchain.com/wp-json/wp/v2/job_listing"

    payload = "slug="+slug+"&title="+title
    headers = {
        'content-type': "application/x-www-form-urlencoded",

    }

    response = requests.request("POST", url, data=payload, headers=headers,auth=HTTPBasicAuth('BlockchainAsh','AqGv F3EG Fu8c aLsK 5i3d LLHC'))

    print(response.text)
    return  True
while True:
    try:


        job_urls=driver.find_elements(By.XPATH,'//tr[@class="highlighted"]/td[2]/a')
        #job_urls=jobsTr.find_elements(By.XPATH,'//tr/td[2]/a')
        main_window = driver.current_window_handle
        for job_url in job_urls:
            #single_parse(job_url)
            job_url.send_keys(Keys.COMMAND + 't')
            ActionChains(driver).move_to_element(job_url).key_down(Keys.COMMAND).click(job_url).key_up(Keys.COMMAND).perform()
            driver.switch_to.window(driver.window_handles[1])
            job_slug=driver.find_element(By.CSS_SELECTOR,'.panel-heading').text
            job_title=driver.find_element(By.CSS_SELECTOR,'.job-title').text
            company_name=driver.find_element(By.CSS_SELECTOR,'.job-url span').text
            job_description=driver.find_element(By.XPATH,'//div[@class="panel-body"]/p[1]').text
            job_skills=driver.find_element(By.XPATH,'//div[@class="panel-body"]/div[1]/div[1]/p[2]').text
            job_benifits=driver.find_element(By.XPATH,'//div[@class="panel-body"]/div[1]/div[2]/p[2]').text
            job_apply_link=driver.find_element(By.XPATH,'//div[@class="panel-body"]/div[2]/a').get_attribute('href')
            createIfNotExist(job_slug,job_title)
            time.sleep(5)
            driver.close()
            driver.switch_to.window(main_window)

            time.sleep(5)

        nextLink = driver.find_element(By.CSS_SELECTOR, 'ul.pagination li:last-of-type a')
        nextLink.click()
    except Exception as ex:
        print("No More Pages")
        print(ex)
        traceback.print_exc()
        break
