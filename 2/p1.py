lines = open("i1").readlines()
res = 0

for line in lines:
    valid = True
    inc = 0
    dec = 0
    line = line.split()
    
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
 
    if valid:
        res += 1

print(res)
            