from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Starts a webdriver isntance and opens chatGPT
driver = webdriver.Chrome(executable_path='/Users/stephenhuang/Desktop/Script Testing/chromedriver_mac64/chromedriver')
driver.get('https://www.google.com/')

# Finds input field and writes question and send
input_field = driver.find_element_by_class_name('gLFyf')
input_field.send_keys('nba')
input_field.send_keys(Keys.RETURN)

# Wait
driver.implicity_wait(10)

# Get Results

