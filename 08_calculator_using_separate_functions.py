# Difficulty: Hard
# Topic: Calculator using separate functions

# Each operation gets its own small function
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


# This function picks the right operation based on the symbol
def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Error: unknown operator"


# Main program: ask the user for input and show the result
def main():
    print("Simple Calculator (+, -, *, /)")
    a = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    b = float(input("Enter second number: "))
    print("Result:", calculate(a, operator, b))


# Only run main() when this file is executed directly
if __name__ == "__main__":
    main()
