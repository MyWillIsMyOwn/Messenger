import mysql.connector
import re


def connect():
    return mysql.connector.connect(
        user="root",
        password="Demon123@",
        host="127.0.0.1",
        database="Messenger",
        auth_plugin="auth_native_password",
    )


def register(usertype="normal"):
    valid_email_format = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    username = input("Please enter new username... ")
    password = input("Please enter your password... ")
    while True:
        email = input("Please enter your email... ")
        if re.fullmatch(valid_email_format, email):
            break
        else:
            print("Invalid email format\n")

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

    connected_data_base = connect()
    cursor = connected_data_base.cursor()
    cursor.execute(input_user_command, input_user_data)
    connected_data_base.commit()
    print("User added correctly")
    connected_data_base.close()


register()
