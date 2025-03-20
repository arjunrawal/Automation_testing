from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        
        # Locators for elements on the login page
        self.username = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self):
        """Opens the login page."""
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def loginC(self, username, password):
        """Performs login action with wait to ensure elements are loaded."""
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        
        # Enter username, password and click login button
        wait.until(EC.presence_of_element_located(self.username)).send_keys(username)
        wait.until(EC.presence_of_element_located(self.password)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
