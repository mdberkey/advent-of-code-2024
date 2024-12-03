import re


def extract_nums(string):
    res = 0
    pattern = r"mul\(\d+,\d+\)"

    match = re.findall(pattern, string)
    for m in match:
        x, y = m.split(",")
        x = int(x[4:])
        y = int(y[:-1])
        res += x * y
    
    return res

raw = open("input").read()

res = extract_nums(raw)

print(res)