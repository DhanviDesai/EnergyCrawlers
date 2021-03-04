from os import system
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Vattenfall Credentials
# username = "username"
# password = "password"
# initialize the Chrome driver
driver = webdriver.Chrome(executable_path=r'C:\Users\Dhanvi\Headless_Browsers\chromedriver')

fromYear, fromMonth = 2020, 1
toYear, toMonth = 2021, 1


driver.get("https://www.vattenfall.se/")
driver.maximize_window()
# find username/email field and send the username itself to the input field
driver.find_element_by_id("cmpwelcomebtnyes").click()
driver.find_element_by_xpath('//*[@id="page-header"]/div/nav/div/div/ul[2]/li[1]/a').click()
wait = WebDriverWait(driver, 10)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="customerNumTab"]/a')))
driver.find_element_by_xpath('//*[@id="customerNumTab"]/a').click()
driver.find_element_by_id('customerId').send_keys('2001079662')
# find password input field and insert password as well
driver.find_element_by_id("pin").send_keys('4995')
driver.find_element_by_id('submitButton2').click()
wait.until(presence_of_element_located((By.XPATH, '//*[@id="collapse-8769"]/div/ul/li[1]/a')))

driver.find_element_by_xpath('//*[@id="collapse-8769"]/div/ul/li[1]/a').click()
wait.until(presence_of_element_located((By.XPATH, '/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/input')))


print('Will try to select day here')

wait.until(presence_of_element_located((By.XPATH,'/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div')))
day_button = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div')
day_button.click()
driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div/ul/li[2]/a').click()

wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-day/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')))
print('Wait done')

driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-day/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/input').click()
time.sleep(1)

selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
while selectedYear != fromYear:
    if selectedYear > fromYear:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[1]/button').click()
    else:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[3]/button').click()

    selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(1) > datepicker-dropdown > div > div > ul > li > div > div > div > table > tbody').find_elements_by_tag_name('td')[fromMonth-1].click()

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