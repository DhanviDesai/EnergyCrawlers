
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd


driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://www.kwhgreen.com/Login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# to click on the Användarnamn username
driver.find_element_by_id('MainContent_Email').send_keys('fvkund@solorbioenergi')

# to click on the Lösenord password
driver.find_element_by_id('MainContent_Password').send_keys('Solorbioenergi_2016')


# to click on the loggi button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[4]/div[2]/div[1]/section/div/div[4]/div/input')))
driver.find_element_by_xpath('/html/body/form/div[4]/div[2]/div[1]/section/div/div[4]/div/input').click()

# to select the city

wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[2]/select')))
city = Select(driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[2]/select'))
city.select_by_visible_text('Vilhelmina')
time.sleep(2)

wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[2]/select')))
city = Select(driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[2]/select'))
city.select_by_visible_text('Vilhelmina')


# to click on the Kundnummer(number)
driver.find_element_by_id('ContentPlaceHolder1_tbxKundnummer').send_keys('2066217')

# to click on the Person-/Org.-nummer YYMMDDABCD(number)
driver.find_element_by_id('ContentPlaceHolder1_tbxIdNummer').send_keys('5562308212')

# to click on the Hamta data(Download Data) button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[7]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[7]/input').click()

wait.until(presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody')))
tbody = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody')
trs = tbody.find_elements_by_tag_name("tr")
header = []
for td in trs[0].find_elements_by_tag_name("th"):
    header.append(td.text)

complete_data = []
# complete_data.append(header)
trs = trs[1:]
for tr in trs:
    curr = []
    for td in tr.find_elements_by_tag_name("td"):
        curr.append(td.text)
    complete_data.append(curr)


df = pd.DataFrame(complete_data,columns=header)
print(df.head())

df.to_csv('data.csv',index=False)

#/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody



# # to download the pdf fie
# wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[7]/td[2]/input')))
# driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[7]/td[2]/input').click()

