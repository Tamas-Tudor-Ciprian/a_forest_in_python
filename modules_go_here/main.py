import win32console, win32con, time , random
from os import system,name

# myConsole.WriteConsole("Hello World!") # Effectively the print func.
# myConsole.WriteConsoleOutputCharacter(Characters="Hello World!\0", WriteCoord=win32console.PyCOORDType(5,5)) # Print at coordinates
#
# time.sleep(3) # this must be called or you won't see results. This is because after running the code (because there is no loop) the cmd.exe takes the console over.

# myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE,
#                                                        ShareMode=0, SecurityAttributes=None,
#                                                        Flags=1)  # create screen buffer

def simulation():
    myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE, SecurityAttributes=None,
                                                       Flags=1)  # create screen buffer
    myConsole.SetConsoleActiveScreenBuffer()  # set this buffer to be active
    WIDTH = 120
    HEIGHT = 30
    buffer = []
    for i in range(WIDTH*HEIGHT):
        buffer.append(" ")
    while True:
        myConsole.WriteConsole("".join(buffer))
        time.sleep(1)
        system('cls')
        buffer[random.randrange(0,WIDTH*HEIGHT)] = "T"

def cartesian_to_linear():
    pass

def linear_to_cartesian():
    pass


simulation()