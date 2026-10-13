# Problem 2


num1 = int(input("Enter the first number: "))
OPERATOR = input("Enter the operator (+ - * / // % **): ")
num2 = int(input("Enter the second number: "))

if OPERATOR == "+":
    result = num1 + num2

elif OPERATOR == "-":
    result = num1 - num2

elif OPERATOR == "*":
    result = num1 * num2

elif OPERATOR == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

elif OPERATOR == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Cannot divide by zero"

elif OPERATOR == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Cannot divide by zero"

elif OPERATOR == "**":
    result = num1 ** num2

else:
    result = "Invalid operator"

if isinstance(result, (int, float)):
    print("Result:", round(result, 3))
else:
    print("Result:", result)


# Problem 2 ended
