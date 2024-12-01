
with open("input") as f:
    lines = [line.strip() for line in f.readlines()]
    left_nums = []
    right_nums = []

    for line in lines:
        l, r = line.split()
        l = int(l)
        r = int(r)
        left_nums.append(l)
        right_nums.append(r)
    
    left_nums.sort()
    right_nums.sort()

    res = 0
    for l, r in zip(left_nums, right_nums):
        res += abs(l - r)
    
    print(res)
