# from scraping_utils import get_driver
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
from scraping_utils import get_driver
import traceback
import pandas as pd


year = '2020'
month = 'januari'
day = '01'

url = 'https://www.vattenfall.se'
driver = get_driver()
driver.maximize_window()
driver.get(url)
#Tried making it none
# driver.execute_script('document.getElementById("cmpbox2").style.display = "none";')
# driver.execute_script('document.getElementById("cmpbox").style.display = "none";')
# print('set those things to none')
wait = WebDriverWait(driver,15)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="cmpwelcomebtnyes"]/a')))
driver.find_element_by_xpath('//*[@id="cmpwelcomebtnyes"]/a').click()
log_in = driver.find_element_by_xpath('//*[@id="page-header"]/div/nav/div/div/ul[2]/li[1]/a')

log_in.click()

wait = WebDriverWait(driver,10)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="customerNumTab"]')))
driver.find_element_by_xpath('//*[@id="customerNumTab"]').click()
driver.find_element_by_id('customerId').send_keys('2001079662')
driver.find_element_by_id('pin').send_keys('4995')
driver.find_element_by_id('submitButton2').click()

#Click on Min förbrukning
wait = WebDriverWait(driver,15)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="collapse-8769"]/div/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="collapse-8769"]/div/ul/li[1]/a').click()



count = 1

    #Select date resolution
wait.until(presence_of_element_located((By.XPATH,'/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')))

    #Get facility ID
fid = driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div[1]/div/div/div[2]/span[2]')
print("FacilityId ",fid.text)

day_button = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div')
day_button.click()
driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div/ul/li[1]/a').click()

    #Wait until an error is thrown
wait.until(EC.invisibility_of_element_located((By.TAG_NAME,'loading-spinner')))

    #Select from date
driver.execute_script('window.scrollTo(0,200);')
time.sleep(1)
from_date = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')
from_date.click()

driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr[1]/th[2]/button').click()

driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[2]/button').click()


table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

tds = table.find_elements_by_tag_name('td')
for td in tds:
    if td.text == year:
        td.click()
        break

table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

tds = table.find_elements_by_tag_name('td')
for td in tds:
    if td.text == month:
        td.click()
        break

table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

tds = table.find_elements_by_tag_name('td')
for td in tds:
    if td.text == day:
        td.click()
        break

driver.execute_script('window.scrollTo(0,750);')

typ = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[1]/h3')
print('quantity',typ.text)

        # unit = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]/span')

        # /html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]/span

        # /html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]

print('unit kWh')


wait.until(EC.invisibility_of_element_located((By.TAG_NAME,'loading-spinner')))
driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/div[2]/button').click()
time.sleep(15)
count += 1
