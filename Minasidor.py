from calendar import month

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://minasidor.skekraft.se/login?returnUrl=%2Fcorporate")

# to open the Användarnamn och lösenord after visiting the url
driver.find_element_by_id("wrapper").click()
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div').click()
wait = WebDriverWait(driver, 10)
# to enter the Användarnamn(username) number
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[1]/div/input').send_keys('5591349328')

# to enter the Lösenord(password) pin
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/div/input').send_keys('813885')

# to enter the login button
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/button').click()

# to open the Förbrukning(Consumption)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div/nav/ul/li[2]/a')))
driver.find_element_by_xpath('//*[@id="header"]/div/div/div/nav/ul/li[2]/a').click()
# to open the Sodra jarnvagsgatn 50 the district
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]').click()

# to open the Ar(year)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]').click()


# open the Dag(day)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]').click()
for i in range(12):
#to open the monthly wise data
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a')))
    driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a').click()
# to download the xls files
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/div/div')))
    driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/div/div').click()

# to open the Sodra jarnvagsgatn 50 fastigheten
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[2]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[2]').click()

# to open the Dag(day)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[1]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[1]').click()
for j in range(12):
# to open the monthly wise data
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/a')))
    driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[5]/a').click()

# to download the xls files
    wait.until((presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[4]/div/div'))))
    driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[4]/div/div').click()

# to open the Rapporter(reports)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div/div/nav/ul/li[4]/a')))
driver.find_element_by_xpath('//*[@id="header"]/div/div/div/nav/ul/li[4]/a').click()

# to open the EL
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label').click()

# to open the El timmätning årsrapport
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[2]/label/span')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[2]/label/span').click()

# t
# wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/label[4]')))
# driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/label[4]').click()

# to download execl file
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[5]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[3]/div[5]').click()