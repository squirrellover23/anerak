import json

from Screens.All_Screen_Handler import get_new_screen
from Profile import profile, guest, login


class user:
    def __init__(self, connection):
        self.connection = connection
        self.login_prof = login

        self.display_width = 1500
        self.display_height = 900

        self.guest_mode = True
        self.playing_game = False
        self.is_typing = False
        self.profile = login
        self.current_screen = get_new_screen(login.default_screen, self)
        self.profile = self.current_screen.profile
        self.draw = []
        self.non_mov_obs = []
        self.move_screen = []
        self.draw_images = []
        self.draw_current_screen()

    def get_draw(self):
        x = self.draw + []
        b = self.non_mov_obs + []
        z = self.move_screen + []
        self.draw = []
        self.non_mov_obs = []
        self.move_screen = []
        return json.dumps({"draw": x, "non_move": b, "screen_to": z, "key_input": self.current_screen.movement, "is_typing": self.is_typing})

    def screen_to(self, x, y):
        self.move_screen = [x, y]

    def add_draw_info(self, ob_to_draw):
        if ob_to_draw[0] == 1:
            self.draw.append({"type": ob_to_draw[1], "parameters": ob_to_draw[2]})
        if ob_to_draw[0] == 2:
            self.non_mov_obs.append({"type": ob_to_draw[1], "parameters": ob_to_draw[2]})

    def make_new_game(self, tribes, game_player_type, game_info):
        pass

    def draw_current_screen(self):
        self.draw = []
        self.non_mov_obs = []
        self.draw_images = []
        if self.current_screen.update_screen > 0:
            self.current_screen.update_screen -= 1
            draw_stuff = self.current_screen.draw_screen()
            for o in draw_stuff:
                self.add_draw_info(o)

    def change_screen(self, change_screen_to):
        self.current_screen = get_new_screen(change_screen_to, self)
        self.current_screen.update_screen = 3
        self.screen_to(self.current_screen.reset_x, self.current_screen.reset_y)
        self.draw_current_screen()

    def handle_input(self, input):
        if input['MOTION']:
            self.current_screen.button_mouse_motion(input['POS'], input['SCREENPOS'], input['ZOOM'])
        if input['CLICK']:
            self.current_screen.button_mouse_motion(input['POS'], input['SCREENPOS'], input['ZOOM'])
            self.current_screen.handle_mouse_click(input['POS'], input['SCREENPOS'], input['ZOOM'])
        if self.is_typing:
            self.current_screen.handle_text_typed(input['TYPINGTEXT'])
        self.draw_current_screen()

    def login_attempt(self, username, password):
        login_info = self.profile.try_login(username, password)
        print(login_info[0])
        if login_info[1] is not None:
            self.change_profile(login_info[1])

        return login_info[0]

    def new_account_attempt(self, username, password):
        error = ''
        if len(username) < 4:
            error = 'Username is too short'
        if not self.profile.try_new_username(username):
            error = 'Username is already taken'
        if len(password) < 6:
            error = 'Password is too short'
        if error == '':
            self.change_profile(profile(username, password))
            print('New account created?!')
        return error

    def change_profile(self, new_profile: profile):
        self.profile = new_profile
        self.change_screen(new_profile.default_screen)
