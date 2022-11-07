from utils import Messages, display_commands
from data_base import UserFinder
from user_maintance import Maintain, Remove

find = UserFinder()
message = Messages()


class Admin:
    @staticmethod
    def admin_session(username):
        while True:
            if not find.check_user_existance(username):
                return
            print(f"--{username}-- as administrator")
            admin_command = input("Enter command\n")
            match admin_command:
                case "help":
                    display_commands("admin_session")
                case "users":
                    find.print_users(input())
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
                case "create":
                    usertype = input(
                        """Type "normal" to create normal user or "admin" to create admin user\n"""
                    )
                    match usertype:
                        case "normal":
                            create = Maintain()
                            create.register()
                        case "admin":
                            print(
                                "Are you sure that you want to create admin usertype? y/n"
                            )
                            if input("") == "y":
                                create = Maintain("admin")
                                create.register()
                        case _:
                            print("Unkown usertype")
                case "delete":
                    user = input("Enter username to delete\n")
                    remove = Remove()
                    remove.remove_user(
                        username_to_delete=user,
                        answer=input(
                            "Do you really want to delete your account ? y/n\n"
                        ),
                    )
                    if not find.check_user_existance(username):
                        return
                case "logout":
                    print(f"User {username} logged out correctly")
                    return
                case _:
                    print(
                        """Unkown command, type "help" to display all available commands\n"""
                    )
