import cmath as math

#challenge 1
def egg_carton():
    eggs = int(input("Number of Eggs:"))
    print("Number of Cartons that can be filled:", eggs // 12)
    print("Eggs left over:", eggs % 12)

#challenge 4
#shows complex solutions cause why not. All I need to do is add a c
def quadratic(a=-4.9, c=11000):
        if (a == 0):
            return "no"
        b = -1*float(input("Initial Velocity (as a positive value cause the equation flips it):"))
        try:
            x = [((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a), ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)]
        except:
            return "if you kept it complex then I don't even know, otherwise no real values of x"
        return f"x could be {x}"
    
#challenge 3
def geometric():
    a = float(input("A value:"))
    b = float(input("B value:"))
    print("The geometric mean is:", math.sqrt(a*b))

#challenge 5
def tempFtoC():
    c = float(input("Input a temp in celcius to convert to fahrenheit:"))
    print((9/5)*c+32)

#challenge 6
def cylinder():
    r = float(input("Radius:"))
    h = float(input("Height:"))
    v = math.pi*(r**2)*h
    sa = (2*(v/h))+(h*2*math.pi*r)
    print("The volume is:", v)
    print("The surface area is:", sa)

#challenge 7
def multiples():
    num = int(input("Number to multiply:"))
    m = 1;
    while (num*m <= 20):
        print(num*m)
        m+=1

#challenge 8
def fibonacci():
    n = int(input("Nth Term:"))
    a = 0
    b = 1
    if (n == 0):
        return print(f"Term #0 is:", a);
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(f"Term #{n} is:", b)