#challenge 1
def square(x: int):
    '''Takes an integer as an argument, and returns the squared value'''
    return x**2

print(square(10))

#challenge 2
def print_stdout(input: str):
    '''Prints the value of the input string to the console'''
    print(input)

print_stdout("Hello World")

#challenge 3
def parameters(add1: float, add2: float, multiplier1:int, multiplier2:int=1, multiplier3:int=1):
    '''Takes in two numbers to add together, their coefficients and then a third multiplier term'''
    value = (multiplier1*add1)+(multiplier2*add2)*multiplier3
    return value

print(parameters(1, 3, 2, 1))
print(parameters(1, 3, 2, 1, 2))

#challenge 4
def half(x: int):
    '''Returns the input integer divided by 2'''
    return x/2

def quadruple(x: int):
    '''Multiplies the input by 4'''
    return x*4

halved = half(2)
quad = quadruple(halved)

print (quad)

#challlenge 5
def str_to_float(string: str):
    '''Attempts to convert string values into a float, if string does not convert, returns False'''
    try:
        num = float(string)
        return num
    except ValueError:
        return False

print(str_to_float("2.4"))
print(str_to_float("Hello"))

#challenge 6
def docstring():
    '''↑ Check above ↑'''
    return "Already Done!"

print(docstring())
