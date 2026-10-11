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