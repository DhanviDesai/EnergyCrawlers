from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path
import os

chrome_path = r'C:\Users\Dhanvi\Headless_Browsers\chromedriver'

def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_experimental_option("prefs", {
            "download.default_directory": str(os.path.join(Path.home(), "Downloads")),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
    })
    driver = webdriver.Chrome(executable_path = chrome_path,options=chrome_options)
    download_dir = os.getcwd()
    enable_download_headless(driver, download_dir)
    return driver