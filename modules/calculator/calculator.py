total: float = 0
operator: str = None

def addition(x: float, y: float) -> float:
    return x + y

def subtraction(x: float, y: float) -> float:
    return x - y

def multiplication(x: float, y: float) -> float:
    return x * y

def division(x: float, y: float) -> float:
    return x / y

def power(x: float, y: float) -> float:
    return x ** y

def modulus(x:float, y: float) -> float:
    return x % y

op_list = {
    "*": multiplication,
    "/": division, 
    "+": addition, 
    "-": subtraction, 
    "^": power, 
    "**": power,
    "%": modulus
}

def __is_operator(entry: str):
    # return entry in ["*", "/", "+", "-", "^", "**"]
    return entry in op_list

def __calculate(operator, left, right):
    return op_list[operator](left, right)
    # if operator == "*":
    #     return multiplication(left, right)
    # elif operator == "/":
    #     return division(left, right)
    # elif operator == "+":
    #     return addition(left, right)
    # elif operator == "-":
    #     return subtraction(left, right)
    # elif operator in ["^", "**"]:
    #     return power(left, right)

print("This is a Basic Calculator App.")
print("Please hit enter after entry of each number, operator, or state-letters.")
print("You may use letter 'c' and 'x' for reset and exit respectively")
print(total)
while True:
    entry: str = input(": ").lower()
    
    if entry.isnumeric():
        entry = float(entry)
        if operator is None:
            total = entry
            # print (f"Enter operator", end="") 
        else:
            print (total, operator, entry) #, end=" = ")
            total = __calculate(operator, total, float(entry))
            print(total)
    elif __is_operator(entry):
        operator = entry
        # print(f"{total} {operator}")
    else:
        #  probably reset?
        if entry == "c":
            total, operator = 0, None
            print(total)
        elif entry == "x":
            print("terminating calculator app")
            break
        else:
            print("unexpected entry")
