import math

def quadratic(a, b, c):
    try:
        x = [((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a), ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)]
        return f"x could be {x}"
    except:
        return "There are no possible x's"

print(quadratic(-1, 2, 3))