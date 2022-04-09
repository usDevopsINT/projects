import logging
import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

logging.basicConfig(filename='pytestt.log' ,level=logging.DEBUG, datefmt='|%Y-%m-%d|%H:%M:%S|', format='%(asctime)s::%(levelname)-6s [%(filename)s:%(lineno)d]--->%(message)s')

driver = webdriver.Chrome(executable_path="chromedriver.exe") #change it to your web driver location

def selenium_b99():
    try:
        driver.maximize_window()
        driver.get("https://www.youtube.com/")
        search_youtube = driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
        search_youtube.send_keys(f" tell me why brooklyn 99")
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value=f"(//a[@id='video-title'])[1]").click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button").click()
    except not DeprecationWarning:
        logging.exception("something worng with selenium_b99 function")
        return False
    return True

selenium_b99()

"""
def test_selenium_b99():
    assert selenium_b99() == True
"""
