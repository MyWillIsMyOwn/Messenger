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
    nickname = input("Enter username...")
    if check_user_existance(nickname):
        connected_data_base = connect()
        correct_password = connected_data_base.cursor()
        correct_password.execute(
            """SELECT password FROM Messenger.users where username = %s""", [nickname]
        )
        counter = 0
        while counter < 3:
            password = getpass.getpass("Enter your password... ")
            if correct_password.fetchone() == (f"{password}",):
                print("TAK")

            # if password == correct_password: session()
            else:
                print("Invalid password, try again")
                counter += 1
        print("Given wrong password 3 times, returning to main menu...")
        main()
        connected_data_base.close()
    else:
        print(
            '''Looks like account with given username doesn't exist, in case of register type "register", to exit program type "exit"'''
        )


def log_out():
    # main()
    pass


def session(username, usertype):
    pass


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


def check_user_existance(username):
    connected_data_base = connect()
    cursor = connected_data_base.cursor()
    cursor.execute("SELECT username, email FROM Messenger.users")
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
        email = input("Please enter your email... ")
        if re.fullmatch(valid_email_format, email):
            break
        else:
            print("Invalid email format\n")
    username = input("Please enter new username... ")
    password = getpass.getpass("Please enter your password... ")

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


# register()
# log_in()
def main():
    while True:
        match input(
            """Welcome to my messenger, already have an account? Type "login" to log in to app or "register" to create one. To quite type "exit"\n"""
        ):
            case "login":
                log_in()
            case "register":
                register()
            case "exit":
                exit()


if __name__ == "__main__":
    main()
