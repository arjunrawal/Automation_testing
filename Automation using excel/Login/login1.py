from selenium.webdriver.common.by import By

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tutorialsninja.com/demo/index.php?route=account/login"

    def open(self):
        """Opens the login page."""
        self.driver.get(self.url)

    def login(self, email, password):
        """Performs login with the given credentials."""
        self.driver.find_element(By.ID, "input-email").send_keys(email) 
        self.driver.find_element(By.ID, "input-password").send_keys(password)  
        self.driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div/form/input").click()
