num1 = input("Enter first num:")
num2 = input("Enter second num:")
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = int(num1) + int(num2)
elif operator == "-":
    result = int(num1) - int(num2)
elif operator == "*":
    result = float(num1) * float(num2)
elif operator == "/":
    if float(num2) != 0:
        result = float(num1) / float(num2)
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
print("Result:", result)