from colorama import Back, Fore, Style, init

init(autoreset=True)
messages = [
    "blah blah blah",
    (Fore.LIGHTYELLOW_EX + Style.BRIGHT + Back.MAGENTA + "Alert!!!"),
    "blah blah blah",
]
for m in messages:
    print(m)
