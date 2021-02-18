import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://minasidor.skekraft.se/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[3]/label')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[3]/label').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[1]/div/input').send_keys('5591349328')
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/div/input').send_keys('813885')
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-login-page/div/div/mp-login/div/div/div/div[4]/div[2]/button').click()
wait.until(presence_of_element_located((By.XPATH,'//*[@id="header"]/div/div/div/nav/ul/li[2]/a')))
driver.find_element_by_xpath('//*[@id="header"]/div/div/div/nav/ul/li[2]/a').click()
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[1]/div/div/div/div[1]/mp-subscription-menu/div/div[1]/div[1]').click()
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[2]').click()
wait.until(presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a')))
driver.find_element_by_xpath('//*[@id="wrapper"]/section/div/mp-consumption-corporate-volume-page/div[2]/div/mp-volume-graph/div/div[1]/div[6]/a').click()


