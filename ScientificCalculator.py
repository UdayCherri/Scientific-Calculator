PIE = 3.141592653589793

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sine(x, terms=10):
    x = x * (PIE / 180) 
    sine_value = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sine_value += term
    return sine_value

def cosine(x, terms=10):
    x = x * (PIE / 180) 
    cosine_value = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cosine_value += term
    return cosine_value

def tangent(x):
    sin_x = sine(x)
    cos_x = cosine(x)
    if cos_x != 0:
        return sin_x / cos_x
    else:
        return 'Undefined (cos(x) = 0)'

def cosecant(x):
    sin_x = sine(x)
    if sin_x != 0:
        return 1 / sin_x
    else:
        return 'Undefined (sin(x) = 0)'

def secant(x):
    cos_x = cosine(x)
    if cos_x != 0:
        return 1 / cos_x
    else:
        return 'Undefined (cos(x) = 0)'

def cotangent(x):
    tan_x = tangent(x)
    if tan_x != 0:
        return 1 / tan_x
    else:
        return 'Undefined (tan(x) = 0)'

def logarithm(x, terms=10):
    if x <= 0:
        return 'Undefined (logarithm for x <= 0)'
    y = x - 1
    ln_x = 0
    for n in range(1, terms + 1):
        term = ((-1) ** (n + 1)) * (y ** n) / n
        ln_x += term
    return ln_x
   
def log_base(x, base, terms=10):
    ln_x = logarithm(x, terms)
    ln_base = logarithm(base, terms)
    if isinstance(ln_x, str) or isinstance(ln_base, str):
        return 'Invalid input for logarithm'
    return ln_x / ln_base

def exponential(x, terms=10):
    exp_x = 1
    for n in range(1, terms + 1):
        term = (x ** n) / factorial(n)
        exp_x += term
    return exp_x

def arithmetic():
    print("\nChoose an arithmetic operation:")
    print("1. Add (+)    2. Subtract (-)    3. Multiply (*)    4. Divide (/)")
    op = int(input("Enter the operation index: "))
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    if op == 1:
        print(f"{a} + {b} = {a + b}")
    elif op == 2:
        print(f"{a} - {b} = {a - b}")
    elif op == 3:
        print(f"{a} * {b} = {a * b}")
    elif op == 4:
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

def trigonometricfn():
    print("Performing Trigonometric operations...\n")
    tMenu = 1000
    while tMenu != 7:
        print("\n1.sin          2.cos          3.tan\n4.cosec          5.sec          6.cot          7.EXIT\n")
        tMenu = int(input("Enter the index of the operation:"))
        if tMenu >= 7:
            print("Invalid Input, Please enter a valid input.")
            continue
        else:
            x = int(input("Enter the value of x (in degrees): "))
        
        if tMenu == 1:
            print(f"sin({x}°) = {sine(x)}")
        elif tMenu == 2:
            print(f"cos({x}°) = {cosine(x)}")
        elif tMenu == 3:
            print(f"tan({x}°) = {tangent(x)}")
        elif tMenu == 4:
            print(f"cosec({x}°) = {cosecant(x)}")
        elif tMenu == 5:
            print(f"sec({x}°) = {secant(x)}")
        elif tMenu == 6:
            print(f"cot({x}°) = {cotangent(x)}")
        elif tMenu == 7:
            break
        else:
            print("Invalid Input, Please enter a valid input.")

def logarithmicfn():
    print("Performing Logarithmic operations...")
    x = float(input("Enter the value of x: "))
    if x > 0:
        print(f"ln({x}) = {logarithm(x)}")
    else:
        print("Logarithm undefined for x <= 0.")
    
    base = float(input("Enter the base: "))
    if base > 0 and base != 1:
        print(f"log_{base}({x}) = {log_base(x, base)}")
    else:
        print("Invalid base for logarithm.")

def exponentialfn():
    print("Performing Exponential operations...")
    x = float(input("Enter the value of x: "))
    print(f"e^{x} = {exponential(x)}")

def arithmeticfn():
    print("Performing Arithmetic operations...")
    arithmetic()

if __name__ == '__main__':
    print("")
    print("   _____      _            __  _ _____         ______      __            __            ")
    print("  / ___/_____(_)__  ____  / /_(_) __(_)____   / ____/___ _/ /_  ______ _/ /_____  _____")
    print("  \\__ \\/ ___/ / _ \\/ __ \\/ __/ / /_/ / ___/  / /   / __ `/ / / / / __ `/ __/ __ \\/ ___/")
    print(" ___/ / /__/ /  __/ / / / /_/ / __/ / /__   / /___/ /_/ / / /_/ / /_/ / /_/ /_/ / /    ")
    print("/____/\\___/_/\\___/_/ /_/\\__/_/_/ /_/\\___/   \\____/\\__,_/_/\\__,_/\\__,_/\\__/\\____/_/     ")

    opMenu = 1000
    while opMenu != 1 and opMenu != 2 and opMenu != 3 and opMenu != 4:
        print("\nWhat operation do you want to perform?\n\n1.Trigonometric     2.Logarithmic     3.Exponential     4.Arithmetic")
        opMenu = int(input("Enter the index of the operation:"))
        if opMenu == 1:
            trigonometricfn()
            break
        elif opMenu == 2:
            logarithmicfn()
            break
        elif opMenu == 3:
            exponentialfn()
            break
        elif opMenu == 4:
            arithmeticfn()
            break
        else:
            print("Invalid Input, Please enter a valid input.")
