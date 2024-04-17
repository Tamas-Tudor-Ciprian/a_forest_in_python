

from colorama import Fore , Back , Style
from screen_buffer_handling import *

# myConsole.WriteConsole("Hello World!") # Effectively the print func.
# myConsole.WriteConsoleOutputCharacter(Characters="Hello World!\0", WriteCoord=win32console.PyCOORDType(5,5)) # Print at coordinates
#
# time.sleep(3) # this must be called or you won't see results. This is because after running the code (because there is no loop) the cmd.exe takes the console over.

# myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE,
#                                                        ShareMode=0, SecurityAttributes=None,
#                                                        Flags=1)  # create screen buffer



def random_fire_simulation():
    TREE = Fore.GREEN + '↑'
    FIRE = Fore.LIGHTYELLOW_EX + 'ш'
    INTENSE_FIRE = Fore.RED + 'Ш'
    handler = buffer_handler()
    counter = 10

    fire_buffer = []

    for i in range(WIDTH*HEIGHT):
        fire_buffer.append(0)

    while True:

        if counter == 10:
            handler.add_to_random_location(TREE)
            counter = 0
        counter = counter + 1
        handler.print(0.1)

        handler.remove(INTENSE_FIRE)
        handler.random_replace(TREE,FIRE)
        handler.replace(FIRE,INTENSE_FIRE)

        for i in range(WIDTH*HEIGHT):
            x_coord , y_coord = linear_to_cartesian(i,WIDTH)
            if handler.buffer[i] == TREE:
                if random.randrange(3) == 2:
                    handler.add_to_surrounding_random_location(i,TREE)
                if handler.check_around_for_element(x_coord,y_coord,FIRE) == True or handler.check_around_for_element(x_coord,y_coord,INTENSE_FIRE) == True:
                    fire_buffer[i] = 1

        for i in range(WIDTH*HEIGHT):
            if fire_buffer[i] == 1:
                fire_buffer[i] = 0
                handler.buffer[i] = FIRE







def center_fire_simulation():
    TREE = Fore.GREEN + '↑'
    FIRE = Fore.LIGHTYELLOW_EX + 'ш'
    INTENSE_FIRE = Fore.RED + 'Ш'
    handler = buffer_handler()
    counter = 10

    fire_buffer = []

    for i in range(WIDTH*HEIGHT):
        fire_buffer.append(0)

    handler.add(WIDTH//2,HEIGHT//2,TREE)

    counter = 0

    while True:

        counter = counter+1

        if counter==50:
            handler.add(WIDTH//2,HEIGHT//2,FIRE)

        handler.print(0.1)

        handler.remove(INTENSE_FIRE)
        handler.replace(FIRE,INTENSE_FIRE)

        for i in range(WIDTH*HEIGHT):
            x_coord , y_coord = linear_to_cartesian(i,WIDTH)
            if handler.buffer[i] == TREE:
                if random.randrange(3) == 2:
                    handler.add_to_surrounding_random_location(i,TREE)
                if handler.check_around_for_element(x_coord,y_coord,FIRE) == True or handler.check_around_for_element(x_coord,y_coord,INTENSE_FIRE) == True:
                    fire_buffer[i] = 1

        for i in range(WIDTH*HEIGHT):
            if fire_buffer[i] == 1:
                fire_buffer[i] = 0
                handler.buffer[i] = FIRE

