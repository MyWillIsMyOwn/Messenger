from utils import Messages, display_commands
from data_base import UserFinder
from user_maintance import Maintain

find = UserFinder()
message = Messages()


class User:
    @staticmethod
    def user_session(username):
        while True:
            print(f"--{username}--")
            user_command = input("Enter command\n")
            match user_command:
                case "help":
                    display_commands("user_session")
                case "messages":
                    message.display_messages(
                        sender_nickname=username,
                        interlocutor=input("Enter username...\n"),
                    )
                case "write":
                    message.write_message(
                        your_nickname=username,
                        receiver=input("Enter username...\n"),
                    )
                case "users":
                    find.print_users(input())
                case "logout":
                    print(f"User {username} logged out correctly")
                    return
                case "delete":
                    remove = Maintain()
                    remove.remove_user(
                        username=username,
                        answer=input(
                            "Do you really want to delete your account ? y/n\n"
                        ),
                    )
                    return
                case _:
                    print(
                        """Unkown command, type "help" to display all available commands"""
                    )
