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