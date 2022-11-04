import mysql.connector
import re
import getpass


def connect():
    return mysql.connector.connect(
        user="root",
        password="niema",
        host="127.0.0.1",
        database="Messenger",
        auth_plugin="auth_native_password",
    )


def log_in():
    nickname = input("Enter username...\n")
    if check_user_existance(nickname):
        connected_data_base = connect()
        log_in_data = connected_data_base.cursor()
        log_in_data.execute(
            """SELECT password, usertype FROM Messenger.users where username = %s""",
            [nickname],
        )

        counter = 0
        data = log_in_data.fetchone()
        correct_password = data[0]
        usertype = data[1]
        while counter < 3:
            password = getpass.getpass("Enter your password... \n")
            print("coor", correct_password)
            if correct_password == password:
                connected_data_base.close()
                print("Logged in correctly...")
                match usertype:
                    case "admin":
                        admin_session(nickname)
                    case "user":
                        user_session(nickname)
                    case _:
                        print("Unkown usertype, returning to main menu")
                        main()
            else:
                print("Invalid password, try again")
                counter += 1
        print("Given wrong password 3 times, returning to main menu...")
    else:
        return "Looks like account with given username doesn't exist, getting back to main menu...\n"


def log_out(username):
    print(f"User {username} logged out correctly")
    main()


def user_session(username):
    while True:
        print(f"--{username}--")
        user_command = input("Enter command")
        match user_command:
            case "help":
                help("user_session")
            case "messages":
                pass
            case "write":
                pass
            case "users":
                pass
            case "logout":
                log_out(username)
            case _:
                print(
                    """Unkown command, type "help" to display all available commands"""
                )


def admin_session(username):
    while True:
        print(f"--{username}-- as administrator")
        admin_command = input("Enter command")
        match admin_command:
            case "help":
                help("admin_session")
            case "users":
                pass
            case "messages":
                pass
            case "write":
                pass
            case "create":
                usertype = input(
                    """Type "normal" to create normal user or "admin" to create admin user"""
                )
                match usertype:
                    case "normal":
                        register(usertype="normal")
                    case "admin":
                        register(usertype="admin")
                    case _:
                        print("Unkown usertype")
            case "delete":
                pass
            case "logout":
                log_out(username)
            case _:
                print(
                    """Unkown command, type "help" to display all available commands"""
                )


def show_users():
    connected_data_base = connect()
    users = connected_data_base.cursor()
    users.execute("SELECT username FROM Messenger.users")
    for user in users:
        print(user)
    connected_data_base.close()


def get_time():
    # to show what time message was sent
    pass


def display_messages():
    # who sent, who received, time, from particual user
    pass


def display_commands(func):
    commands = {
        "help": "shows all available commands",
        "login": "log in to messenger",
        "logout": "log out from messenger",
        "create": "create account",
        "delete": "delete account",
        "users": "display all available users",
        "messages": "display 100 last messeges from particular user",
        "write": "to write a message to particular user",
        "exit": "to quit the program",
    }
    main_list = ("login", "create", "exit")
    user = ("users", "messages", "write", "logout")
    admin = ("users", "messages", "write", "create", "delete", "logout")
    match func:
        case "main":
            for key, value in commands.items():
                if str(key).startswith(main_list):
                    print(f"""Type: "{key}" to {value}""")
        case "user_session":
            for key, value in commands.items():
                if str(key).startswith(user):
                    print(f"""Type: "{key}" to {value}""")
        case "admin_session":
            for key, value in commands.items():
                if str(key).startswith(admin):
                    print(f"""Type: "{key}" to {value}""")


def check_user_existance(username):
    connected_data_base = connect()
    cursor = connected_data_base.cursor()
    cursor.execute("SELECT username FROM Messenger.users")
    for row in cursor:
        if username == row[0]:
            return True
    connected_data_base.close()


def check_usertype():
    pass


def register(usertype="normal"):
    valid_email_format = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    while True:
        email = input("Please enter your email...\n")
        if re.fullmatch(valid_email_format, email):
            break
        else:
            print("Invalid email format\n")
    username = input("Please enter new username...\n")
    password = getpass.getpass("Please enter your password...\n")

    input_user_command = """INSERT INTO Messenger.users(
        username, 
        password, 
        email, 
        usertype
        ) VALUES(
            %(username)s, 
            %(password)s, 
            %(email)s, 
            %(usertype)s
            )"""
    input_user_data = {
        "username": username,
        "password": password,
        "email": email,
        "usertype": usertype,
    }
    try:
        connected_data_base = connect()
        cursor = connected_data_base.cursor()
        cursor.execute(input_user_command, input_user_data)
        connected_data_base.commit()
        connected_data_base.close()
    except mysql.connector.IntegrityError:
        if check_user_existance(username):
            print(f"""Username named: "{username}" already exists""")
        else:
            print(f"""Email: "{email}" alredy exists""")
        return
    except mysql.connector.DatabaseError:
        print("Couldn't register user right now, try later...")
        return
    print("User added correctly")


register()
# display_commands("main")


def main():
    while True:
        match input():
            case "login":
                log_in()
            case "create":
                register()
            case "exit":
                exit()
            case "help":
                display_commands("main")
            case _:
                print("""Type "help" to see available commands""")


# if __name__ == "__main__":
#     main()
