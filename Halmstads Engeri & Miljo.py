import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://minasidor.hem.se/default.aspx")
driver.maximize_window()

wait = WebDriverWait(driver, 30)

# to click on the Användarnamn username
driver.find_element_by_id('txtUser').send_keys('83460')

# to click on the Lösenord password
driver.find_element_by_id('txtPassword').send_keys('Plantagen123')


# to click on the loggi button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[4]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div[4]/div/div[1]/div/input')))
driver.find_element_by_xpath('/html/body/form/div[4]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[2]/div[4]/div/div[1]/div/input').click()

# to select the Rapportcenter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/nav/div[2]/ul/li[9]/a')))
driver.find_element_by_xpath('/html/body/form/nav/div[2]/ul/li[9]/a').click()

# to select the Enga Rapport
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/nav/div[2]/ul/li[9]/ul/li[1]/a')))
driver.find_element_by_xpath('/html/body/form/nav/div[2]/ul/li[9]/ul/li[1]/a').click()

time.sleep(6)

# to select the csv
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/label[1]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/label[1]/input').click()

# to select the Timme(time)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[1]/div[2]/select/option[4]')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[1]/div[2]/select/option[4]').click()


# to select the Exporter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/span/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/span/input').click()

# to select the Naturegus Energi(Symbol)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[1]/ul/li[2]/a/i')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[1]/ul/li[2]/a/i').click()

time.sleep(6)

# to select the csv
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/label[1]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/label[1]/input').click()

# to select the Timme(time)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[1]/div[2]/select/option[4]')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[1]/div[2]/select/option[4]').click()

# to select Exporter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/span/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/section/article/div[3]/div/span/input').click()

