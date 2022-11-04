from data_base import connect, check_user_existance
import mysql
import re
import getpass


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


def remove_user(username, answer):
    if answer == "y":
        if not check_user_existance(username):
            return
        connected_data_base = connect()
        choose_user = connected_data_base.cursor()
        choose_user.execute(
            """DELETE FROM Messenger.users WHERE username = %s""",
            [username],
        )
        connected_data_base.commit()
        connected_data_base.close()
    return
