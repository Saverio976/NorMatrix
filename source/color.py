RED = '\033[0;31m'
BOLDRED = '\033[1;31m'
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
RESET = '\033[0m'

def print_color(color: str, message):
    choice = {
        "red": RED,
        "boldred": BOLDRED,
        "cyan": CYAN,
        "green": GREEN
    }
    print(f"{choice.get(color, '')}{message}{RESET}")
