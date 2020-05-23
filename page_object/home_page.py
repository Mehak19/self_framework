from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    pop_up=(By.XPATH, '''//button[.="✕"]''')
    elctronic=(By.XPATH,'''//span[.="Electronics"]''')
    samsung_s10=(By.XPATH,'''//a[.="Samsung S10 Lite"]''')

    def close_popup(self):
        return self.driver.find_element(*HomePage.pop_up)

    def mousehover_electronic(self):
        return self.driver.find_element(*HomePage.elctronic)

    def moverhover_electronic_operation(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.mousehover_electronic()).click().perform()

    def select_samsungs10(self):
        return self.driver.find_element(*HomePage.samsung_s10)