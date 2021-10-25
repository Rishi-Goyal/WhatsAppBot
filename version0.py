from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

  
# create webdriver object
i = 0
a = "https://web.whatsapp.com/"


driver = webdriver.Firefox()

    
c = random.randint(220,360)
driver.get(a)
wait = WebDriverWait(driver, 600)
name = input('enter the number of users ')
n = name.split()
l = len(n) + 1
msg = input('enter your message ')
#count = int(input("enter the count "))
input('enter after scanning QR code')


for i in range(l):
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(n[i]))
    user.click()
    msg_box = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    time.sleep(2)
    button = driver.find_element_by_class_name('_1E0Oz')
    button.click()
    















