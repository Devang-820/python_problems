# Problem 2

num1 = int(input("Enter the number: "))
OPERATOR = input("Enter the operator (+ - * /): ")
num2 = int(input("Enter the number: "))

if OPERATOR == "+":
    result = num1 + num2
    print(round(result, 3))

elif OPERATOR == "-":
    result = num1 - num2
    print(round(result, 3))

elif OPERATOR == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    OPERATOR == "*"
    result = num1 * num2
    print(round(result, 3))

# Problem 2 ended
