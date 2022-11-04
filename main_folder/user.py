from utils import display_commands, display_messages, write_message
from data_base import print_users
from user_maintance import remove_user


def user_session(username):
    while True:
        print(f"--{username}--")
        user_command = input("Enter command\n")
        match user_command:
            case "help":
                display_commands("user_session")
            case "messages":
                display_messages(
                    username=username, interlocutor=input("Enter username...\n")
                )
            case "write":
                write_message(username)
            case "users":
                print_users(input())
            case "logout":
                print(f"User {username} logged out correctly")
                return
            case "delete":
                remove_user(
                    username=username,
                    answer=input("Do you really want to delete your account ? y/n\n"),
                )
                return
            case _:
                print(
                    """Unkown command, type "help" to display all available commands"""
                )
