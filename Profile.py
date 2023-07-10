

class profile:
    all_profiles = []

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.games = {
            'pass and play': [],
            'online': [],
            'single player': []
        }
        self.games_played = 0
        self.elo = 1000
        self.decks = []
        self.online_game_invites = []
        self.friends = []
        self.all_profiles.append(self)
        self.default_screen = 'home home'

    def try_login(self, username, password):
        for prof in self.all_profiles:
            if prof.name == username:
                print('User Name exists')
                if prof.password == password:
                    return ['login success', prof]
                else:
                    return ['Wrong Password', None]
        return ['Username Does Not Exist', None]

    def try_new_username(self, username):
        for prof in self.all_profiles:
            if prof.name == username:
                return False
        return True


class login_prof(profile):
    def __init__(self):
        super().__init__('login', None)
        self.default_screen = 'start login'


class guest_profile(profile):
    def __init__(self):
        super().__init__('Guest', None)


guest = guest_profile()
login = login_prof()
bob = profile('', '')
