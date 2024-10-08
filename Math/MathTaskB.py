import math

def cirle_area(radius: float):
    '''A function that calculates the area of a circle using the input radius'''
    try:
        ans = math.pi * radius**2
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cylinder_volume(radius: float, height: float = 10):
    try:
        ans = math.pi * radius**2 * height
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def sphere_volume(radius: float):
    try:
        ans = 4/3 * math.pi * radius**3
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cone_volume(radius: float, height: float = 10):
    try:
        ans = math.pi * radius**2 * height / 3
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)
