from main_folder.data_base import connect
from main_folder.user import User
from main_folder.admin import Admin
import getpass

normal_user = User()
admin_user = Admin()

class Session:
    def __init__(self, nick=None):
        if nick:
            self.nickname = nick
        else:
            self.nickname = input("Enter username...\n")
        self.db_password = None
        self.usertype = None
        self.password = None

    def authentication(self):
        return self.db_password == self.password

    def check_privilages(self):
        match self.usertype:
            case "normal":
                normal_user.user_session(self.nickname)
            case "admin":
                admin_user.admin_session(self.nickname)
            case _:
                print("Unknown user type, back to main menu")
                return

    def log_in(self):
        if not self.nickname:
            print("No username is given, returning to main menu...\n")
            return False
        self.get_user_data()
        cnt = 0
        while cnt < 3:
            self.read_password()
            if self.authentication():
                return self.check_privilages()
            else:
                cnt += 1
                self.password = None
                print("Invalid username or password, try again\n")
        print("Given wrong password 3 times, returning to main menu...")
        return False

    def read_password(self):
        self.password = getpass.getpass("Enter your password... \n")

    def get_user_data(self):
        connected_data_base = connect()
        log_in_data = connected_data_base.cursor()
        log_in_data.execute(
            """SELECT * FROM Messenger.users where username = %s""",
            [self.nickname],
        )
        data = log_in_data.fetchone()
        if data:
            self.db_password = data[2]
            self.usertype = data[3]