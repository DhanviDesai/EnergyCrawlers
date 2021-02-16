from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from scraping_utils import get_driver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
import os

#TODO: Traverse the list and download only those facilities that have Fjärrvärme

#Download directory is the current working directory
#Input : username,password,typ,facility_ids,period
#   typ_look_up = {0 : 'Fjärrvärme', 1 : 'Fjärrkyla', 2 : 'El', 3 : 'Elnät'}
#   typ = Any of the key values, Default : ALL
#   facility_ids = 'ALL' or list of facility_ids, Default : ALL 
#   period = yyyy-mm-dd;yyyy-mm-dd or None (in the format from;to or Default:None [last 12 months])

def UmeaEnergi(username,password,period=None,facility_ids='ALL'):

    url = 'https://www.umeaenergi.se/mina-sidor/login'

    driver = get_driver()
    driver.maximize_window()
    driver.get(url)

    wait = WebDriverWait(driver,5)
    wait.until(presence_of_element_located((By.ID,'onetrust-consent-sdk')))
    driver.execute_script('document.getElementById("onetrust-consent-sdk").style.display="none";')

    driver.find_element_by_id('sectionplaceholder_1_rowplaceholderec931a9bef844079a92fd532f121cae1_0_blockplaceholder1013ddee3ff2e4f9383371ec262ea3ef1_0_Login1_UserName').send_keys(username)
    driver.find_element_by_id('sectionplaceholder_1_rowplaceholderec931a9bef844079a92fd532f121cae1_0_blockplaceholder1013ddee3ff2e4f9383371ec262ea3ef1_0_Login1_Password').send_keys(password)
    driver.find_element_by_id('sectionplaceholder_1_rowplaceholderec931a9bef844079a92fd532f121cae1_0_blockplaceholder1013ddee3ff2e4f9383371ec262ea3ef1_0_Login1_LoginButton').click()

    wait = WebDriverWait(driver,13)
    wait.until(presence_of_element_located((By.XPATH,'//*[@id="statistics"]/div[2]/div[1]/div/div[2]/div[2]/a[1]')))
    deta = driver.find_element_by_xpath('//*[@id="statistics"]/div[2]/div[1]/div/div[2]/div[2]/a[1]')
    if deta is not None:
        deta.click()
        count = 2
        while(1):
            try:
                wait.until(presence_of_element_located((By.XPATH,'//*[@id="contentmypages_1_rowplaceholder6279a7bbe7094378869b50f403fff889_0_pnlRow"]/div/div/div[3]/div[2]/table/tbody/tr['+str(count)+']')))
            except TimeoutException:
                break
            tr = driver.find_element_by_xpath('//*[@id="contentmypages_1_rowplaceholder6279a7bbe7094378869b50f403fff889_0_pnlRow"]/div/div/div[3]/div[2]/table/tbody/tr['+str(count)+']')
            tds = tr.find_elements_by_tag_name('td')

            if not facility_ids == 'ALL' and tds[2].text not in facility_ids:
                count += 1
                continue

            curr_facility_id = tds[2].text
                    
            a_tag_click = tds[3].find_elements_by_tag_name('a')[1]
            a_tag_click.click()
            try:
                wait.until(presence_of_element_located((By.XPATH,'//*[@id="contentmypages_0_rowplaceholdere4ea818a20a648c693f0db4e87d91ec7_0_blockplaceholder1b3ee104966734570a21245d44117f453_0_desktop"]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/select/option[4]')))
            except TimeoutException:
                count += 1
                driver.back()
                continue
            #Resolution changes
            select_catg = Select(driver.find_element_by_xpath('//*[@id="contentmypages_0_rowplaceholdere4ea818a20a648c693f0db4e87d91ec7_0_blockplaceholder1b3ee104966734570a21245d44117f453_0_desktop"]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/select'))
            select_catg.select_by_visible_text('Timme')

            if period is not None:
                select_catg = Select(driver.find_element_by_xpath('//*[@id="contentmypages_0_rowplaceholdere4ea818a20a648c693f0db4e87d91ec7_0_blockplaceholder1b3ee104966734570a21245d44117f453_0_desktop"]/div/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/select'))
                select_catg.select_by_visible_text('Valfritt datum')
                wait.until(EC.visibility_of_element_located((By.ID,'pickerfrom')))
                from_range = driver.find_element_by_id('pickerfrom')
                to_range = driver.find_element_by_id('pickerto')
                from_range.clear()
                from_range.send_keys(period.split(';')[0])
                to_range.clear()
                to_range.send_keys(period.split(';')[1])

            prev_file_count = len(os.listdir(os.getcwd()))
                    
            exportera = driver.find_element_by_xpath('//*[@id="contentmypages_0_rowplaceholdere4ea818a20a648c693f0db4e87d91ec7_0_blockplaceholder1b3ee104966734570a21245d44117f453_0_desktop"]/div/div[2]/div/div[2]/div[3]/div[2]/div[3]/div/div/a[2]')
            if exportera is not None:
                exportera.click()
                chart = driver.find_element_by_xpath('//*[@id="contentmypages_0_rowplaceholdere4ea818a20a648c693f0db4e87d91ec7_0_blockplaceholder1b3ee104966734570a21245d44117f453_0_desktop"]/div/div[2]/div/div[2]/div[3]/div[1]/div[2]')
                while('block' not in chart.get_attribute("style")):
                    time.sleep(1)
                
                #Check for download success and handle failure accordingly : How do I get to know if download fails? Maybe keep a threshold of 10-15 seconds, if file not found after that report as failure
                while(len(os.listdir(os.getcwd())) - prev_file_count == 0):
                    time.sleep(1)
                    
            print('Downloaded',curr_facility_id)

            driver.back()
            count += 1


username = 'norrvidden'
password = 'Argus92'
typ = 0
facility_ids = ['30000000386']
# period = '2020-01-01;2020-01-31'
period = None

if __name__ == "__main__":
    UmeaEnergi(username,password)
