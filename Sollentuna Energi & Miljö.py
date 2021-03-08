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

# to select the 108184002 - Bergkällavägen 26
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[2]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[2]/tbody/tr/td[3]/a').click()


time.sleep(1)
#to select the 	20800 - Bergkällavägen 26
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[4]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[4]/tbody/tr/td[3]/a').click()

time.sleep(1)
# to open the Rapportcenter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/a').click()

time.sleep(1)
# to opne the Engarapport inside the Rapportcenter
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/ul/li[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[4]/ul/li[3]/a').click()


# to select the manad(month)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input').click()

# to select the Flode
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[3]/td/div/label[2]')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[3]/td/div/label[2]').click()

# to select the Microsoft execl
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input').click()

# to select the Exportera button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input').click()

# to select the 3750065 - Bergkällavägen 26
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[5]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[5]/tbody/tr/td[3]/a').click()

# to select the manad(month)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input').click()

# to select the Microsoft execl
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input').click()

# to select the Exportera button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input').click()


time.sleep(3)
# to select the 3750071 - Bergkällavägen 28
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[6]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[6]/tbody/tr/td[3]/a').click()

# to select the manad(month)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input').click()

# to select the Microsoft execl
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input').click()

# to select the Exportera button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input').click()

time.sleep(3)
# to select the 9600 - Bergkällavägen 28
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[7]/tbody/tr/td[3]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[1]/div[2]/div/div/table[7]/tbody/tr/td[3]/a').click()

# to select the manad(month)
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[2]/td/strong/table/tbody/tr[1]/td[2]/span/input').click()

# to select the Flode
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[3]/td/div/label[2]')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[3]/td/div/label[2]').click()

# to select the Microsoft execl
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[4]/td/strong/table/tbody/tr[2]/td/input').click()

# to select the Exportera button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td/div/table/tbody/tr[3]/td[5]/fieldset[2]/table/tbody/tr[5]/td/input').click()

# to select the Hem(Home) button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[1]/a')))
driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/div/div/div[1]/ul/li[1]/a').click()

driver.get("https://minasidor.seom.se/Login.aspx")


# to select the Se mina fakturor
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div[1]/div[1]/div/div[1]/div[1]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[1]/div[1]/div/div[1]/div[1]/input').click()

# to select the 5166143106
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[2]/td[3]')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[2]/td[3]').click()

# to select the 5165960203
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[3]/td[3]')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[3]/td[3]').click()

# to select the 5165960104
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[4]/td[3]')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[1]/div[4]/div/div/table/tbody/tr[2]/td/table/tbody[2]/tr/td/div[2]/table/tbody/tr[4]/td[3]').click()