from Screens.Home_Screens.Home_Account_Screen import home_account_screen
from Screens.Home_Screens.Home_Deck_Screen import home_deck_screen
from Screens.Home_Screens.Home_Games_Screen import home_game_screen
from Screens.Home_Screens.Home_Screen_base import home_screen_base_page
from Screens.Login_Screens.Create_Account_Screen import create_account_screen
from Screens.Login_Screens.Home_Login_Screen import home_login_screen
from Screens.Login_Screens.Login_Screen import login_screen


def get_new_screen(screen_name, user):
    if screen_name == 'home base':
        return home_screen_base_page(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home login':
        return home_login_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'login':
        return login_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'create account':
        return create_account_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home decks':
        return home_deck_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home games':
        return home_game_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home account':
        return home_account_screen(user.display_width, user.display_height, user.profile, user)

