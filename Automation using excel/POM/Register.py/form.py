from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import registerL

class registerpage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    def formC(self, first_name, last_name, email, telephone, pwd, confirm_pwd):
        wait = WebDriverWait(self.driver, 10)

        # Fill in text fields
        wait.until(EC.presence_of_element_located(registerL.First_Name)).send_keys(first_name)
        wait.until(EC.presence_of_element_located(registerL.Last_Name)).send_keys(last_name)
        wait.until(EC.presence_of_element_located(registerL.Email)).send_keys(email)
        wait.until(EC.presence_of_element_located(registerL.Telephone)).send_keys(telephone)
        wait.until(EC.presence_of_element_located(registerL.password)).send_keys(pwd)
        wait.until(EC.presence_of_element_located(registerL.Confirm_password)).send_keys(confirm_pwd)


#----------------------------for condition for chosing options-----------
    
        # # Click the subscribe radio button
        # subscribe_radio = wait.until(EC.element_to_be_clickable(registerL.subscribe_button))
        # if not subscribe_radio.is_selected():  # Check if already selected
        #     subscribe_radio.click()
        
        # # Click the privacy policy checkbox
        # privacy_checkbox = wait.until(EC.element_to_be_clickable(registerL.Privacypolicy_button))
        # if not privacy_checkbox.is_selected():  # Check if already selected
        #     privacy_checkbox.click()
        
        # # Click Continue to submit the form
        # wait.until(EC.element_to_be_clickable(registerL.Continue_button)).click()

#--------for directly choosing------------------

        # Click the "Yes" radio button directly
        wait.until(EC.element_to_be_clickable(registerL.subscribe_button)).click()

        # Click the Privacy Policy checkbox directly
        wait.until(EC.element_to_be_clickable(registerL.Privacypolicy_button)).click()

        # Click the Continue button to submit the form
        wait.until(EC.element_to_be_clickable(registerL.Continue_button)).click()

