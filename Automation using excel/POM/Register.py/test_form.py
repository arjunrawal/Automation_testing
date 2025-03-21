from selenium import webdriver
from form import registerpage
from time import sleep

driver = webdriver.Chrome()

# Create an instance of registerpage
new_register = registerpage(driver)

# Open the registration page
new_register.open()

# Perform form fill-up
new_register.formC("arjun", "rawal", "arjun21@gmail.com", "82838322332", "arjun21@", "arjun21@")

# Wait for 10 seconds to see the result 
sleep(10)

# Close the browser
driver.quit()
