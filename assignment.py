num1 = input("Enter first number:")
num2 = input("Enter second number:")
operator = input("Enter operator +,-,/:")
if operator == "+" :
    result = int(num1) + int(num2)
elif operator == "-":
    result = int(num1) - int(num2)
elif operator == "*":
    result = int(num1) * int(num2)


print("Result:", result)