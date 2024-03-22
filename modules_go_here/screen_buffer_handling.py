import win32console,win32con
from some_math import *
from os import system,name
import time

WIDTH = 120
HEIGHT = 30
EMPTY = ' '

class buffer_handler:
    buffer = []

    x = y = 0
    myConsole = win32console.CreateConsoleScreenBuffer(DesiredAccess=win32con.GENERIC_READ | win32con.GENERIC_WRITE,
                                                       SecurityAttributes=None,
                                                       Flags=1)  # create screen buffer
    def __init__(self):
        self.myConsole.SetConsoleActiveScreenBuffer()  # set this buffer to be active
        for i in range(WIDTH * HEIGHT):
            self.buffer.append(EMPTY)

    def add_to_random_location(self, to_add):
        random_coord = random.randrange(0, WIDTH * HEIGHT)
        if self.buffer[random_coord] == EMPTY:
            self.buffer[random_coord] = to_add
    def random_replace(self,to_change):
        pass
    def add_to_surrounding_random_location(self, x, y,to_add):
        coord_x , coord_y = random_location_around_cartesian_coordinate(x,y,WIDTH)
        if cartesian_to_linear(coord_x,coord_y,WIDTH)<WIDTH*HEIGHT:
            if self.buffer[cartesian_to_linear(coord_x,coord_y,WIDTH)] == EMPTY:
                self.buffer[cartesian_to_linear(coord_x,coord_y,WIDTH)] = to_add

    def add_to_surrounding_random_location(self, x,to_add):
        coord_x, coord_y = linear_to_cartesian(x,WIDTH)
        coord_x , coord_y = random_location_around_cartesian_coordinate(coord_x, coord_y)
        if cartesian_to_linear(coord_x,coord_y,WIDTH)<WIDTH*HEIGHT:
            if self.buffer[cartesian_to_linear(coord_x,coord_y,WIDTH)] == EMPTY:
                self.buffer[cartesian_to_linear(coord_x,coord_y,WIDTH)] = to_add

    def remove(self,to_be_removed):
        for i in range(WIDTH*HEIGHT):
            if self.buffer[i] == to_be_removed:
                self.buffer[i] = EMPTY

    def replace(self,to_be_replaced,replacement):
        for i in range(WIDTH*HEIGHT):
            if self.buffer[i] == to_be_replaced:
                self.buffer[i] = replacement


    def print(self,sleep_time):
        system('cls')
        self.myConsole.WriteConsole("".join(self.buffer))
        time.sleep(sleep_time)

