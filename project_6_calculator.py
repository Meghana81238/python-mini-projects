import os

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

symbol={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }

number_1=float(input("enter first number"))
continue_flag=True
while continue_flag:
        for operator in symbol:
             print(operator)
        operator=input("pick an operator")    
        number_2=float(input("enter second number"))
        opertaion=symbol[operator]
        output=opertaion(number_1,number_2)
        print(f"{number_1}{operator}{number_2}={output}")
        continue_calculation=input(f"enter 'y' to continue calculation with {output} or enter 'n' to start new calculation or enter 'x' to exit:")
        if continue_calculation=='y':  
             number_1=output

        elif continue_calculation=='n':
             os.system('cls')
             number_1=float(input("enter first number"))

        else:
             continue_flag=False
             print("bye")