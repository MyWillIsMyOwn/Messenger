from main_folder.data_base import connect, UserFinder
import mysql
import re
import getpass

find = UserFinder()


class Maintain:
    def __init__(self, usertype="normal"):
        self.email = input("Please enter your email...\n")
        self.username = input("Please enter new username...\n")
        self.password = getpass.getpass("Please enter your password...\n")
        self.usertype = usertype

    def register(self):
        valid_email_format = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        while True:
            if re.fullmatch(valid_email_format, self.email) or self.email == "exit":
                break
            else:
                print("Invalid email format\n")
                self.email = input("Please enter your email again...\n")
                continue

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
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "usertype": self.usertype,
        }
        try:
            connected_data_base = connect()
            cursor = connected_data_base.cursor()
            cursor.execute(input_user_command, input_user_data)
            connected_data_base.commit()
            connected_data_base.close()
        except mysql.connector.IntegrityError:
            if find.check_user_existance(self.username):
                print(f"""Username named: "{self.username}" already exists""")
            else:
                print(f"""Email: "{self.email}" alredy exists""")
            return
        except mysql.connector.DatabaseError as e:
            print("Couldn't register user right now, try later...")
            print(e)
            return
        print(f"User {self.username} added correctly")


class Remove:
    @staticmethod
    def remove_user(username_to_delete, answer):
        if answer == "y":
            if not find.check_user_existance(username_to_delete):
                print(f"Couldn't find user named {username_to_delete}")
                return
            connected_data_base = connect()
            choose_user = connected_data_base.cursor()
            choose_user.execute(
                """DELETE FROM Messenger.users WHERE username = %s""",
                [username_to_delete],
            )
            connected_data_base.commit()
            connected_data_base.close()
            print(f"Account {username_to_delete} has been deleted\n")
        return
