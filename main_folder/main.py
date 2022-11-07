from session import Session
from user_maintance import Maintain
from utils import display_commands


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
                print("""Type "help" to see available commands""")


if __name__ == "__main__":
    main()
