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
