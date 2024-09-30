import math

#challenge 4
def quadratic(a=-4.9, c=11000):
        if (a == 0):
            return "no"
        while True:
            try:
                b = -1*float(input("Initial Velocity (as a positive value as the equation flips it):"))
                break
            except ValueError:
                print("Not a float")
        try:
            t = [((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a), ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)]
        except:
            return "otherwise no real values of t"
        return f"The parcel will land after {t} seconds"

#challenge 6
def cylinder():
    while True:
        try:
            r = float(input("Radius:"))
            h = float(input("Height:"))
            break
        except ValueError:
            print("Not a float")
    v = math.pi*(r**2)*h
    sa = (2*(v/h))+(h*2*math.pi*r)
    print("The volume is:", v)
    print("The surface area is:", sa)

#challenge 7
def multiples():
    while True:
        try:
            num = int(input("Number to multiply:"))
            if num > 0:
                break
            print("Value is either negative or 0")
        except ValueError:
            print("Not a number")
    m = 1;
    while (num*m <= 20):
        print(num*m)
        m+=1

quadratic()
cylinder()
multiples()