#1
student = {
    "Name": "devang",
    "age": 22,
    "course": "cse"
}

student.update({"city": "Delhi"})

student["age"] = 23
student["course"]="AI/ML"

print(student)
print(student["course"])



##2

student = {
   "name": "Devang",
    "age": 22,
    "marks": 80
}
student["marks"]
student.update({"marks":90})
if student["marks"]>=85:
    print("Excellent marks!")
else:
    print("Keep practicing!")

     
##3

student = {
    "name": "Devang",
    "details": {
              #  "age": 22,
                  "course": "CSE",
                   "city": "Delhi"
                }
}
student["details"]["course"] = "AI/ML"
student["details"]["marks"] = 90
print(student["name"])
print(student["details"]["age"])



##4

students = [
    {"name": "Devang", "age": 22, "marks": 90},
    {"name": "Rahul", "age": 21, "marks": 85},
    {"name": "Aman", "age": 23, "marks": 78}
]
students.append({"name": "priya", "age": 22, "marks": 98})
students[2]["marks"]=88

print(students[0]["name"])
print(students[1]["marks"])
print(students)


