import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd


driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://eforsyning.dk/tranegilde/#/")
driver.maximize_window()

wait = WebDriverWait(driver, 38)

# to  press the GOdkend(approve) button
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/mat-dialog-container/dff-cookie-consent-dialog/div/div/mat-dialog-actions/div/button[1]/span[1]')))
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/mat-dialog-container/dff-cookie-consent-dialog/div/div/mat-dialog-actions/div/button[1]/span[1]').click()


# to click on the Användarnamn username
driver.find_element_by_id('forbrugerNr').send_keys('234703001')

# to click on the Lösenord password
driver.find_element_by_id('kode').send_keys('7636')


# to click on the loggi button
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/app-root/app-shell/div/div/div/div/login/login-container/div[2]/div[2]/mat-tab-group/div/mat-tab-body[1]/div/login-forbrugernr/form/div[3]/button')))
driver.find_element_by_xpath('/html/body/div[1]/div[2]/app-root/app-shell/div/div/div/div/login/login-container/div[2]/div[2]/mat-tab-group/div/mat-tab-body[1]/div/login-forbrugernr/form/div[3]/button').click()

# to press the ikku nu button (cookies)
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/e-boks-popup-content/div/div/div/button[2]')))
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/e-boks-popup-content/div/div/div/button[2]').click()

# to select the the Mit forbrug button
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/app-root/app-shell/div/eforsyning-sidenav-menu/dff-sidenav-menu/div[2]/a')))
driver.find_element_by_xpath('/html/body/div[1]/div[2]/app-root/app-shell/div/eforsyning-sidenav-menu/dff-sidenav-menu/div[2]/a').click()


time.sleep(5)

# to select the Download button
wait.until(presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/app-root/app-shell/div/div/div/div/ng-component/dff-side/panel/mat-card/div[1]/button/span[1]/mat-icon/svg')))
driver.find_element_by_xpath('/html/body/div[1]/div[2]/app-root/app-shell/div/div/div/div/ng-component/dff-side/panel/mat-card/div[1]/button/span[1]/mat-icon/svg').click()