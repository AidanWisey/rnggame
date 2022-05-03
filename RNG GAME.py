import random
import time as t
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.RED + '''WELCOME TO:                                                  
 ____  _   _  ____    ____    _    __  __ _____ _ 
''' + Fore.YELLOW + '''|  _ \| \ | |/ ___|  / ___|  / \  |  \/  | ____| |
''' + Fore.GREEN + '''| |_) |  \| | |  _  | |  _  / _ \ | |\/| |  _| | |
''' + Fore.BLUE + '''|  _ <| |\  | |_| | | |_| |/ ___ \| |  | | |___|_|
''' + Fore.MAGENTA + '''|_| \_|_| \_|\____|  \____/_/   \_|_|  |_|_____(_)
Made by Aidan lol''')
colorama.init(autoreset=False)
t.sleep(1)
print(Fore.RED + 'Enter 1 to start level 1 (1/2 Chance):')
levelone = int(input(': '))
if levelone == 1:
    while True:
        levelonerng = random.randint(0, 1)
        print(levelonerng)
        if levelonerng == 0:
            break
        else:
            print(Fore.RED + 'Trying again...')
else:
    quit()
print(Fore.RED + 'Congratulations, you beat level 1 (1/2 chance)')
t.sleep(1)
print(Fore.YELLOW + 'Enter 1 to start level 2 (1/4 Chance):')
leveltwo = int(input(': '))
if leveltwo == 1:
    while True:
        leveltworng = random.randint(0, 3)
        print(leveltworng)
        if leveltworng == 0:
            break
        else:
            print(Fore.YELLOW + 'Trying again...')
else:
    quit()
print(Fore.YELLOW + 'Congratulations, you beat level 2 (1/4 chance)')
t.sleep(1)
print(Fore.GREEN + 'Enter 1 to start level 3 (1/8 Chance):')
levelone = int(input(': '))
if levelone == 1:
    while True:
        levelonerng = random.randint(0, 7)
        print(levelonerng)
        if levelonerng == 0:
            break
        else:
            print(Fore.GREEN + 'Trying again...')
else:
    quit()
print(Fore.GREEN + 'Congratulations, you beat level 3 (1/8 chance)')
t.sleep(1)
print(Fore.BLUE + 'Enter 1 to start level 4 (1/16 Chance):')
levelone = int(input(': '))
if levelone == 1:
    while True:
        levelonerng = random.randint(0, 15)
        print(levelonerng)
        if levelonerng == 0:
            break
        else:
            print(Fore.BLUE + 'Trying again...')
else:
    quit()
print(Fore.BLUE + 'Congratulations, you beat level 4 (1/16 chance)')
t.sleep(1)
print(Fore.MAGENTA + 'Enter 1 to start level 5 (1/32 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 31)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.MAGENTA + 'Trying again...')
else:
    quit()
print(Fore.MAGENTA + 'Congratulations, you beat level 5 (1/32 chance)')
t.sleep(1)
print(Fore.RED + Back.WHITE + 'Enter 1 to start level 6 (1/64 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 63)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.RED + Back.WHITE + 'Trying again...')
else:
    quit()
print(Fore.RED + Back.WHITE + 'Congratulations, you beat level 6 (1/64 chance)')
t.sleep(1)
print(Fore.YELLOW + Back.WHITE + 'Enter 1 to start level 7 (1/128 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 127)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.YELLOW + Back.WHITE + 'Trying again...')
else:
    quit()
print(Fore.YELLOW + Back.WHITE + 'Congratulations, you beat level 7 (1/128 chance)')
t.sleep(1)
print(Fore.GREEN + Back.WHITE + 'Enter 1 to start level 8 (1/256 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 255)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.GREEN + Back.WHITE + 'Trying again...')
else:
    quit()
print(Fore.GREEN + Back.WHITE + 'Congratulations, you beat level 8 (1/256 chance)')
t.sleep(1)
print(Fore.BLUE + Back.WHITE + 'Enter 1 to start level 9 (1/512 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 511)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.BLUE + Back.WHITE + 'Trying again...')
else:
    quit()
print(Fore.BLUE + Back.WHITE + 'Congratulations, you beat level 9 (1/512 chance)')
t.sleep(1)
print(Fore.MAGENTA + Back.WHITE + 'Enter 1 to start level 10 (1/1024 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 1023)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Fore.MAGENTA + Back.WHITE + 'Trying again...')
else:
    quit()
print(Fore.MAGENTA + Back.WHITE + 'Congratulations, you beat level 10 (1/1024 chance)')
t.sleep(1)
print(Back.WHITE + Fore.BLACK + 'Enter 1 to start level 11 (1/2048 Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, 2047)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.WHITE + Fore.BLACK + 'Trying again...')
else:
    quit()
print(Back.WHITE + Fore.BLACK + 'Congratulations, you beat level 11 (1/2048 chance)')
t.sleep(1)
print('From now on, levels will be in beta.')
t.sleep(1)
levelno = 12
chances = 4096
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances - 1)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 13
chances = 8192
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 14
chances = 16384
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 15
chances = 32786
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 16
chances = 65536
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 17
chances = 131072
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 18
chances = 262144
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 19
chances = 524288
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 20
chances = 1048576
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 21
chances = 2097152
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 22
chances = 4194304
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 23
chances = 8388608
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 24
chances = 16777216
print(Back.BLACK + Fore.WHITE + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLACK + Fore.WHITE + 'Trying again...')
else:
    quit()
print(Back.BLACK + Fore.WHITE + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
print('How did you get here? Are you cheating?')
t.sleep(1)
levelno = 25
chances = 33554432
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 26
chances = 67108864
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 27
chances = 134217728
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 28
chances = 268435456
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 29
chances = 536870912
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
levelno = 30
chances = 536870912
print(Back.BLUE + Fore.GREEN + 'Enter 1 to start level', levelno, '(1/', chances, 'Chance):')
level = int(input(': '))
if level == 1:
    while True:
        levelrng = random.randint(0, chances)
        print(levelrng)
        if levelrng == 0:
            break
        else:
            print(Back.BLUE + Fore.GREEN + 'Trying again...')
else:
    quit()
print(Back.BLUE + Fore.GREEN + 'Congratulations, you beat level', levelno, '(1/', chances, 'chance)')
t.sleep(1)
print(Back.BLACK + Fore.RED + 'Well, you did it.  You must be the luckiest person alive or are good at cheating. If you did it fully legitimatley, you beat 30 levels of pure RNG. The last level had a 1/536870912 chance of beating it. That is a 1.86264515e-9% chance of beating it. Well done.')
quitting = int(input('Input 1 to quit the game: '))
if quitting == 1:
    quit()
else:
    print('lol okay')
    t.sleep(1)
