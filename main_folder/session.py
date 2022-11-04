from data_base import connect, check_user_existance
from user import user_session
from admin import admin_session
import getpass


def authentication(nickname, password):
    if not check_user_existance(nickname):
        return False
    connected_data_base = connect()
    log_in_data = connected_data_base.cursor()
    log_in_data.execute(
        """SELECT id, password FROM Messenger.users where username = %s""",
        [nickname],
    )
    data = log_in_data.fetchone()
    correct_password = data[1]
    return correct_password == password


def log_in():
    cnt = 0
    while cnt < 3:
        nickname = input("Enter username...\n")
        password = getpass.getpass("Enter your password... \n")

        if authentication(nickname=nickname, password=password):
            return check_privilages(nickname)
        else:
            print("Invalid username or password, try again")
            cnt += 1
    print("Given wrong password 3 times, returning to main menu...")
    return False


def check_privilages(nickname):
    connected_data_base = connect()
    log_in_data = connected_data_base.cursor()
    log_in_data.execute(
        """SELECT id, usertype FROM Messenger.users where username = %s""",
        [nickname],
    )
    data = log_in_data.fetchone()
    privilages = data[1]
    match privilages:
        case "normal":
            user_session(nickname)
        case "admin":
            admin_session(nickname)
        case _:
            print("Unknown user type, back to main menu")
            return
