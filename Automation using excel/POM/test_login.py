from selenium import webdriver
from login import Loginpage  # Import Loginpage class from login.py
from time import sleep

# Initialize the WebDriver
driver = webdriver.Chrome()

# Create an instance of the Loginpage class
login = Loginpage(driver)

# Open the login page
login.open()

# Perform login with username and password
login.loginC("arjunrawal21@gmail.com", "arjun21@#")

# Wait for 10 seconds to see the result 
sleep(10)

# Close the browser
driver.quit()
