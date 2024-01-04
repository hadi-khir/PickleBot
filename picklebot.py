from datetime import time, timedelta, timezone
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

reservation_url = 'https://theracentre.my.site.com/?state=#/app/dashboard'
begin_time = time(0,0)
end_time = time(0,5)
max_try = 10
reservation_time = int(sys.argv[1])

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)
driver = webdriver.Chrome(options=options)

est = timezone(timedelta(hours=+9), 'EST')

while True:
    
    print("Navigating to reservation home page...")
    driver.get(reservation_url)
    sleep(3)

    print("Logging in...")
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[1]/div/div/a').click()
    sleep(3)
    
    print("Switching to iframe...")
    iframe = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/form/iframe')
    driver.switch_to.frame(iframe)
    
    print("Entering username and password...")
    username = driver.find_element(By.XPATH, '//*[@id="j_id0:j_id5:loginComponent:loginForm:username"]')
    password = driver.find_element(By.XPATH, '//*[@id="j_id0:j_id5:loginComponent:loginForm:password"]')
    username.send_keys('khir.hadi@gmail.com')
    password.send_keys('GrBbE7BnZBwt5C')
    driver.find_element(By.XPATH, '//*[@id="j_id0:j_id5:loginComponent:loginForm:loginButton"]').click()
    sleep(2)

    driver.get('https://theracentre.my.site.com/#/app/program/calendar/DIV-002/?cat1=Pickleball%20Court%20Booking&cat2=Pickleball%20Court%20Bookings#program-card-list')
    sleep(5)

    date_input = driver.find_element(By.XPATH, '//*[@id="program-schedule"]/div[1]/div[2]/div/input')
    date_input.clear()
    date_input.send_keys('2024')
    date_input.send_keys(Keys.TAB)
    date_input.send_keys('01')
    date_input.send_keys('06')
    sleep(5)

    court_slot = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[3]/div/div[2]/a[4]')
    court_slot.click()
    sleep(5)
