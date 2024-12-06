
with open("i1") as f:
    lines = [line.strip() for line in f.readlines()]
    left_nums = []
    right_nums = []


    for line in lines:
        l, r = line.split()
        l = int(l)
        r = int(r)
        left_nums.append(l)
        right_nums.append(r)
    
    from collections import Counter

    vals = Counter(right_nums)

    res = 0
    for l in left_nums:
        res += l * vals[l]
    
    print(res)