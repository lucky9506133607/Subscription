from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    button_login_xpath = "//button[@type='submit']"
    link_logout_LinkText = "Logout"

    # lets create a constructor to initiate our driver, and for that we will create our constructor which will invoke at the time of object creation.
    # what this constructor is doing is capturing the driver from the test case
    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(by=By.XPATH, value=self.textbox_username_id).clear()
        self.driver.find_element(by=By.XPATH, value=self.textbox_username_id).send_keys(username)
    def setPassword(self, password):
        self.driver.find_element(by=By.XPATH, value=self.textbox_password_id).clear()
        self.driver.find_element(by=By.XPATH, value=self.textbox_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(by=By.LINK_TEXT,value=self.link_logout_LinkText).click()

