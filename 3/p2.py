import re


def extract_nums(string):
    res = 0
    pat_mul = r"mul\(\d+,\d+\)"
    pat_do = r"do\(\)"
    pat_dont = r"don't\(\)"

    m_mul = re.findall(pat_mul, string)
    iter_mul = re.finditer(pat_mul, string)
    m_do = re.findall(pat_do, string)
    iter_do = re.finditer(pat_do, string)
    m_dont = re.findall(pat_dont, string)
    iter_dont = re.finditer(pat_dont, string)

    mul_list = []
    do_list = []
    dont_list = []
    for i, m in enumerate(iter_mul):
        mul_list.append((m.start(), m_mul[i]))
    for i, m in enumerate(iter_do):
        do_list.append((m.start(), m_do[i]))
    for i, m in enumerate(iter_dont):
        dont_list.append((m.start(), m_dont[i]))
    
    new_list = mul_list + do_list + dont_list
    sorted_list = sorted(new_list, key=lambda x: x[0])

    do = True
    for tup in sorted_list:
        i, string = tup
        string = str(string)
        if string == "do()":
            do = True
        elif string == "don't()":
            do = False
        elif string[0] == "m" and do:
            x, y = string.split(",")
            x = int(x[4:])
            y = int(y[:-1])
            res += x * y
    
    return res

raw = open("i1").read()
# i0 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
res = extract_nums(raw)

print(res)