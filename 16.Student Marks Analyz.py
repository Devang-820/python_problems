
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