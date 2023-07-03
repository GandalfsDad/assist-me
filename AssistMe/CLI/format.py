from colorama import Fore

def format_input(input_text: str) -> str:
    return f"{Fore.GREEN}{input_text}{Fore.RESET}"

def format_response(name: str, response_text: str) -> str:
    return f"{Fore.RED}{name}{Fore.RESET}: {response_text}"