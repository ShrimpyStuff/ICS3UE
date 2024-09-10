import cmath

#shows complex solutions cause why not. All I need to do is add a c
def quadratic(a, c):
        if (a == 0):
            return "no"
        b = -1*float(input("Initial Velocity (as a positive value cause the equation flips it):"))
        try:
            x = [((-b) - cmath.sqrt((b**2)-(4*a*c)))/(2*a), ((-b) + cmath.sqrt((b**2)-(4*a*c)))/(2*a)]
        except:
            return "if you kept it complex then I don't even know, otherwise no real values of x"
        return f"x could be {x}"
    
print(quadratic(-4.9, 11000))