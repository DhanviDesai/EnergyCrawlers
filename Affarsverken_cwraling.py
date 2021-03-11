import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.affarsverken.se/templates/login/Login.aspx?ReturnUrl=%2fPrivat%2fMina-sidor%2f")


# to login
# to enter username
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/fieldset/div[1]/input').send_keys('554731')
wait = WebDriverWait(driver, 60)
# to enter password
wait.until(presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/fieldset/div[2]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/fieldset/div[2]/input').send_keys('5568171416')
# to click on login
wait.until(presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/fieldset/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/fieldset/input').click()


# To select EI
wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div/div[2]/div[1]/div/ul/li[1]/a')))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div/div[2]/div[1]/div/ul/li[1]/a').click()

# To select hourly readings
wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div/div[2]/div/div/ul/li[1]/ul/li[3]/a')))
driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div/div[2]/div/div/ul/li[1]/ul/li[3]/a').click()

# #  to select from date
# wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input').clear()
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('2020-01-01')
#
#  # to select till date
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[2]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[2]/input').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()
# time.sleep(2)


index=1

while(1):
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div/div/ul/li[{0}]'.format(index)).click()
    except Exception as e:
        print(e)
        break
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()
    time.sleep(2)

    #  to select from date
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys('2020-01-01')

    # to select till date
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[2]/input')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[2]/input').clear()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[2]/input').send_keys('2021-03-11')
    time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()
    time.sleep(2)

    # to click on Hamta(Retrieve)
    wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input').click()
    time.sleep(5)
    # to download excel file
    wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input').click()
    time.sleep(5)
    index+=1



    # # to click on Hamta(Retrieve)
    # wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input')))
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input').click()
    # time.sleep(5)
    # # to download excel file
    # wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input')))
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input').click()
    # time.sleep(5)

# select = Select(driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/select'))
# options = select.options
# print(options[0].text)
# for address in options:
#     address.


# # to click on Hamta(Retrieve)
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input').click()
# time.sleep(5)
# # to download excel file
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input').click()
# time.sleep(5)

# # to select the address tab
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()

# # to select second address
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div/div/ul/li[2]')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div/div/ul/li[2]').click()
# # to click on Hamta(Retrieve)
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input').click()
# # to download excel file
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input').click()
#
#
# # to select the address tab
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div').click()

# # to select third address
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div/div/ul/li[3]')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[5]/div/div/div/ul/li[3]').click()
# # to click on Hamta(Retrieve)
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[1]/div[5]/input').click()
# # to download excel file
# wait.until(presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input')))
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[6]/div/div[2]/div[1]/div[7]/div[2]/div/div[2]/div[2]/div[1]/input').click()