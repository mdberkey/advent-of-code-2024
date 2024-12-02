import math
from copy import deepcopy


lines = open("input").readlines()
res = 0

def is_line_valid(line):
    valid = True
    inc = 0
    dec = 0

    for i, val in enumerate(line):
        val = int(val)
        if i == len(line) - 1:
            continue
        next = int(line[i+1])
        if abs(next - val) > 3 or abs(next - val) < 1:
            valid = False
            break
        if next - val > 0:
            inc += 1
        elif next - val < 0:
            dec += 1
        else:
            valid = False
            break

    if (inc > 0 and dec != 0) or (dec > 0 and inc != 0):
        valid = False

    return valid


for line in lines:
    line = line.split()

    for i in range(len(line) + 1):
        if i == len(line):
            if is_line_valid(line):
                res += 1
                break
        else:
            new_line = deepcopy(line)
            new_line = new_line[:i] + new_line[i+1:]
            if is_line_valid(new_line):
                res += 1
                break

print(res)
            