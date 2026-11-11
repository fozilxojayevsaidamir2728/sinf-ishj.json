import json

with open("academy.json", "r") as ptr:
    data = json.load(ptr)

branches = data["branches"]

# 1. Barcha branch nomlari
for branch in branches:
    print(branch["name"])


# 2. Faqat Python o'qituvchilari
for branch in branches:
    for teacher in branch["teachers"]:
        if teacher["subject"] == "pyton":
            print(teacher["name"], branch["name"], teacher["experience"])

# # 3. Har bir branchda nechta o'quvchi bor
for branch in branches:
    print(branch["name"], len(branch["students"]))

# 4. Eng ko'p payment to'layotgan o'quvchi
max_payment = 0
student_name = ""
branch_name = ""

for branch in branches:
    for student in branch["students"]:
        if student["payment"] > max_payment:
            max_payment = student["payment"]
            student_name = student["name"]
            branch_name = branch["name"]

print(student_name, branch_name, max_payment)

