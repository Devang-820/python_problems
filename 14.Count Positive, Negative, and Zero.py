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
