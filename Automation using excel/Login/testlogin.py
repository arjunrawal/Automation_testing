from selenium import webdriver
from login1 import LoginPage  # Import the LoginPage class
from time import sleep

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Create an instance of LoginPage
l = LoginPage(driver)

# Open the login page
l.open()

# Perform login
l.login("arjun21@gmail.com", "hey")

# Wait for 10 seconds to observe the result
sleep(10)

# Quit the driver
driver.quit()
