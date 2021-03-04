import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://minasidor.seom.se/Login.aspx")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# to click on the Användarnamn username
driver.find_element_by_id('UserName').send_keys('55259')

# to click on the Lösenord password
driver.find_element_by_id('Password').send_keys('Corem2017')


# to click on the loggi button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div/div/div[2]/p/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div/div/div[2]/p/input').click()

# to open the Enegrikollen
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/ul/li[7]/a')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/ul/li[7]/a').click()

# to open the Rapportcenter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/a').click()


# to opne the Engarapport inside the Rapportcenter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/ul/li[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/ul/li[3]/a').click()

wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[4]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[4]/tbody/tr/td[3]/a').click()

