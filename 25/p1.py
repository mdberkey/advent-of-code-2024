def get_heights(section, is_lock):
    heights = [0] * len(section[0])
    if not is_lock:
        section.reverse()
    section = section[1:-1]
    for row in section:
        for i, char in enumerate(row):
            if char == "#":
                heights[i] += 1
    
    return tuple(heights)
                
if __name__ == "__main__":
    lines = open("25/i1.txt").read()
    keys = []
    locks = []

    for section in lines.split("\n\n"):
        if section.startswith("#####"):
            locks.append(get_heights(section.split(), is_lock=True))
        else:
            keys.append(get_heights(section.split(), is_lock=False))
    
    res = 0    
    for key in keys:
        for lock in locks:
            valid = True
            for k, l in zip(key, lock):
                if k + l > 5:
                    valid = False
                    break
            if valid:
                res += 1

    print(res)