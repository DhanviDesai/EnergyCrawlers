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


# to select
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/div/mp-menu/header/div/div/div/nav/ul/li[3]/a')))
driver.find_element_by_xpath('/html/body/app-root/div/mp-menu/header/div/div/div/nav/ul/li[3]/a').click()

wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-costs-page/div[2]/div/mp-tabs-menu/div/div[1]/ul/mp-tabs-menu-item[2]/li/a')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-costs-page/div[2]/div/mp-tabs-menu/div/div[1]/ul/mp-tabs-menu-item[2]/li/a').click()
# to have 100 bills in the same page
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/div[1]/div[2]/div/select')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/div[1]/div[2]/div/select').click()

wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/div[1]/div[2]/div/select/option[4]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/div[1]/div[2]/div/select/option[4]').click()

# to download
# 1
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[4]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[4]').click()
# 2
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[5]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[5]').click()
# 3
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[6]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[6]').click()
# 4
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[7]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[7]').click()
# 5
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[8]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[8]').click()
# 6
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[9]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[9]').click()
# 7
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[10]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[10]').click()
# 8
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[11]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[11]').click()
# 9
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[12]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[12]').click()
# 10
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[13]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[13]').click()
# 11
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[14]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[14]').click()
# 12
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[15]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[15]').click()
# 13
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[16]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[16]').click()
# 14
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[17]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[17]')
# 15
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[18]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[18]').click()
# 16
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[19]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[19]').click()
# 17
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[20]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[20]').click()
# 18
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[21]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[21]').click()
# 19
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[22]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[22]').click()
# 20
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[23]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[23]').click()
# 21
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[24]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[24]').click()
# 22
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[25]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[25]').click()
# 23
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[26]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[26]').click()
# 24
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[27]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[27]').click()
# 25
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[28]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[28]').click()
# 26
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[29]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[29]').click()
# 27
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[30]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[30]').click()
# 28
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[31]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[31]').click()
# 29
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[32]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[32]').click()
# 30
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[33]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[33]').click()
# 31
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[34]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[34]').click()
# 32
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[35]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[35]').click()
# 33
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[36]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[36]').click()
# 34
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[37]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[37]').click()
# 35
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[38]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[38]').click()
# 36
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[39]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[39]').click()
# 37
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[40]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[40]').click()
# 38
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[41]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[41]').click()
# 39
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[42]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[42]').click()
# 40
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[43]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[43]').click()
# 41
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[44]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[44]').click()
# 42
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[45]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[45]').click()
# 43
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[46]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[46]').click()
# 44
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[47]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[47]').click()
# 45
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[48]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[48]').click()
# 46
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[49]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[49]').click()
# 47
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[50]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[50]').click()
# 48
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[51]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[51]').click()
# 49
wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[52]')))
driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-economy-corporate-invoices-page/div[3]/div[1]/mp-invoices/div/div/table/tbody/tr[52]').click()

# # to open on Rapporter
# wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/div/mp-menu/header/div/div/div/nav/ul/li[4]/a')))
# driver.find_element_by_xpath('/html/body/app-root/div/mp-menu/header/div/div/div/nav/ul/li[4]/a').click()
#
# # to open EI
# wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label')))
# driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/label').click()
#
# # to open Export av timvärden
# wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[10]/label')))
#
# driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[10]/label').click()
#
# # to enter from date
# wait.until(presence_of_element_located((By.XPATH,'/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[11]/div[3]/mp-datepicker/input')))
# driver.find_element_by_xpath('/html/body/app-root/main/section/div/mp-reports-page/div[2]/div[1]/mp-reports/div/div/div[1]/div/div[11]/div[3]/mp-datepicker/input').click()
# # to open year
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[1]')))
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/mat-calendar-header/div/div/button[1]').click()
# # to select 2020
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-multi-year-view/table/tbody/tr[2]/td[1]/div')))
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-multi-year-view/table/tbody/tr[2]/td[1]/div').click()
# # to select january
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-year-view/table/tbody/tr[2]/td[1]/div')))
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-year-view/table/tbody/tr[2]/td[1]/div').click()
# # to select date
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[2]/td[2]/div')))
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[2]/td[2]/div').click()
#
