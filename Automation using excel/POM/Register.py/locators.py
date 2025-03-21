from selenium.webdriver.common.by import By

class registerL:
    # Text Input Fields
    First_Name = (By.ID, "input-firstname")
    Last_Name = (By.ID, "input-lastname")
    Email = (By.ID, "input-email")
    Telephone = (By.ID, "input-telephone")
    password = (By.ID, "input-password")
    Confirm_password = (By.ID, "input-confirm")

    # Radio Button (Subscribe to Newsletter: Yes)
    subscribe_button = (By.XPATH, '//input[@name="newsletter" and @value="1"]')

    # Checkbox (Privacy Policy Agreement)
    Privacypolicy_button = (By.XPATH, '//input[@name="agree"]')

    # Submit Button (Continue)
    Continue_button = (By.XPATH, '//input[@value="Continue"]')
