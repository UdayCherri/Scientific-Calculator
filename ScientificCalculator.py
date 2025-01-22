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

def exponentialfn():
    print("Performing Exponential operations...")

def arithmeticfn():
    print("Performing Arithmetic operations...")

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
