from data_base import connect
from user import User

from admin import Admin
import getpass


normal_user = User()
admin_user = Admin()


class Session:
    def __init__(self):
        self.nickname = input("Enter username...\n")
        self.password = getpass.getpass("Enter your password... \n")

    def authentication(self):
        connected_data_base = connect()
        log_in_data = connected_data_base.cursor()
        log_in_data.execute(
            """SELECT id, password FROM Messenger.users where username = %s""",
            [self.nickname],
        )
        data = log_in_data.fetchone()
        if not data:
            return False
        correct_password = data[1]
        return correct_password == self.password

    def check_privilages(self):
        connected_data_base = connect()
        log_in_data = connected_data_base.cursor()
        log_in_data.execute(
            """SELECT id, usertype FROM Messenger.users where username = %s""",
            [self.nickname],
        )
        data = log_in_data.fetchone()
        privilages = data[1]
        match privilages:
            case "normal":
                normal_user.user_session(self.nickname)
            case "admin":
                admin_user.admin_session(self.nickname)
            case _:
                print("Unknown user type, back to main menu")
                return

    def log_in(self):
        cnt = 0
        while cnt < 2:
            if self.authentication():
                return self.check_privilages()
            else:

                print("Invalid username or password, try again")
                cnt += 1
                Session()
        print("Given wrong password 3 times, returning to main menu...")
        return False
