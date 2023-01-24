#!/usr/bin/env python

import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
#browser.implicitly_wait(2)
browser.get('https://apps.db.ripe.net/db-web-ui/#/fulltextsearch')

time.sleep(2)
#elem = browser.find_element_by_id("fullTextSearchInput")
elem = browser.find_element(By.ID,"fullTextSearchInput")
elem.send_keys("mercadona", Keys.ENTER)

#Wait 5 secs for the query to be done
time.sleep(5)

page = 1
inetnums = []
inet6nums = []
emails = []
mntby = []

def extract_info(inetnums, inet6nums, browser):
   rows = browser.find_element(By.ID,"resultsAnchor").find_element(By.CLASS_NAME,"padding").find_elements(By.CLASS_NAME,"margin-bottom.grey-border-top.padding-top.results")
   for row in rows:

      #Finding emails
      mails = re.findall('[^\s=]+@mercadona.es', row.text)
      for mail in mails:
         emails.append(mail)
#         print mail
      
      #Finding mnt-by
      mnts = re.findall('mnt-by=[^\s,]+', row.text)
      for mnt in mnts:
         mnt_by = re.split('=', mnt)[1]
         mntby.append(mnt_by)
#         print mnt_by

      #Getting IP information 
      text = row.find_element(By.CSS_SELECTOR,"a").text
      if "inetnum" in text:
         ip = re.split('\n', re.split(': ', row.text)[1])[0]
         inetnums.append(ip)
         print(str(ip))
      if "inet6num" in text:
         ip6 = re.split('\n', re.split(': ',row.text)[1])[0]
         inet6nums.append(ip6)
#         print ip6

def next_page(browser, page):
   paginator = browser.find_element(By.CSS_SELECTOR,"paginator")
   pagination = paginator.find_element(By.CLASS_NAME,'pagination')
   #Finding page in paginator
   pages = pagination.find_elements(By.CSS_SELECTOR,"li")
   try:
    for i in range(len(pages)):
      elem_page = pages[i].find_element(By.CSS_SELECTOR,"a")
      try:
        new_page = int(elem_page.text)
      except:
        continue
      if page + 1 == new_page:
         #Going to the next page
         elem_page.click()
         return new_page
   except:
     print("No more pages")
     raise Exception('')
   return
   #raise Exception('')              #No more pages

browser.execute_script("window.scrollTo(0, 300)")
while True:
   try:
      extract_info(inetnums, inet6nums, browser)
      page = next_page(browser, page)
      time.sleep(1)
   except Exception as e:
      print(e)
      break

browser.quit()

#print "DONE!!!"
