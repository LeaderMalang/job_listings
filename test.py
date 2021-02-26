from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


driver=webdriver.Chrome('/Users/casper.local/Desktop/Dev/job_listing/chromedriver')
#print(driver.title)
driver.get('https://crypto.jobs')
def single_parse(job_Link_element,main_dr):
    print(job_Link_element.text)
    main_dr
    #main_window = main_dr.current_window_handle
    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = main_dr.current_window_handle

    # Open the link in a new tab by sending key strokes on the element
    # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
    job_Link_element.send_keys(Keys.CONTROL + Keys.RETURN)

    # Switch tab to the new tab, which we will assume is the next one on the right
    main_dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

    # Put focus on current window which will, in fact, put focus on the current visible tab
    main_dr.switch_to.window(main_window)

    # do whatever you have to do on this page, we will just got to sleep for now
    time.sleep(2)

    # Close current tab
    main_dr.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    # Put focus on current window which will be the window opener
    main_dr.switch_to.window(main_window)



    #job_Link_element.click()
    title=main_dr.find_element(By.CSS_SELECTOR,'.panel-heading').text
    job_title=main_dr.find_element(By.CSS_SELECTOR,'.job-title').text
    job_url=main_dr.find_element(By.CSS_SELECTOR,'.job-url::attr(href)').text
    company=main_dr.find_element(By.CSS_SELECTOR,'.job-url span').text
    print(job_title,main_dr)
    return True

while True:
    try:
        nextLink=driver.find_element(By.CSS_SELECTOR,'ul.pagination li:last-of-type a')
        nextLink.click()
        job_urls=driver.find_elements(By.CSS_SELECTOR,'.job-url')
        for job_url in job_urls:
            single_parse(job_url,driver)
            time.sleep(5)
    except Exception as ex:
        print("No More Pages")
        break
# for nextLink in nextLinks:
#     nextLink.click()
#     #driver.getCurrentUrl()
#     time.sleep(5)