from main_folder.utils import Messages, display_commands
from main_folder.data_base import UserFinder
from main_folder.user_maintance import Remove

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
                    remove = Remove()
                    remove.remove_user(
                        username_to_delete=username,
                        answer=input(
                            "Do you really want to delete your account ? y/n\n"
                        ),
                    )
                    if not find.check_user_existance(username):
                        return
                case _:
                    print(
                        """Unkown command, type "help" to display all available commands\n"""
                    )
