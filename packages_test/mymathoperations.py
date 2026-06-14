def sum_fun(a, b):
    return a + b

def product_fun(a, b):
    return a * b

def difference_fun(a, b):
    return a - b

def quotient_fun(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def power_fun(a, b):
    return a ** b

def modulus_fun(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot perform modulus by zero"