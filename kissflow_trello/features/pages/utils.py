
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class util:

    def __init__(self,driver):
        self.driver = driver

    def on_click(self,by_locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()
        except:
            assert False,"Failure | .The element canot be located using"+ (''.join(by_locator))

    def enter_value(self, by_locator,value):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(value)
        except:
            assert False ,"Failure | .The element cannot be located using"+ (''.join(by_locator))