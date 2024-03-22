

from colorama import Fore , Back , Style
from screen_buffer_handling import *

# myConsole.WriteConsole("Hello World!") # Effectively the print func.
# myConsole.WriteConsoleOutputCharacter(Characters="Hello World!\0", WriteCoord=win32console.PyCOORDType(5,5)) # Print at coordinates
#
# time.sleep(3) # this must be called or you won't see results. This is because after running the code (because there is no loop) the cmd.exe takes the console over.

# myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE,
#                                                        ShareMode=0, SecurityAttributes=None,
#                                                        Flags=1)  # create screen buffer



def simulation():
    TREE = Fore.GREEN + 'T'
    Fire = Fore.LIGHTRED_EX + 'F'
    INTENSE_FIRE = Fore.RED + 'F'
    handler = buffer_handler()
    counter = 10
    while True:
        if counter == 10:
            handler.add_to_random_location(TREE)
            counter = 0
        counter = counter + 1
        handler.print(0.1)
        for i in range(WIDTH*HEIGHT):
            if handler.buffer[i] == TREE:
                handler.add_to_surrounding_random_location(i,TREE)




simulation()