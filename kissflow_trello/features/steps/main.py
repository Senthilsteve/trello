
from features.config.config import config
from features.pages.homepage import home_page
from features.pages.default import default_page
from features.pages.utils import util
from behave import given, when, then

class main:

    driver = config.driver
    util_obj = util(config.driver)
    home_obj = home_page(driver,util_obj)
    default_obj = default_page(driver,util_obj)

    @given('Login into Trello using credentials')
    def login(context):

        main.home_obj.navigate_login_trello(config.user_name, config.password)

    @when('Create a new Board "{board}"')
    def create_board(context,board):

        main.default_obj.create_board(board)

    @then('Create "{count}" Lists with status as "{list1}", "{list2}", "{list3}", "{list4}"  respectively')
    def create_list(context,count,list1,list2,list3,list4):

        list =[list1,list2,list3,list4]

        if int(count) == len(list):
            main.default_obj.create_list_main(list)
        else:
            assert False , "Mismacth in list count "

    @then('Create "{count}" Cards. : "{card1}", "{card2}", "{card3}", "{card4}" under the list "{list}".')
    def create_board(context,count, card1,card2,card3,card4,list):

        card = [card1,card2,card3,card4]

        if int(count) == len(card):
            main.default_obj.add_card_fn(card,list)
        else:
            assert False , "Mismacth in card count "


    @then('Move Card "{card}" to "{list}".')
    def move_card(context,card,list):

        main.default_obj.move_card_to_different_list(card,list)

    @then('Open Card "{card}" and Assign it to the current logged in user and then leave a comment on Card  saying "{comment}"')
    def step_impl(context,card,comment):

        main.default_obj.assign_enter_comment(card,comment)





