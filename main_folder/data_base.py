import mysql.connector


def connect():
    return mysql.connector.connect(
        user="root",
        password="niema",
        host="127.0.0.1",
        database="Messenger",
        auth_plugin="auth_native_password",
    )


class UserFinder:
    @staticmethod
    def check_user_existance(username):
        connected_data_base = connect()
        cursor = connected_data_base.cursor()
        cursor.execute("SELECT username FROM Messenger.users")
        for row in cursor:
            if username == row[0]:
                return True
        connected_data_base.close()
        print(f"Couldn't find username named {username}")
        return False

    def print_users(self, txt):
        connected_data_base = connect()
        users = connected_data_base.cursor()
        users.execute("SELECT id, username FROM Messenger.users")
        cnt = 0
        for (id, username) in users:
            if str(username).startswith(txt) and cnt < 10:
                print(username)
                cnt += 1
        connected_data_base.close()
