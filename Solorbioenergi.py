
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from scraping_utils import get_driver


driver = get_driver()

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

# to click on the Hamta data(Show data) button
wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[7]/input')))
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[1]/tbody/tr/td[7]/input').click()

#Wait until the select element to select facilities is visible
wait.until(presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[4]/td[2]/select')))

select = Select(driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[4]/td[2]/select'))

for option in select.options:
    facilityId = option.text.split('-')[0].strip()

    select.select_by_visible_text(option.text)
    # print(option.text)


    #Wait until the table is present
    wait.until(presence_of_element_located((By.XPATH,'/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody')))

    #Get tbody of the data table
    tbody = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody')

    #for all the rows in the table
    trs = tbody.find_elements_by_tag_name("tr")

    header = []

    #Create header list
    for td in trs[0].find_elements_by_tag_name("th"):
        header.append(td.text)

    #list to hold list of row values
    complete_data = []

    #first row is the header row, so removing that for traversing
    trs = trs[1:]

    for tr in trs:
        curr = []
        for td in tr.find_elements_by_tag_name("td"):
            curr.append(td.text)
        complete_data.append(curr)


    df = pd.DataFrame(complete_data,columns=header)

    months = ['Januari','Februari','Mars','April','Maj','Juni','Juli','Augusti','September','Oktober','November','December']

    complete_data_block = []

    for i in range(len(df)):
        year = df['År'][i]
        for m in range(len(months) - 1):
            data_block = {'facilityId':facilityId,'kind':'Fjärrvärme','quantity':'Energy','unit':'MWh'}
            data_block['startDate'] = year+'-'+months[m]
            data_block['endDate'] = year+'-'+months[m+1]
            data_block['value'] = df[months[m]][i]
            complete_data_block.append(data_block)
        data_block = {'facilityId':facilityId,'kind':'Fjärrvärme','quantity':'Energy','unit':'MWh'}
        data_block['startDate'] = year+'-'+months[m+1]
        year = str(int(year) + 1)
        data_block['endDate'] = year+'-'+months[(m+2)%len(months)]
        data_block['value'] = df[months[m]][i]
        complete_data_block.append(data_block)

    for i in range(12):
        print(complete_data_block[i])

    # print(df.head())

    # df.to_csv('data-'+facilityId+'.csv',index=False)

    #data = {'agentId':'','jobId':'','username':'','facilityId':'','kind':'','quantity':'','startDate':'','endDate':'','unit':'','value':'','timestamp':''}

    #data = {'agentId':'MESTRO-SOLOR-BIOENERGI','jobId':'9357ee44-0e0a-43cf-b7be-2186bd933ccc','username':'fvkund@solorbioenergi','facilityId':'42527977','kind':'Fjärrvärme','quantity':'Energy','startDate':'2021-Januari','endDate':'2021-Februari','unit':'MWh','value':'158629','timestamp':'1613986376157'}

#/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[12]/td/div/table/tbody



# # to download the pdf fie
# wait.until(presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[7]/td[2]/input')))
# driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div/div/table[2]/tbody/tr[7]/td[2]/input').click()

