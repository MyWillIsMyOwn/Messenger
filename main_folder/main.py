from session import log_in
from utils import display_commands
from user_maintance import register


def main():
    while True:
        match input():
            case "login":
                log_in()
            case "create":
                register()
            case "exit":
                exit()
            case "help":
                display_commands("main")
            case _:
                print("""Type "help" to see available commands""")


if __name__ == "__main__":
    main()