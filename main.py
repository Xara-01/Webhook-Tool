from pystyle import *; from colorama import *; import os

os.system('cls')
os.system('title WebHooks Tool - By xara-01')

b = Fore.BLUE
c = Fore.CYAN


print(Colorate.Horizontal(Colors.blue_to_cyan ,'''
                                        _     _                 _      _              _     
                          __      _____| |__ | |__   ___   ___ | | __ | |_ ___   ___ | |___ 
                          \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | __/ _ \ / _ \| / __|
                           \ V  V /  __/ |_) | | | | (_) | (_) |   <  | || (_) | (_) | \__ |
                            \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_\  \__\___/ \___/|_|___/   By xara-01
\n''', 1))

print(Colorate.Vertical(Colors.blue_to_cyan ,"""
                        ╔══════════════════════════════════╦═════════════════════════════════╗
                        ║             1: checker           ║          3: deletor             ║
                        ║══════════════════════════════════║═════════════════════════════════║
                        ║             2: spamer            ║          4: Credit              ║
                        ╚══════════════════════════════════╣═════════════════════════════════╝                                                               
\n""", 1))

cmd = input(f"{b}┌──({c}github.com/xara-01){b}-[{c}~{b}]\n{b}└─$ ")


if cmd == "1":
    os.system('cls')
    os.system('cmd /k "python utils/test.py"')

if cmd == "2":
    os.system('cls')
    os.system('cmd /k "python utils/spam.py"')

if cmd == "3":
    os.system('cls')
    os.system('cmd /k "python utils/del.py"')

if cmd == "4":
    os.system('cls')
    os.system('cmd /k "python utils/cred.py"')