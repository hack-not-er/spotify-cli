from selenium import webdriver
import os, sys, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    

driver = webdriver.Chrome(executable_path='E:\SeleniumDrivers\chromedriver.exe')


def login():
    
    #username field

    #wait for the username field to be visible
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-username')))
    username.send_keys('xx')

    #password field
    password = driver.find_element_by_id('login-password')
    password.send_keys('xxx')
    time.sleep(1)

    #click login button
    driver.find_element_by_id('login-button').click()

#
def play():
    global playButton
    playButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[data-testid='play-button'][class='Button-qlcn5g-0 kgFBvD']")))

    exists = ''
    try:
        banner_close = driver.find_element_by_id('onetrust-close-btn-container')
        exists = True
    except NoSuchElementException:
        exists = False
    if exists:
        banner_close.click()
    shuffle = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[data-testid='control-button-shuffle']")))

    print(shuffle.get_attribute('aria-label'))
    if shuffle.get_attribute('aria-label') == 'Enable shuffle':
        shuffle.click()

    time.sleep(1)
    
    #click play button
    playButton.click()
