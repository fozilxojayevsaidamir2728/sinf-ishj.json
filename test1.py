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

# 3. Har bir branchda nechta o'quvchi bor
for branch in branches:
    print(branch["name"], len(branch["students"]))
