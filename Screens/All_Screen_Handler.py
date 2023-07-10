from Screens.Account_Screens.Account_Info_Screen import account_info_screen
from Screens.Account_Screens.Account_Settings_Screen import account_settings_screen
from Screens.Account_Screens.Account_Social_Screen import account_social_screen
from Screens.Account_Screens.Account_Stats_Screen import account_stats_screen
from Screens.Deck_Builder_Screens.Create_New_Deck_Start import create_new_deck_start
from Screens.Home_Screens.Home_Deck_Screen import home_deck_screen
from Screens.Home_Screens.Home_Games_Screen import home_game_screen
from Screens.Home_Screens.Home_Home_Screen import home_home_screen
from Screens.Login_Screens.Create_Account_Screen import create_account_screen
from Screens.Login_Screens.Start_Login_Screen import start_login_screen
from Screens.Login_Screens.Login_Screen import login_screen


def get_new_screen(screen_name, user):
    if screen_name == 'home home':
        return home_home_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'start login':
        return start_login_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'login':
        return login_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'create account':
        return create_account_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home decks':
        return home_deck_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home games':
        return home_game_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'home account':
        return account_info_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'account social':
        return account_social_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'account stats':
        return account_stats_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'account settings':
        return account_settings_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'view deck':
        print('Make this exist')
        # return account_settings_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'edit deck':
        print('Make this exist')
        # return account_settings_screen(user.display_width, user.display_height, user.profile, user)
    elif screen_name == 'create new deck start':
        return create_new_deck_start(user.display_width, user.display_height, user.profile, user)

    else:
        print('No Screen Named', screen_name)
