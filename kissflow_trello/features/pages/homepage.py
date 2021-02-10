

from selenium.webdriver.common.by import By
from features.config.config import config
from features.pages.utils import util
import time

class home_page:

    btn_login = (By.LINK_TEXT,"Log In")

    text_user = (By.ID,"user")

    text_pass = (By.XPATH,"//*[@placeholder=\"Enter password\"]")

    log_in = (By.ID,"login")

    log_submit_in = (By.ID,"login-submit")

    text_team = (By.ID,"moonshotCreateTeam")

    def __init__(self,driver,util):
        self.driver = driver
        self.obj_util = util

    def navigate_login_trello(self,username,  password):

        self.driver.get(config.URl)

        self.obj_util.on_click(self.btn_login)

        self.obj_util.enter_value( self.text_user, username)

        self.obj_util.on_click(self.log_in)

        time.sleep(2)

        self.obj_util.enter_value(self.text_pass, password)

        self.obj_util.on_click(self.log_submit_in)
