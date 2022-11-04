from datetime import datetime
from data_base import connect, check_user_existance
import mysql


def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def write_message(sender):
    receiver = input("Who you want to send the message to\n")
    if check_user_existance(receiver):
        message = input("Enter text message\n")
        input_user_command = """INSERT INTO Messenger.messages(
        sender, 
        receiver, 
        text, 
        send_time
        ) VALUES(
            %(sender)s, 
            %(receiver)s, 
            %(text)s, 
            %(send_time)s
            )"""
        input_user_data = {
            "sender": sender,
            "receiver": receiver,
            "text": message,
            "send_time": get_time(),
        }
        try:
            connected_data_base = connect()
            cursor = connected_data_base.cursor()
            cursor.execute(input_user_command, input_user_data)
            connected_data_base.commit()
            connected_data_base.close()
        except mysql.connector.DatabaseError:
            print("Couldn't register user right now, try later...")
            return
        print(f"Message sent to {receiver}")
        return
    else:
        print(f"Couldn't find user named {receiver}")


def display_messages(username, interlocutor):
    connected_data_base = connect()
    messages = connected_data_base.cursor()
    messages.execute(
        "SELECT * FROM (SELECT id, sender, receiver, text, send_time FROM Messenger.messages ORDER BY id DESC LIMIT 30) AS sub ORDER BY id ASC"
    )
    nickname = ""
    for (id, sender, receiver, text, send_time) in messages:
        if (
            sender == username
            and receiver == interlocutor
            or sender == interlocutor
            and receiver == username
        ):
            if username == sender:
                nickname = "You"
            else:
                nickname = sender
            print("")
            print(f"{nickname} {send_time}")
            print(text)


def display_commands(func):
    commands = {
        "help": "shows all available commands",
        "login": "log in to messenger",
        "delete": "to delete an account",
        "logout": "log out from messenger",
        "create": "to create account",
        "users": "display first 10 users that nickname starts with given string",
        "messages": "display 30 last messeges from particular user",
        "write": "to write a message to particular user",
        "exit": "to quit the program",
    }
    main_list = ("login", "create", "exit")
    user = ("users", "messages", "write", "logout", "delete")
    admin = ("users", "messages", "write", "create", "delete", "logout", "delete")
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
