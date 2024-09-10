import cmath

def quadratic(a, b, c):
        if (a == 0):
            return "no"
        x = [((-b) - cmath.sqrt((b**2)-(4*a*c)))/(2*a), ((-b) + cmath.sqrt((b**2)-(4*a*c)))/(2*a)]
        return f"x could be {x}"
    
print(quadratic(1, 2, 3))