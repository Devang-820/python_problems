# Problem 1

name = input("enter your name: ")
age = int(input("Your age: "))
city = input("city: ")

print(f"Your name is {name}, you are {age} years old and live in {city}")

# Problem 1 ended


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


# Problem 3

num = int(input("Enter the number"))

if num == 0:
    print("Zero")

elif num < 0:
    print("Negative")

else:
    print("Positive")

# Problem 3 ended


# Problem 4

num = int(input("enter the number:"))

if num == 0:
    print("zero")

elif num % 2 == 0:
    print("even")

else:
    print("The number is odd")

# Problem 4 ended


# Problem 5

num = int(input("enter the number"))

for i in range(1, num + 1):
    print(i)

# Problem 5 ended


# Problem 6

num = int(input("Enter the number: "))

count = 0

for i in range(0, num):
    if i % 2 == 0:
        count = count + 1

print(count)

# Problem 6 ended


# Problem 7

num = int(input("Enter the number: "))

total = 0

for i in range(1, num + 1):
    total = total + i

print(total)

# Problem 7 ended


# Problem 8

num = int(input("Enter the number: "))

total = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        total = total + i

i % 2 == 0    # even
i % 2 != 0    # odd

print(total)

# Problem 8 ended


# Problem 9

num = int(input("Enter the number: "))

count = 0
total = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        count = count + 1
        total = total + i

print("Number of odd numbers:", count)
print("Sum of odd numbers:", total)

# Problem 9 ended


# Problem 10

largest_number = 0

for i in range(5):
    num = int(input("Enter the number: "))

    if num > largest_number:
        largest_number = num

print("Largest number:", largest_number)

# Problem 10 ended


# Problem 11

total = []
sum = 0

# Loop 1: collect numbers
for i in range(5):
    num = int(input("Enter the number: "))
    total.append(num)

# Loop 2: add numbers from the list
for num in total:
    sum = sum + num

print(sum)

# Problem 11 ended


# Problem 12

largest_num = 0

for i in range(5):
    num = int(input("Enter the number: "))

    if num > largest_num:
        largest_num = num

print("Largest number:", largest_num)

# Problem 12 ended


# Problem 13

num = int(input("Enter the number: "))

largest_num = 0
smallest_num = 0

for i in range(4):
    num = int(input("Enter the number: "))

    if num > largest_num:
        largest_num = num

    if num < smallest_num:
        smallest_num = num

print(f"the smalles number is {smallest_num} and the largest number is {largest_num}")

# Problem 13 ended


# Problem 14

positive = 0
negative = 0
zero = 0

for i in range(5):
    Number = int(input("Enter the number: "))

    if Number > 0:
        positive = positive + 1

    elif Number < 0:
        negative = negative + 1

    else:
        zero = zero + 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

# Problem 14 ended


# Problem 15

even = 0
odd = 0
sum = 0

for i in range(5):
    num = int(input("enter the number"))

    if num % 2 == 0:
        even = even + 1

    elif num % 2 != 0:
        odd = odd + 1

    sum = sum + num

print("Even:", even)
print("Odd:", odd)
print("Sum:", sum)

# Problem 15 ended


# Problem 16

total = 0
passed = 0

for i in range(5):

    marks = int(input("Enter marks: "))

    total = total + marks

    if i == 0:
        highest = marks
        lowest = marks

    else:
        if marks > highest:
            highest = marks

        if marks < lowest:
            lowest = marks

    if marks >= 40:
        passed = passed + 1

    else:
        print("Fail")

average = total / 5

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)

# Problem 16 ended