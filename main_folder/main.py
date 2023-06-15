from main_folder.session import Session
from main_folder.user_maintance import Maintain
from main_folder.utils import display_commands


def main():
    while True:
        match input():
            case "login":
                session = Session()
                session.log_in()
            case "create":
                register = Maintain()
                register.register()
            case "exit":
                exit()
            case "help":
                display_commands("main")
            case _:
                print("""Type "help" to see available commands\n""")


if __name__ == "__main__":
    main()
