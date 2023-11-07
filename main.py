import time

# import webdriver from selenium
from selenium import webdriver
   
# Choose browser of your wish
# In the case of Firefox, use webdriver.Firefox()
driver = webdriver.Chrome(executable_path = 'chromedriver.exe')

# provide an URL 
url = "https://multitab.io.vn/"

# opening the url in the browser
driver.get(url)

# give a delay for 10 seconds
time.sleep(10)

# close the browser
driver.close()