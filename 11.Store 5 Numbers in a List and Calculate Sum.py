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