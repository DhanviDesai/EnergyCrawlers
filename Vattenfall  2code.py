import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

fromYear, fromMonth = 2020, 1
toYear, toMonth = 2021, 12

driver.maximize_window()


driver.get("https://www.vattenfall.se/")

#to accept the cookies
driver.find_element_by_id("cmpwelcomebtnyes").click()

# to press the login button
driver.find_element_by_xpath('//*[@id="page-header"]/div/nav/div/div/ul[2]/li[1]/a').click()
wait = WebDriverWait(driver, 45)

# to press the private button in login tab
wait.until(presence_of_element_located((By.XPATH, '//*[@id="nav-login"]/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="nav-login"]/ul/li[1]/a').click()

# to open the username tab
wait.until(presence_of_element_located((By.XPATH, '//*[@id="customerNumTab"]/a')))
driver.find_element_by_xpath('//*[@id="customerNumTab"]/a').click()

# to enter the username
driver.find_element_by_id('customerId').send_keys('2000920276')

# to enter the password
driver.find_element_by_id("pin").send_keys('6344')

# to press the login buttom
driver.find_element_by_id('submitButton2').click()

# to open the Min förbrukning
wait.until(presence_of_element_located((By.XPATH ,'//*[@id="collapse-8769"]/div/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="collapse-8769"]/div/ul/li[1]/a').click()


# driver.execute_script(('window.scrollTo(0,250);'))
# to open the from tab
wait.until(presence_of_element_located((By.XPATH, '/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/input')))
#Click on the div to select
driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/input').click()
time.sleep(1)
#Get the value of the year
selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)

while selectedYear != fromYear:
    if selectedYear > fromYear:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[1]/button').click()
    else:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[3]/button').click()

    selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
#
driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > tbody').find_elements_by_tag_name('td')[fromMonth-1].click()

driver.execute_script(('window.scrollTo(0,450);'))
# to open the to tab
driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[2]/datepicker-dropdown/div/input').click()
time.sleep(1)
selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
while selectedYear != toYear:
    if selectedYear > toYear:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[2]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[1]/button').click()
    else:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[2]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[3]/button').click()

    selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
    driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > tbody').find_elements_by_tag_name('td')[toMonth-1].click()

wait.until(presence_of_element_located((By.CSS_SELECTOR, '#consumption-graph-container > div:nth-child(4) > button > span:nth-child(2)')))
driver.find_element_by_css_selector('#consumption-graph-container > div:nth-child(4) > button > span:nth-child(2)').click()


# driver.execute_script(('window.scrollTo(0,0);'))
# to open the Valj anlaggning
driver.execute_script(('window.scrollTo(0,10);'))
time.sleep(2)
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[5]/cm-premise-dir/section/div/div/div/div/div/div/button/span[2]')))
driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/div/div/div/div/button/span[2]').click()

# /html/body/div[5]/cm-premise-dir/section/div/div/premise-large-filter-old/section/div[3]/div[1]/div[1]/table/tbody/tr[1]
# /html/body/div[5]/cm-premise-dir/section/div/div/premise-large-filter-old/section/div[3]/div[1]/div[1]/table/tbody/tr[2]
#
# to open the UPP735999100057238916	Bolandsgatan 15 ...		El

trs = driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-large-filter-old/section/div[3]/div[1]/div[1]/table/tbody').find_elements_by_tag_name('tr')
for tr in trs:
    tr.click()
# wait.until(presence_of_element_located((By.XPATH, '/html/body/div[5]/cm-premise-dir/section/div/div/premise-large-filter-old/section/div[3]/div[1]/div[1]/table/tbody/tr[4]')))
# driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-large-filter-old/section/div[3]/div[1]/div[1]/table/tbody/tr[4]').click()

    # to close the Valj anlaggning (Stang X)
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="select-menu"]/div[1]/div/div/div[1]/button/span')))
    driver.find_element_by_xpath('//*[@id="select-menu"]/div[1]/div/div/div[1]/button/span').click()

    # to open the Timme tab
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="home"]/div[1]/div[1]/div/div/ul/li[2]/div/div[1]/button[1]')))
    driver.find_element_by_xpath('//*[@id="home"]/div[1]/div[1]/div/div/ul/li[2]/div/div[1]/button[1]').click()

    fromYear, fromMonth, fromDate = 2020, 1, '1'
    toYear, toMonth, toDate = 2020, 2, '29'

    # to open the fromtab
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="home"]/div[1]/div[1]/div/div/ul/li[5]/div/div[1]/div[1]/input')))
    driver.find_element_by_xpath('//*[@id="home"]/div[1]/div[1]/div/div/ul/li[5]/div/div[1]/div[1]/input').click()

    # to click on the year tab in the fromtab in it
    wait.until(presence_of_element_located((By.XPATH, '/html/body/div[12]/div[1]/table/thead/tr[2]/th[2]')))
    driver.find_element_by_xpath('/html/body/div[12]/div[1]/table/thead/tr[2]/th[2]').click()

    time.sleep(1)

    # to click on the year's tab in the fromtab
    wait.until(presence_of_element_located((By.CSS_SELECTOR, 'body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch')))
    selectedYear = int(driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch').text)
    while selectedYear != fromYear:
        if selectedYear > fromYear:
            driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.prev').click()

        else:
            driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-days > table > thead > tr:nth-child(2) > th.next').click()
    # same selector from the line no 119(int())
        selectedYear = int(driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch').text)

    # driver.find_element_by_css_selector('#home > div.row.cons-space-top > div:nth-child(1) > div > div > ul > li:nth-child(5) > div > div:nth-child(1) > div.input_container.consumptionStartDt.datepicker-old.date > input').find_elements_by_tag_name('span')[fromMonth-1].click()
    #home > div.row.cons-space-top > div:nth-child(1) > div > div > ul > li:nth-child(5) > div > div:nth-child(1) > div.input_container.consumptionStartDt.datepicker-old.date > input

    # to click on the data bar to pick the from date
    driver.find_element_by_xpath('/html/body/div[12]/div[2]/table/tbody/tr/td').find_elements_by_tag_name('span')[fromMonth-1].click()
    time.sleep(1)
    # /html/body/div[12]/div[1]/table/tbody
    tds_day = driver.find_element_by_xpath('/html/body/div[12]/div[1]/table/tbody').find_elements_by_class_name("day")
    for td in tds_day:
        if td.text == fromDate:
            td.click()
            break


    # to open the totab
    wait.until(presence_of_element_located((By.XPATH , '/html/body/section/div/div/div/div[1]/consumption/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/ul/li[5]/div/div[1]/div[2]/input')))
    driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/ul/li[5]/div/div[1]/div[2]/input').click()

    # to click on the year tab in the totab in it
    wait.until(presence_of_element_located((By.XPATH, '/html/body/div[12]/div[1]/table/thead/tr[2]/th[2]')))
    driver.find_element_by_xpath('/html/body/div[12]/div[1]/table/thead/tr[2]/th[2]').click()
    time.sleep(1)

    # to click on the year's tab in the totab
    wait.until(presence_of_element_located((By.CSS_SELECTOR, 'body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch')))
    selectedYear = int(driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch').text)
    while selectedYear != toYear:
        if selectedYear > toYear:
            driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.prev').click()
        else:
            driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.next').click()

        selectedYear = int(driver.find_element_by_css_selector('body > div.datepicker.datepicker-dropdown.dropdown-menu.datepicker-orient-left.datepicker-orient-bottom > div.datepicker-months > table > thead > tr:nth-child(2) > th.datepicker-switch').text)
    # driver.find_element_by_css_selector('#home > div.row.cons-space-top > div:nth-child(1) > div > div > ul > li:nth-child(5) > div > div:nth-child(1) > div.input_container.consumptionEndDt.datepicker-old.date > input').click()

    # to click on the data bar to pick the to date
    driver.find_element_by_xpath('/html/body/div[12]/div[2]/table/tbody').find_elements_by_tag_name('span')[toMonth-1].click()

    time.sleep(1)
    # /html/body/div[12]/div[1]/table/tbody
    tds_day = driver.find_element_by_xpath('/html/body/div[12]/div[1]/table/tbody').find_elements_by_class_name("day")
    for td in tds_day:
        if td.text == toDate:
            td.click()
            break



    driver.execute_script(('window.scrollTo(0,450);'))

    # to download the xls file
    wait.until(presence_of_element_located((By.XPATH, '/html/body/section/div/div/div/div[1]/consumption/div/div/div/div/div[1]/div/div[3]/div[6]/div/div/div[2]/button/span[2]')))
    driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div/div/div/div/div[1]/div/div[3]/div[6]/div/div/div[2]/button/span[2]').click()


    # to close the ad pop button
    wait.until(presence_of_element_located((By.XPATH, '/html/body/div[12]/div/div/div/div/button/span')))
    driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div/button/span').click()