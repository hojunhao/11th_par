# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 13:03:21 2016

@author: Vivobook
"""


# sample script to scrap parliament.gov.sg
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


# start firefox instance
driver = webdriver.Firefox()

# main search page
driver.get("http://www.parliament.gov.sg/" +
           "publications-singapore-official-reports")
time.sleep(5)
driver.switch_to_frame(0)

# driver.find_element_by_id('parliamentNo').send_keys("realpython")
el = driver.find_element_by_id("parliamentNo")
select = Select(driver.find_element_by_id('parliamentNo'))
select.select_by_visible_text('11th (02-11-2006 to 19-04-2011)')

time.sleep(2)
driver.find_element_by_id("B_Search").click()

driver.switch_to_window(driver.window_handles[1])
time.sleep(5)


folder_path = "D:/workspace/11th_par/listing/"
filename = "Page"

# restarting from a certain page in case the process is disrupted
# js_script = "javascript:SerResult.doSearch(449)"
# driver.execute_script(js_script)

# loop through all results page
for i in range(1, 130):
    file_path = folder_path + filename + str(i) + ".html"
    print file_path
    check_page = driver.find_element_by_xpath(
        '//div[@id="searchResults"]/p/span').text
    # save file
    with open(file_path, "w") as output:
        output.write(driver.page_source.encode("ascii", "ignore"))
    # go to next page
    driver.find_element_by_xpath(
        '//div[@id="divPrevNextLink"]/table/tbody/tr/td[4]/a').click()
    time.sleep(10)

driver.quit()
