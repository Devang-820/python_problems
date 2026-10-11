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