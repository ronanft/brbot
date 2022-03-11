class AllBots:
    def __init__(self, kwargs):
        self.meta5_login = {
            "login": kwargs.get("mtlogin"),
            "password": kwargs.get("mtpass"),
            "server": kwargs.get("mtserver"),
        }

    def display(self):
        print(
            self.meta5_login
            # "ID: %d \nName: %s \nServer: %s"
            # % (self.meta5_login, self.meta5_pass, self.meta5_server)
        )
