

from calendar import month
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# head to github login page
fromYear, fromMonth = 2019, 3
toYear, toMonth = 2020, 12
driver.maximize_window()
driver.get("https://minasidor.skekraft.se/login?returnUrl=%2Fcorporate")

# to open the Användarnamn och lösenord after visiting the url
driver.find_element_by_id("wrapper").click()
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div').click()
wait = WebDriverWait(driver, 60)
# to enter the Användarnamn(username) number
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[1]/div/input').send_keys('5591349328')

# to enter the Lösenord(password) pin
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/div/input').send_keys('813885')

# to enter the login button
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/button').click()

# # to open the Förbrukning(Consumption)
# wait.until(presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div/nav/ul/li[2]/a')))
# driver.find_element_by_xpath('//*[@id="header"]/div/div/div/nav/ul/li[2]/a').click()
# # to open the Sodra jarnvagsgatn 50 the district
# wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]').click()
#
# # to open the Ar(year)
# wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]').click()
#
#
# # open the Dag(day)
# wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]').click()
# for i in range(12):
# #to open the monthly wise data
#     wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a')))
#     driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a').click()
# # to download the xls files
#     wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/div/div')))
#     driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/div/div').click()
#
#
# # to open the Sodra jarnvagsgatn 50 fastigheten
# wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[2]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[2]').click()
#
# # to open the Dag(day)
# wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[1]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[1]').click()
#
# for j in range(12):
#     wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/a')))
#     driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/a').click()
#
#     # to download the xls files
#     wait.until((presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[4]/div/div'))))
#     driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[4]/div/div').click()
#
# to open the Rapporter(reports)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div/nav/ul/li[4]/a')))
driver.find_element_by_xpath('//*[@id="header"]/div/div/div/nav/ul/li[4]/a').click()

# to open the EL
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label').click()

# to open the El timmätning årsrapport
wait.until(presence_of_element_located((By.XPATH, '/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[2]/label')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[2]/label').click()

wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[3]/input')))
time.sleep(5)
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[3]/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[3]/input').send_keys('2020')

# to download execl file
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[4]/select/option[2]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[4]/select/option[2]').click()

# to download report
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[5]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[5]').click()

# to download Fjärrvärme(District Heating)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/label')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/label').click()

# to Fjärrvärme dygnsförbrukning
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/div/div[1]/label')))
time.sleep(5)
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/div/div[1]/label').click()

# To select year
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/div/div[2]/div[2]/mp-datepicker/input')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[3]/div/div[2]/div[2]/mp-datepicker/input').click()

#
time.sleep(1)
#
selectedYear = int(driver.find_element_by_css_selector('#mat-datepicker-2 > mat-calendar-header > div > div > button.mat-calendar-period-button.mat-button').click())
driver.find_element_by_css_selector('#mat-datepicker-2 > div > mat-multi-year-view > table > tbody > tr:nth-child(2) > td:nth-child(1) > div').click()
while selectedYear != fromYear:
    if selectedYear > fromYear:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[2]').click()
    else:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[3]').click()
    selectedYear = int(driver.find_element_by_css_selector('#mat-datepicker-0 > mat-calendar-header > div > div > button.mat-calendar-period-button.mat-button').text)
driver.find_element_by_css_selector('#mat-datepicker-2 > div > mat-year-view > table > tbody > tr:nth-child(2) > td:nth-child(1) > div').find_elements_by_tag_name('td')[fromMonth-1].click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[2]/td[2]/div').click()
time.sleep(1)
selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
while selectedYear != toYear:
    if selectedYear > toYear:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[2]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[1]/button').click()
    else:
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[2]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[3]/button').click()
    selectedYear = int(driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > thead > tr > th:nth-child(2) > button > strong').text)
driver.find_element_by_css_selector('body > section > div > div > div > div.b2bconsumptionblock > consumption > div:nth-child(1) > div > consumption-heat > div > div > consumption-heat-energy > div > div.col-xs-12.consumption-filter.flex-space-between > consumption-filter-time > div > div:nth-child(2) > consumption-filter-time-month > datepicker-range-selection > div > div:nth-child(2) > datepicker-dropdown > div > div > ul > li > div > div > div > table > tbody').find_elements_by_tag_name('td')[toMonth-1].click()


