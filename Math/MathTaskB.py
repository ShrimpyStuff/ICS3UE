import math

def circle_area(radius: float):
    '''A function that calculates the area of a circle using the input radius'''
    try:
        ans = round(math.pi * radius**2, 2)
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cylinder_volume(radius: float, height: float = 10):
    '''A function that calculates the volume of the cylinder using the input radius and optional height'''
    try:
        ans = math.pi * radius**2 * height
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def sphere_volume(radius: float):
    '''A function that calculates the volume of the sphere using the input radius and optional height'''
    try:
        ans = 4/3 * math.pi * radius**3
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cone_volume(radius: float, height: float = 10):
    '''A function that calculates the volume of the cone using the input radius and optional height'''
    try:
        ans = math.pi * radius**2 * height / 3
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def circle_circumference(radius: float):
    '''A function that calculates the circumference of a circle using the input radius and optional height'''
    try:
        ans = math.pi *radius*2
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cylinder_sa(radius: float, height: float = 10):
    '''A function that calculates the surface area of a cylinder using the input radius and optional height'''
    try:
        ans = (math.pi * radius**2 * 2) + (math.pi*2*radius*height)
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def sphere_sa(radius: float):
    '''A function that calculates the surface area of a sphere using the input radius'''
    try:
        ans = 4 * math.pi * radius**2
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)

def cone_sa(radius: float, height: float = 10):
    '''A function that calculates the surface area of a cone using the input radius and optional height'''
    try:
        ans = round((math.pi * radius) * (radius + math.sqrt(height**2+radius**2)), 2)
        return ans
    except not KeyboardInterrupt as e:
        print("An error occured:", e)