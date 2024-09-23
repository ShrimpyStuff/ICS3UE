import math

angle_rad = math.radians(float(input("Please input the angle of inclination in degrees: ")))
distance = float(input("Please input the distance from the object: "))
height = math.tan(angle_rad)*distance
print("The height of the object is", height)