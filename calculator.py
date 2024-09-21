import calheading
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a+b
operations_dictionary={
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
def calculator():
    number1=float(input("enter the first number\n"))
    for symbols in operations_dictionary:
        print(symbols)
    continue_cal = True
    while continue_cal:
        op_symbol = input("pick an operation\n")
        number2 = float(input("enter the second number\n"))
        calculator_function=operations_dictionary[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue = input(f"enter y to continue calculation with {output} or n to start new calculation or x to exit\n")
        if should_continue=="y":
            number1=output
        elif should_continue=="n":
            continue_cal=False
            calculator()
        else:
            continue_cal=False
            print("have a good day")
print(calheading.logo)
calculator()