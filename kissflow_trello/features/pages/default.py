from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class default_page:

    plus_button = (By.XPATH,"//*[@data-test-id='header-create-menu-button']")
    board_name_text =(By.XPATH,"//input[@placeholder='Add board title']")
    create_board_btn = (By.XPATH,"//p[contains(text(),'A board is made up of cards')]")
    create_btn = (By.XPATH,"//*[@data-test-id=\"create-board-submit-button\" ]")
    create_list = (By.XPATH,"//span[@class='placeholder']")
    add_list = (By.XPATH,"//input[@value='Add List']")
    add_new_list = (By.CLASS_NAME,"list-name-input")
    add_new_card_under_not_started = (By.XPATH,"//h2[text()='Not Started']/parent::*/following-sibling::div[@class='card-composer-container js-card-composer-container']/descendant::*[text()='Add a card']")
    add_card_details = (By.XPATH,"//*[@placeholder='Enter a title for this card…']")
    add_card = (By.XPATH,"//input[@value='Add Card']")
    ele_Move = (By.XPATH,"//a[@title='Move']")
    ele_list = (By.CLASS_NAME,"js-select-list")
    Move_button = (By.XPATH,"//*[@value='Move']")
    close_button = (By.XPATH,"//div[@data-elevation='1']/a")
    member_button = (By.XPATH,"//*[@title='Members']")
    select_first_member = (By.CLASS_NAME,"full-name")
    comment_box = (By.XPATH,"//div[@class='comment-box']//textarea")
    save_btn = (By.XPATH,"//input[@value='Save']")
    close_list = (By.XPATH,"//a[@title='Close the board menu.']")

    def __init__(self,driver,util):
        self.driver =  driver
        self.obj_util = util


    def create_board(self,board_name):

        self.driver.maximize_window()

        self.obj_util.on_click(self.plus_button)

        self.obj_util.on_click(self.create_board_btn)

        self.obj_util.enter_value(self.board_name_text, board_name)

        time.sleep(2)

        self.obj_util.on_click(self.create_btn)


    def create_list_main(self,list):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.create_list)).click()
        except:
            print("")
        finally:
            for item in list:

                self.obj_util.enter_value(self.add_new_list, item)

                self.obj_util.on_click(self.add_list)

            self.obj_util.on_click(self.close_list)



    def add_card_fn(self, card, list_name):

        self.obj_util.on_click(self.add_new_card_under_not_started)

        for item in card:

            self.obj_util.enter_value(self.add_card_details, item)

            self.obj_util.on_click(self.add_card)


    def move_card_to_different_list(self, card, list):

        try:
            act = ActionChains(self.driver)

            ele = self.driver.find_element_by_xpath("//span[text()='Card " + card + "']/parent::*")

            ele_2 = self.driver.find_element_by_xpath("//h2[text()='"+list+"']/parent::*")

            act.drag_and_drop(ele, ele_2).perform()

        except:
            assert False ,"Failure! The drag and drop operation cannot be performed due to failure in element identification"

    def assign_enter_comment(self, card, string):
        try:
            self.driver.find_element_by_xpath("//span[text()='Card " + card + "']/parent::*").click()
        except:
            assert False , "Failure | .The element cannot be located using using"+ card


        self.obj_util.on_click(self.member_button)

        self.obj_util.on_click(self.select_first_member)

        self.obj_util.enter_value(self.comment_box, string)

        self.obj_util.on_click(self.save_btn)

        self.obj_util.on_click(self.close_button)

