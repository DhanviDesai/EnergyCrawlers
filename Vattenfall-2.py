# from scraping_utils import get_driver
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException,TimeoutException
import time
import winsound
from scraping_utils import get_driver
import traceback
import pandas as pd
import os
import json

def dump_data(facilityId,quantity,unit,kind):
    df = pd.read_excel('data.xlsx',engine='openpyxl',names=['date','value'])
    complete_data = []
    for i in range(len(df['date']) - 1):
        data_block = {}
        data_block = {'facilityId':facilityId,'quantity':quantity,'unit':unit,'kind':kind}
        data_block['startDate'] = df['date'][i]
        data_block['endDate'] = df['date'][i+1]
        data_block['value'] = df['value'][i]
        complete_data.append(data_block)
    
    for i in range(10):
        print(complete_data[i])


kind_lookup = {'heat-1.svg':'Fjärrvärme','heat-2.svg':'Fjärrvärme','Cool-1.svg':'Fjärrkyla','el-1.svg':'Elnät','el-2.svg':'Elnät'}

year = '2020'
month = 1
day = '01'

url = 'https://www.vattenfall.se'
driver = get_driver()
driver.maximize_window()
driver.get(url)
#Tried making it none
# driver.execute_script('document.getElementById("cmpbox2").style.display = "none";')
# driver.execute_script('document.getElementById("cmpbox").style.display = "none";')
# print('set those things to none')
wait = WebDriverWait(driver,30)
wait.until(presence_of_element_located((By.XPATH,'//*[@id="cmpwelcomebtnyes"]/a')))
driver.find_element_by_xpath('//*[@id="cmpwelcomebtnyes"]/a').click()
log_in = driver.find_element_by_xpath('//*[@id="page-header"]/div/nav/div/div/ul[2]/li[1]/a')

log_in.click()

driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul[2]/li[1]/div/ul/li[1]/a').click()

wait.until(presence_of_element_located((By.XPATH,'//*[@id="customerNumTab"]')))
driver.find_element_by_xpath('//*[@id="customerNumTab"]').click()
driver.find_element_by_id('customerId').send_keys('2001079662')
driver.find_element_by_id('pin').send_keys('4995')
driver.find_element_by_id('submitButton2').click()

#Click on Min förbrukning
wait.until(presence_of_element_located((By.XPATH,'//*[@id="collapse-8769"]/div/ul/li[1]/a')))
driver.find_element_by_xpath('//*[@id="collapse-8769"]/div/ul/li[1]/a').click()



count = 1
while(1):
    try:
        #_hj-1tTKm__styles__surveyContainer _hj-2UlJh__styles__positionRight _hj-3BmV5__styles__openingAnimation
        button_xpath = '/html/body/div[12]/div/div/div/div/button'
        div_xpath = '/html/body/div[12]/div/div/div/div'
        # if EC.visibility_of_element_located((By.XPATH,div_xpath)):
        #     driver.find_element_by_xpath(button_xpath).click()
        print(count)
        driver.execute_script("document.getElementById('page-header').style.display = 'none';")

        driver.execute_script(" if(document.getElementsByClassName('_hj-1tTKm__styles__surveyContainer')[0] !== undefined){ document.getElementsByClassName('_hj-1tTKm__styles__surveyContainer')[0].style.display='none'; }")

        wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div['+str(count)+']/div/div')))

        print('/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div['+str(count)+']/div/div')

        #/html/body/div[6]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div[3]/div/div

        #/html/body/div[6]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div[4]

        driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div['+str(count)+']/div/div').click()
        
        #Get facility ID
        fid = driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div['+str(count)+']/div/div/div[2]/span[2]')
        facilityId = fid.text
        print("FacilityId ",fid.text)

        #Get kind
        kind_img = driver.find_element_by_xpath('/html/body/div[5]/cm-premise-dir/section/div/div/premise-small-filter-old/div/div[1]/div/slick/div/div/div['+str(count)+']/div/div/div[1]/img')
        print('kind',kind_img.get_attribute('src'))
        kind_name = kind_img.get_attribute('src').split('/')[-1]

        #Select timme resolution
        wait.until(presence_of_element_located((By.XPATH,'/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div')))
        
        day_button = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div')
        day_button.click()
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[1]/btn-dropdown/div/ul/li[1]/a').click()

        #Wait until an error is thrown
        wait.until(EC.invisibility_of_element_located((By.TAG_NAME,'loading-spinner')))

        #Select from date
        driver.execute_script('window.scrollTo(0,200);')
        time.sleep(1)
        from_date = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div')
        from_date.click()

        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr[1]/th[2]/button').click()

        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table/thead/tr/th[2]/button').click()


        table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

        table.find_elements_by_tag_name('td')[year-1].click()

        tds = table.find_elements_by_tag_name('td')
        for td in tds:
            if td.text == year:
                td.click()
                break

        table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

        tds = table.find_elements_by_tag_name('td')
        for td in tds:
            if td.text == month:
                td.click()
                break

        table = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[1]/consumption-filter-time/div/div[2]/consumption-filter-time-hour/datepicker-range-selection/div/div[1]/datepicker-dropdown/div/div/ul/li/div/div/div/table')

        tds = table.find_elements_by_tag_name('td')
        for td in tds:
            if td.text == day:
                td.click()
                break

        driver.execute_script('window.scrollTo(0,700);')

        typ = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[1]/h3')
        quantity = typ.text
        print('quantity',typ.text)

                # unit = driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]/span')

                # /html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]/span

                # /html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/highchart/div/span[2]

        print('unit kWh')


        wait.until(EC.invisibility_of_element_located((By.TAG_NAME,'loading-spinner')))
        driver.find_element_by_xpath('/html/body/section/div/div/div/div[1]/consumption/div[1]/div/consumption-heat/div/div/consumption-heat-energy/div/div[2]/consumption-graph/div/div[2]/button').click()
        while(not os.path.exists('data.xlsx')):
            time.sleep(1)
        count += 1
        # os.rename('data.xlsx','data-'+fid.text+'.xlsx')
        dump_data(facilityId,quantity,'kWh',kind_lookup[kind_name])
        os.remove('data.xlsx')
        driver.execute_script('window.scrollTo(0,0);')
        # driver.back()
    
    except Exception as e:
        print(traceback.format_exc())
        break
