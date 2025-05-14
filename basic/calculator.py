# Basic Calculator using Conditional Statements
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator entered.")
