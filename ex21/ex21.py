def add(a, b):
    print(f"adding {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"subtract {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"multiple {a} * {b}")
    return a * b


def divide(a, b):
    print(f"divide {a} / {b}")
    return int(a / b)


print("Let's do some math with just functions !")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"""
Age : {age}
Height : {height}
Weight : {weight}
IQ : {iq}
""")
# a puzzle for the extra credit ,type it in anyway

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes L", what, "Can you do it by hand ?")
