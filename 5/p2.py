import math


lines = open("input").read().splitlines()
res = 0

rules = []
updates = []

for i in range(len(lines)):
    if lines[i] == "":
        break

rule_lines = lines[:i]
update_lines = lines[i+1:]
rules = {}
updates = []

for r in rule_lines:
    l, r = (int(x) for x in r.split("|"))
    if l not in rules:
        rules[l] = []
    rules[l].append(r)

for u in update_lines:
    updates.append([int(x) for x in u.split(",")])

for u in updates:
    # omg it's bubble sort!!!
    invalid = False
    for i in range(len(u)):
        for j in range(len(u) - 1):
            if u[j] not in rules or u[j+1] not in rules[u[j]]:
                invalid = True
                u[j], u[j+1] = u[j+1], u[j]
    if invalid:
        res += u[(len(u) // 2)]

print(res)
