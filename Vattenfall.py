from scraping_utils import get_driver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = 'https://www.vattenfall.se'
driver = get_driver()
driver.maximize_window()
driver.get(url)
#Tried making it none
# driver.execute_script('document.getElementById("cmpbox2").style.display = "none";')
# driver.execute_script('document.getElementById("cmpbox").style.display = "none";')
# print('set those things to none')
wait = WebDriverWait(driver,10)
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
wait = WebDriverWait(driver,10)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="collapse-8769"]/div/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="collapse-8769"]/div/ul/li[1]/a').click()

#Select dates
wait.until(presence_of_element_located((By.XPATH,'/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')))
from_date = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-month/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')
from_date.click().send_keys('januari 2020')
print(from_date.get_attributes('value'))
