import random

def cartesian_to_linear(x,y,WIDTH):
    return x*WIDTH+y

def linear_to_cartesian(x,WIDTH):
    y = x%WIDTH
    x = x//WIDTH
    return x,y

def random_location_around_cartesian_coordinate(x,y):
    around_tuple = ((x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1),(x + 1, y + 1))
    holder = random.choice(around_tuple)
    holder_x = holder[0]
    holder_y = holder[1]
    return holder_x,holder_y



