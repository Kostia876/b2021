from colorama import *


init()
from colorama import Fore, Back, Style
print(Fore.RED + 'maximal')
print(Back.YELLOW + 'maximal')
print(Style.DIM + 'maximal')
print(Style.RESET_ALL)
print('maximal?')

print('\033[31m' + ' red text')
print('\033[39m')


print(Back.BLUE + 'maximal')
print(Fore.YELLOW + 'maximal')
print('\033[31m' + 'maximal')
print('\033[39m') # and reset to default color
init(autoreset=True)
print(Fore.RED + ' red text')
print('???')


