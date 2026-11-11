
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

# 5. Har bir branch bo'yicha umumiy tushadigan summa
for branch in branches:
    payment = 0
    for student in branch["students"]:
        tushum = payment + student["payment"]
    print(branch["name"], tushum)

# 6. Tajribasi 5 yildan katta o'qituvchilar
for branch in branches:
    for teacher in branch["teachers"]:
        if teacher["experience"] > 5:
            print(teacher["name"], teacher["experience"])

# 7. Faqat Python kursi o'qitiladigan branchlar
for branch in branches:
    for student in branch["students"]:
        if student["course"] != "Python":
            break
        else:
            print(branch["name"])