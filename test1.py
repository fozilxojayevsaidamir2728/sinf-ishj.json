import json

with open("academy.json", "r") as ptr:
    data = json.load(ptr)

branches = data["branches"]

# 1. Barcha branch nomlari
for branch in branches:
    print(branch["name"])


