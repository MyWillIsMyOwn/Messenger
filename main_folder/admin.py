# from utils import Messages, display_commands
# from data_base import UserFinder
# from user_maintance import register, remove_user

# find = UserFinder()
# message = Messages()


# class Admin:
#     @staticmethod
#     def admin_session(username):
#         while True:
#             print(f"--{username}-- as administrator")
#             admin_command = input("Enter command\n")
#             match admin_command:
#                 case "help":
#                     display_commands("admin_session")
#                 case "users":
#                     find.print_users(input())
#                 case "messages":
#                     message.display_messages(
#                         username=username, interlocutor=input("Enter username...\n")
#                     )
#                 case "write":
#                     message.write_message(username)
#                 case "create":
#                     usertype = input(
#                         """Type "normal" to create normal user or "admin" to create admin user\n"""
#                     )
#                     match usertype:
#                         case "normal":
#                             register()
#                         case "admin":
#                             print(
#                                 "Are you sure that you want to create admin usertype? y/n"
#                             )
#                             if input("") == "y":
#                                 register(usertype="admin")
#                         case _:
#                             print("Unkown usertype")
#                 case "delete":
#                     remove_user(
#                         username=input("Enter username to delete\n"),
#                         answer=input(
#                             "Do you really want to delete your account ? y/n\n"
#                         ),
#                     )
#                 case "logout":
#                     print(f"User {username} logged out correctly")
#                     return
#                 case _:
#                     print(
#                         """Unkown command, type "help" to display all available commands"""
#                     )
